import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# ✅ 크롤링할 URL
url = "https://www.lklab.com/"  # 여기에 실제 URL을 넣으세요

# ✅ 요청 및 파싱
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# ✅ a 태그 중 t_no 파라미터가 있는 것들 찾기
pattern = re.compile(r"/product/product_list\.asp\?t_no=(\d+)")

t_no_list = []

for a_tag in soup.find_all("a", href=True):
    match = pattern.search(a_tag["href"])
    if match:
        t_no_list.append(int(match.group(1)))  # 숫자만 추출

# ✅ 중복 제거 및 정렬 (선택 사항)
t_no_list = sorted(set(t_no_list))

# ✅ 엑셀로 저장
df = pd.DataFrame(t_no_list, columns=["t_no"])
df.to_excel("t_no_list.xlsx", index=False)

print("엑셀 파일 저장 완료!")
