## if문
* 참과 거짓을 판단하는 문장이다.
* 조건문 다음에 콜론(:)을 꼭 붙여야 된다.
* 조건에 맞는 실행문은 언제나 같은 들여쓰기를 해야한다.
* 아무런 수행도 하고싶지 않으면 pass를 사용하면 된다.
### 예제
```python
if 조건문:
  수행할 문장1
  수행할 문장2
  수행할 문장3
elif 조건문N:
  수행할 문장N-A
  수행할 문장N-B
  수행할 문장N-C
else:
  수행할 문장A
  수행할 문장B
  수행할 문장C

# pass사용 예제
if 조건문:
  pass # pass를 실행하고 아무 결과값도 보여주지 안흔다.
else:
  수행할 문장A
```
### 비교 연산자
비교 연산자 | 설명
:---:|:---:
x < y | x가 y보다 작다.
x > y | x가 y보다 크다.
x == y | x와 y가 같다.
x != y | x와 y가 같지 않다..
x >= y | x가 y보다 크거나 같다.
x <= y | x가 y보다 작거나 같다.

<br>
<br>
<br>

### and, or, not
연산자 | 설명
:---:|:---:
x or y | x와 y 둘 중에 하나만 참이어도 참이다
x and y | x와 y 모두 참이어야 참이다
not x | x가 거짓이면 참이다

<br>
<br>
<br>

### x in s, x not in s
in(~안에 x가 있으면 true) | not in(~안에 x가 없으면 ture)
:---:|:---:
x in 리스트 | x not in 리스트
x in 튜플 | x not in 튜플
x in 문자열 | x not in 문자열

### 파이썬의 조건부 표현식
```python
if score >= 60:
  message = "success"
else:
  message = "failure"

# 위 코드를 다음과 같이 간단히 표현할 수 있다.
# 방법 : 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message = "success" if score >= 60 else "failure"
```
