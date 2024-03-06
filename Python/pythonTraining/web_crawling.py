import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = ""
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select('img')
    n = 1
    for i in imgs:
        imgUrl = i['src']
        img_data = urlopen(imgUrl).read()  # 수정된 부분: urlopen을 사용하여 이미지 데이터 가져오기
        with open('./img/' + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
            h.write(img_data)  # 수정된 부분: 이미지 데이터를 파일에 쓰기
        n += 1
else:
    print(response.status_code)
