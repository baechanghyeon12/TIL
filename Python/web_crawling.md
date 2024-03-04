## 웹 크롤링 준비하기
### 필요한 라이브러리 이해
Python 웹 크롤링에는 주로 requests, BeautifulSoup, Scrapy 등의 라이브러리를 사용합니다.

– **requests**: Python에서 HTTP 요청을 보내는 라이브러리로, 웹 페이지의 HTML 데이터를 가져오는데 사용됩니다.

– **BeautifulSoup**: HTML과 XML 파일에서 데이터를 추출하기 위한 Python 라이브러리로, 파싱을 쉽게 도와줍니다.

– **Scrapy**: 웹 사이트에서 데이터를 추출하는 등의 복잡한 웹 크롤링 작업을 위한 오픈 소스 프레임워크입니다.
* * *
## 개발환경 설정
Python과 필요한 라이브러리를 설치하고 환경을 설정하는 방법은 다음과 같습니다.

– Python 설치: Python 공식 홈페이지(https://www.python.org/)에서 맞는 버전을 선택해 설치합니다.

– 필요한 라이브러리 설치: pip라는 패키지 관리자를 이용해 requests와 BeautifulSoup를 설치합니다.

```
pip3 install requests beautifulsoup4
```
이렇게 함으로써 웹 크롤링을 위한 기본적인 환경 설정을 마칠 수 있습니다. 이제 Python 코드를 작성하여 웹 크롤링을 수행할 준비가 완료되었습니다.
* * *
### Python 웹 크롤링 기초
#### 간단한 웹 크롤링 예제
Python의 requests와 BeautifulSoup 라이브러리를 이용하면 간단하게 웹 크롤링을 수행할 수 있습니다. 아래 코드는 “https://www.python.org/”에서 Python의 내용을 크롤링하는 예제입니다.

```
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)  # 'Welcome to Python.org' 를 출력
```