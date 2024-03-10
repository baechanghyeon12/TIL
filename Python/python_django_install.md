**Python3 설치**
* 설치 여부 확인하기
```
$ python3 --version
Python 3.12.2
```
* 만약 설치되어있지 않다면 설치
```
$ brew install python3
```

### 가상환경 구축
* Python에서는 프로젝트별로 독립된 가상환경을 만들어주는 virtualenv 툴을 제공함
* 인터넷에서 다운로드한 파이썬 라이브러리들이 충돌을 일으키는 것을 방지하기 위해 독립된 가상환경이 필요함
* 외부 라이브러리들은 서로 의존성을 가지는 경우가 많아 버전이 맞지 않는 경우 오작동 발생
<br>

### 1. Django 프로젝트 디렉토리 생성
```
$ mkdir start-django
start-django $ cd start-django
```
### 2. 가상환경 생성
```
start-django $ python3 -m venv venvproj01
start-django $ cd venvproj01
```
### 3. 가상환경 활성화
```
venvproj01 $ source bin/activate
```
### 4. 가상환경 종료
```
venvproj01 $ deactivate
```
### **Django 설치**
```
venvproj01 $ cd ..
start-django $ pip3 install django
```
* 설치 확인
```
$ python3 -m django --version
4.1.7
```

### Django 프로젝트 생성하기
* 프로젝트 생성
```
$ django-admin startproject proj01
$ cd proj01
```
* 서버 구동
```
$ python3 manage.py runserver
```
* 서버 포트나 IP 변경 시에는 서버 구동 시에 파라미터로 전달
```
$ python3 manage.py runserver 8000
$ python3 manage.py runserver 0.0.0.0:8000
```