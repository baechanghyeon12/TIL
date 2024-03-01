# Python Data Type
### 숫자형
| 항목 | 파이썬 사용 예 |
|:---:|:---:|
|정수|123, -234, 0|
|실수|123.45, -123.43, 2.5e10|
|8진수|0o34, 0o25|
|16진수|0x2A, 0xFF|
<br>

### 숫자형을 활용하기 위한 연산자
| 연산자 | 의미 |
|:---:|:---:|
|+|더하기|
|-|빼기|
|*|곱하기|
|/|나누기|
|**|제곱|
|%|나눗셈 후 나머지를 반환|
|//|나눗셈 후 몫을 반환|
<br>

### 문자열 자료형
| 문자열 생성 방법 | 예시 |
|:---:|:---:|
|큰따옴표(")|"Hello World"|
|작은따옴표(')|'Hello World'|
|큰따옴표 3개 연속(""")|"""Hello World"""|
|작은따옴표 3개 연속('''')|'''Hello World'''|
<br>

### 문자열 연산하기
| 연산자 | 의미 |
|:---:|:---:|
|+|더하기|
|*|곱하기|
|len()|문자열 길이 구하기|
|문자열[시작 번호 인덱스:끝 번호 인덱스](끝번호는 미포함)|문자열 슬라이싱|
<br>
* 문자열의 요솟값은 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다.
<br>

### 문자열 포매팅
#### 문자열 포맷 코드
| 코드 | 설명 |
|:---:|:---:|
|%s|문자열(String)|
|%c|문자 1개(Character)|
|%d|정수(Integer)|
|%f|부동 소수(Flating-point)|
|%o|8진수|
|%x|16진수|
|%%|Literal %(문자 '%' 자체)|
<br>

1. 숫자 바로 대입
```python
>>> "I eat %d apples." % 3
결과 : "I eat 3 apples."
```
<br>

2. 문자열 바로 대입
```python
>>> "I eat %s apples." % "five"
결과 : "I eat five apples."
```
<br>

3. 숫자 값을 나타내는 변수로 대입
```python
>>> number = 3
>>> "I eat %d apples." % number
결과 : "I eat 3 apples."
```
<br>

4. 2개 이상의 값 넣기
```python
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
결과 : "I ate 3 apples. so I was sick for three days."
```
<br>

#### format 함수를 사용한 포맷팅
1. 숫자 바로 대입
```python
>>> "I eat {0} apples.".format(3)
결과 : "I eat 3 apples."
```
<br>

2. 문자열 바로 대입
```python
>>> "I eat {0} apples.".format("five")
결과 : "I eat five apples."
```
<br>

3. 숫자 값을 나타내는 변수로 대입
```python
>>> number = 3
>>> "I eat {0} apples.".format(number)
결과 : "I eat 3 apples."
```
<br>

4. 2개 이상의 값 넣기
```python
>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
결과 : "I ate 3 apples. so I was sick for three days."
```
<br>

5. 이름으로 넣기
```python
>>> "I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)
결과 : "I ate 10 apples. so I was sick for 3 days."
```
<br>

6. 인덱스와 이름을 혼용해서 넣기
```python
>>> "I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)
결과 : "I ate 10 apples. so I was sick for 3 days."
```
<br>
<br>

#### f 문자열 포매팅
* 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다.
* 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.
<br>
<br>
<br>

```python
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
결과 : '나의 이름은 홍길동입니다. 나이는 30입니다.'
```
<br>
* f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능하다.

2. 문자열 바로 대입
```python
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.'
결과 : '나의 이름은 홍길동입니다. 나이는 31입니다.'
```
<br>