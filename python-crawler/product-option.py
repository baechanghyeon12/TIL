# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
#
# # 크롤링할 상품 코드 리스트
# g_no_list = [11548, 11549, 8754]  # 예시 상품 코드
# base_iframe_url = "https://www.lklab.com/product/product_info_order_job.asp?g_no="
#
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
#
# rows = []
#
# for g_no in g_no_list:
#     iframe_url = f"{base_iframe_url}{g_no}"
#     print(f"[INFO] 상품 {g_no} 처리 중...")
#
#     try:
#         response = requests.get(iframe_url, headers=headers, timeout=15)
#         if response.status_code != 200:
#             print(f"  ❌ HTTP 오류: {response.status_code}")
#             continue
#
#         soup = BeautifulSoup(response.text, "html.parser")
#         item_codes = [td.get_text(strip=True) for td in soup.find_all("td", class_="pr22")]
#
#         if not item_codes:
#             print("  ⚠️ 품목코드 없음")
#
#         # ✅ 첫 번째 품목은 g_no 포함, 이후는 빈 문자열로 표시
#         for idx, item_code in enumerate(item_codes):
#             rows.append({
#                 "g_no": g_no if idx == 0 else "",
#                 "item_code": item_code
#             })
#
#         time.sleep(0.5)
#
#     except Exception as e:
#         print(f"  ⚠️ 예외 발생: {e}")
#         continue
#
# # DataFrame 생성 및 엑셀 저장
# df = pd.DataFrame(rows)
# df.to_excel("lklab_item_codes_vertical_grouped.xlsx", index=False)
#
# print("✅ 그룹화된 세로 저장 완료 및 엑셀 저장됨.")
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 👉 엑셀에서 상품코드 리스트 불러오기
df_input = pd.read_excel("lklab_total_product_code.xlsx")  # 파일명만 바꾸세요
g_no_list = df_input.iloc[:, 0].dropna().astype(int).tolist()

# 👉 세션 + 재시도 설정
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36"
}

base_iframe_url = "https://www.lklab.com/product/product_info_order_job.asp?g_no="
rows = []
cnt = 0
for g_no in g_no_list:
    cnt += 1
    iframe_url = f"{base_iframe_url}{g_no}"
    print(f"[INFO] {cnt}번째 상품 {g_no} 처리 중...")

    try:
        response = session.get(iframe_url, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"  ❌ HTTP 오류: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        item_codes = [td.get_text(strip=True) for td in soup.find_all("td", class_="pr22")]

        if not item_codes:
            print("  ⚠️ 품목코드 없음")

        # g_no는 첫 행에만
        for idx, item_code in enumerate(item_codes):
            rows.append({
                "g_no": g_no if idx == 0 else "",
                "item_code": item_code
            })

        # time.sleep(random.uniform(1.5, 3.0))  # 랜덤 지연

    except Exception as e:
        print(f"  ⚠️ 예외 발생: {e}")
        continue

# 결과 저장
df = pd.DataFrame(rows)
df.to_excel("lklab_product_option.xlsx", index=False)
print("✅ 세로형 엑셀 저장 완료.")
