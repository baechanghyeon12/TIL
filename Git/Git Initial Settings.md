# Git 초기 설정
> it을 설치하고 나면 Git의 사용 환경을 적절하게 설정해 주어야 한다.
> **환경 설정은 한 컴퓨터에서 한 번만 하면 된다.**
> 설정한 내용은 Git을 업그레이드해도 유지된다.
* * *
### 1.사용자정보 설정
> Git을 설치하고 나서 가장 먼저 해야 하는 것은 사용자이름과 이메일 주소를 설정하는 것이다. Git은 커밋할 때마다 이 정보를 사용한다. 한 번 커밋한 후에는 정보를 변경할 수 없다
> 다시 말하자면 --global 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다.
> 만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 --global 옵션을 빼고 명령을 실행한다.
```
  $ git config --global user.name "John Doe"
  $ git config --global user.email johndoe@example.com
```
* * *
### 2.설정 확인
> git config --list 명령을 실행하면 설정한 모든 것을 보여주어 바로 확인할 수 있다.
> Git은 같은 키를 여러 파일(/etc/gitconfig 와 ~/.gitconfig 같은)에서 읽기 때문에 같은 키가 여러 개 있을 수도 있다. 그러면 Git은 나중 값을 사용한다.
```
  $ git config --list
  user.name=John Doe
  user.email=johndoe@example.com
  color.status=auto
  color.branch=auto
  color.interactive=auto
  color.diff=auto
  ...
```
> * git config <key> 명령으로 Git이 특정 Key에 대해 어떤 값을 사용하는지 확인할 수 있다.
> '''
>   $ git config user.name
>   John Doe
> '''