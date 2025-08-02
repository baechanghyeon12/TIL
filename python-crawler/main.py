import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse
import time
import random

# --------- 설정값 ---------
# BASE_URL = "https://example.com/products?page={}"
BASE_URL = "https://www.lklab.com/product/product_list.asp?t_no=801"
START_PAGE = 1
END_PAGE = 1           # 실제 마지막 페이지까지로 설정
IMAGE_DIR = "images"   # 이미지 저장 폴더
OUTPUT_XLSX = "products.xlsx"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# 상품 코드와 이미지 정보를 저장할 리스트
result = []

# 이미지 저장 폴더 생성
os.makedirs(IMAGE_DIR, exist_ok=True)

def get_soup(url):
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "lxml")

def download_image(img_url, save_dir):
    """이미지를 지정 폴더에 저장, 파일명 자동생성"""
    os.makedirs(save_dir, exist_ok=True)
    fname = os.path.basename(urlparse(img_url).path)
    local_path = os.path.join(save_dir, fname)
    # 중복 파일 방지: 파일명에 번호 붙이기
    count = 1
    orig_local_path = local_path
    while os.path.exists(local_path):
        name, ext = os.path.splitext(orig_local_path)
        local_path = f"{name}_{count}{ext}"
        count += 1
    r = requests.get(img_url, headers=HEADERS, stream=True)
    with open(local_path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    img_delay = random.uniform(0.2, 1.0)
    time.sleep(img_delay)
    return local_path

for page in range(START_PAGE, END_PAGE + 1):
    print(f"크롤링: {page}페이지")
    url = BASE_URL.format(page)
    soup = get_soup(url)
    # ------ 아래 셀렉터는 실제 사이트 구조에 맞게 수정 필요 ------
    products = soup.select(".product-item")  # 예시: 상품 박스 클래스
    if not products:
        print(f"{page}페이지 상품 없음. 종료.")
        break
    for item in products:
        code = item.select_one(".product-code").text.strip()      # 예시: 상품코드 위치
        img_tag = item.select_one("img")
        img_url = urljoin(url, img_tag["src"]) if img_tag else ""
        img_local = download_image(img_url, IMAGE_DIR) if img_url else ""
        result.append({
            "상품코드": code,
            "이미지URL": img_url,
            "로컬이미지경로": img_local,
        })
    delay = random.uniform(1, 4)
    print(f"{delay:.2f}초 대기 후 다음 페이지 진행")
    time.sleep(delay)

# 엑셀 저장
df = pd.DataFrame(result)
df.to_excel(OUTPUT_XLSX, index=False)
print(f"\n총 {len(result)}개 상품 엑셀 및 이미지 저장 완료")
