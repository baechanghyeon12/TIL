import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

def download_image(img_url, save_dir, file_name):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    try:
        img_resp = requests.get(img_url, stream=True, timeout=10)
        if img_resp.status_code == 200:
            with open(os.path.join(save_dir, file_name), 'wb') as f:
                for chunk in img_resp.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"이미지 다운로드 실패: {img_url}, {e}")
    return False


# 👉 엑셀에서 상품코드 리스트 불러오기
df_input = pd.read_excel("lklab_total_product_code2.xlsx")  # 파일명만 바꾸세요
# g_no_list = df_input.iloc[:, 0].dropna().astype(int).tolist()
g_no_list = df_input.iloc[:, 0].dropna().astype(str).tolist()

# 👉 세션 + 재시도 설정
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36"
}

base_iframe_url = "https://www.lklab.com/product/product_info_order_job.asp?g_no="
rows = []
cnt = 2000
for g_no in g_no_list:
    cnt += 1
    iframe_url = f"{base_iframe_url}{g_no}"
    print(f"[INFO] {cnt}번째 상품 {g_no} 처리 중...")

    try:
        iframe_url = f"https://www.lklab.com/product/product_info_order_job.asp?g_no={g_no}"
        response_order = session.get(iframe_url, headers=headers, timeout=5)
        if response_order.status_code != 200:
            print(f"  ❌ HTTP 오류: {response_order.status_code}")
            continue

        soup = BeautifulSoup(response_order.text, "html.parser")


        item_codes = [td.get_text(strip=True) for td in soup.find_all("td", class_="pr22")]
        item_info = [
            td.get_text(separator='\n', strip=False).split('\n')[0].strip()
            for td in soup.find_all("td", class_="pr2")
        ]

        if not item_codes:
            print("  ⚠️ 품목코드 없음")



        detail_url = f"https://www.lklab.com/product/product_info.asp?g_no={g_no}"
        response_detail = session.get(detail_url, headers=headers, timeout=5)
        if response_detail.status_code != 200:
            print(f"  ❌ 상세정보 HTTP 오류: {response_detail.status_code}")
            # 옵션정보만이라도 계속 진행할 수도 있으나, 여기서는 skip
            continue
        soup_detail = BeautifulSoup(response_detail.text, "html.parser")

        name_eng_tag = soup_detail.find("li", class_="name_eng")
        if name_eng_tag:
            name_eng = name_eng_tag.get_text(strip=True)
        else:
            name_eng = ""  # 값이 없을 때는 빈값 처리


        name_kor_tag = soup_detail.find("li", class_="name_kor")
        if name_kor_tag:
            name_kor = name_kor_tag.get_text(strip=True)
        else:
            name_kor = ""  # 값이 없을 때는 빈값 처리

        keyword = soup_detail.find("p", class_="keyword")
        if keyword:
            it_keyword = keyword.decode_contents()
        else:
            it_keyword = ""  # 값이 없을 때는 빈값 처리


        # === 이미지 크롤링/다운로드 파트 ===
        img_tags = []
        prod_thumb = soup_detail.find(id="thumb_s")
        if prod_thumb:
            img_tags = prod_thumb.find_all("img")

        img_src_list = []
        for idx, img_tag in enumerate(img_tags):
            src = img_tag.get("src")
            if not src:
                continue
            # 절대경로로 변환 (필요시)
            if src.startswith("/"):
                img_url = "https://www.lklab.com" + src
            else:
                img_url = src

            img_src_list.append(img_url)

            # 이미지 다운로드 (폴더: item_img, 파일명: 상품코드_idx.jpg)
            file_name = f"{g_no}_{idx+1}.jpg"
            download_image(img_url, "item_img", file_name)

        # 이미지 src가 20개 미만이면 빈 칸 패딩
        while len(img_src_list) < 20:
            img_src_list.append("")


        # === 엑셀 row에 img_src_list를 순서대로 삽입 ===
        # 예시: 기존 rows.append 딕셔너리에 추가
        # 예: "이미지1"~"이미지20" 열에 매핑
        img_columns = {f"이미지{n+1}": img_src_list[n] for n in range(20)}

        # [상세스펙(UL) HTML 추출 + 상세스펙 이미지 다운로드]
        product_tab_02 = soup_detail.find(id="product_tab_02")
        ul_spec_html = ""
        spec_img_filenames = []

        if product_tab_02:
            center_tag = product_tab_02.find("center")
            if center_tag:
                ul_tag = center_tag.find("ul")
                if ul_tag:
                    ul_spec_html = ul_tag.decode_contents()  # ul 내부 HTML

                # --- 상세스펙 center 안 img 태그 전부 찾기 ---
                img_tags = center_tag.find_all("img")
                for idx_img, img_tag in enumerate(img_tags):
                    src = img_tag.get("src")
                    if not src:
                        continue
                    # 절대경로로 변환
                    if src.startswith("/"):
                        img_url = "https://www.lklab.com" + src
                    else:
                        img_url = src
                    # 파일명 규칙: 상품코드_dt_1.jpg, 상품코드_dt_2.jpg, ...
                    file_name = f"{g_no}_dt_{idx_img + 1}.jpg"
                    download_image(img_url, "item_dt_img", file_name)
                    spec_img_filenames.append(file_name)

        # 10개 미만이면 빈 칸 패딩
        while len(spec_img_filenames) < 10:
            spec_img_filenames.append("")
        spec_img_columns = {f"상세이미지{n + 1}": spec_img_filenames[n] for n in range(10)}

        # item_codes와 item_info(4개씩) 1:v1 매핑
        for idx, item_code in enumerate(item_codes):
            info_group = item_info[idx*4 : (idx+1)*4]
            # 만약 info_group 길이가 4 미만이면 빈칸으로 패딩 (데이터 불일치 방지)
            if len(info_group) < 4:
                info_group += [''] * (4 - len(info_group))

            value = info_group[3]
            for s in ["소비자가 :", ",", "원"]:
                if s in value:
                    value = value.replace(s, "")
            value = value.strip()  # 앞뒤 공백까지 완전히 제거
            if idx == 0:
                row = {
                    "상품 코드": g_no,
                    "상품명(한글)": name_kor,
                    "상품명(영문)": name_eng,
                    "주요 특징": it_keyword,
                    "상품 상세": ul_spec_html,
                    **img_columns,
                    **spec_img_columns,
                    "품목 코드": item_code,
                    "Model": info_group[0].strip(),
                    "Description": info_group[1].strip(),
                    "Unit": info_group[2].strip(),
                    "Price(VAT별도)": value
                }
            else:
                row = {
                    "상품 코드": "",
                    "상품명(한글)": "",
                    "상품명(영문)": "",
                    "주요 특징": "",
                    "상품 상세": "",
                    "품목 코드": item_code,
                    "Model": info_group[0],
                    "Description": info_group[1],
                    "Unit": info_group[2],
                    "Price(VAT별도)": value
                }

            # row = {
            #     "상품 코드": g_no if idx == 0 else "",
            #     "상품명(한글)": name_kor if idx == 0 else "",
            #     "상품명(영문)": name_eng if idx == 0 else "",
            #     "주요 특징": it_keyword if idx == 0 else "",
            #     "품목 코드": item_code,
            #     **img_columns,
            #     "Model": info_group[0],
            #     "Description": info_group[1],
            #     "Unit": info_group[2],
            #     "Price(VAT별도)": value
            # }
            # row.update(img_columns)  # 이미지 열 추가
            rows.append(row)

    except Exception as e:
        print(f"  ⚠️ 예외 발생: {e}")
        continue

# 결과 저장
df = pd.DataFrame(rows)
df.to_excel("lklab_product_option_info2.xlsx", index=False)
print("✅ 세로형 엑셀 저장 완료.")
