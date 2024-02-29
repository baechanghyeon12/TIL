# Git Command
### 변경사항 확인
```java
git status
```
### 스테이지에 올리기
```java
git add (파일명)
git add .       //변경된 모든 파일 add
```
### Commit
```java
git commit -m "(커밋 메세지)"
git commit -am "(커밋 메세지)"		//add + commit 동시에(한번은 commit 되어 있는 파일만 가능 => 즉, 처음엔 불가능)
```
### Commit로그
```java
git log
git log --oneline 					//커밋 내역을 한줄씩 보여줌.
git log --graph					    //커밋 내역을 시각화해서 보여줌.
git log --branches					//각 브랜치의 커밋내역을 보여줌.
git log main..test					//test브랜치에만 있는
```
### 수정내용 확인
```java
git diff							//커밋된 내용과 아직 커밋 하지 않은 파일의 현재 어디가 다른지
```
### 방금 커밋한 메세지 수정하기
```java
git commit --amend
```  


## Branch Command
### 브랜치 목록보기
```java
git branch
```
### 새 브랜치 만들기
```java
git branch (브랜치명)
```
### 브랜치로 이동
```java
git checkout (브랜치명)
```
### 새 브랜치 만들고 이동
```java
git checkout -b (브랜치명)
```
### 브랜치 병합
```java
git git checkout (브랜치명A)			//A로 이동(보통 main)
git merge (병합할 브랜치명B)		//A에 B를 병합branch
```
### 로컬저장소 브랜치 삭제
```java
git branch -d (브랜치명)
```
### 로컬 & 원격저장소 브랜치 삭제
```java
git push origin --delete (브랜치명)
```


## Reset&Revert
### 스테이징 되돌리기
```java
git reset HEAD (파일명)
```
### 최신 커밋 + 스테이징 되돌리기
```java
git reset HEAD^				//최근 커밋 취소되고, 스테이징도 함께 취소됨
git reset HEAD^3			//최근 3개의 커밋 취소
git reset --soft HEAD^		//최근 커밋만 취소됨.
git reset --mixed HEAD^		//최근 커밋 + 스테이징도 취소됨(default)
git reset --hard HEAD^		//최근 커밋 + 스테이징 취소되고 파일도 삭제됨(복구 못함)
```
### 특정 커밋으로 되돌리기
```java
git reset (커밋해시)			//해당 해시로 커밋되고, 스테이징도 함께 취소됨(변경 내용은 그대로)
git reset --hard (커밋해시)	//해당 해시로 커밋되고, 이 전 커밋내용은 모두 삭제됨

```
### 커밋 삭제하지 않고 되돌리기
```java
git revert (취소할 커밋해시)	//커밋내역이 그대로 남아서 돌아갈 수 있음
```  


## Stash
* 파일을 수정하다가 급하게 다른 파일을 커밋해야 하는 경우 사용
* **단, tracked 상태여야함. 즉 한번은 커밋한 상태**
```java
git stash
git stash list
git stash pop				//가장 최근(마지막)에 넣은 파일 먼저 나옴. 변경내역 있다고 뜸
```


## Remote
### 원격저장소 연걸
```java
git remote add origin (원격 주소)		//원격저장소(origin)를 추가하겠다고 깃에게 알려주는 것
```
### 원격저장소 연결확인
```java
git remote -v
```
### 맨 처음 원격 저장소에 파일 올리기
```java
git push -u origin main					//내 컴퓨터에 있는 내용을 원격 저장소에 처음에 한번 연결할 때
```
### 원격 저장소에 파일 올리기
```java
git push								//초기 연결이 끝나면 그냥 push하면 됨.
git push origin (브랜치명)				//원격저장소에 해당브랜치 푸쉬
```
### 원격 저장소에서 파일 내려받기
```java
git pull
```
### 원격저장소 연결 해제
```java
git remote remove origin
```