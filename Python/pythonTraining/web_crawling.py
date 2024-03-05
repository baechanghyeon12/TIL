import requests
from bs4 import BeautifulSoup
import urllib.request

url = ""
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select('img')
    print(len(imgs))
    index = 0
    for img in imgs:
          # 이미지 데이터를 가져옴
        index += 1
        urllib.request.urlretrieve(img["src"],'fbk'+str(index)+'jpg')
        # img_data = requests.get(img["src"]).content
        # # 이미지를 파일로 저장 (파일명은 이미지 URL에서 추출하거나, 원하는 대로 지정)
        # with open('downloaded_image_{index}.jpg', 'wb') as img_file:
        #     img_file.write(img_data)
else : 
    print(response.status_code)

    