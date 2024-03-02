# Python Data Type
## 숫자형
| 항목 | 파이썬 사용 예 |
|:---:|:---:|
|정수|123, -234, 0|
|실수|123.45, -123.43, 2.5e10|
|8진수|0o34, 0o25|
|16진수|0x2A, 0xFF|
<br>

#### 숫자형을 활용하기 위한 연산자
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

#### 문자열 자료형
| 문자열 생성 방법 | 예시 |
|:---:|:---:|
|큰따옴표(")|"Hello World"|
|작은따옴표(')|'Hello World'|
|큰따옴표 3개 연속(""")|"""Hello World"""|
|작은따옴표 3개 연속('''')|'''Hello World'''|
<br>

#### 문자열 연산하기
| 연산자 | 의미 |
|:---:|:---:|
|+|더하기|
|*|곱하기|
|len()|문자열 길이 구하기|
|문자열[시작 번호 인덱스:끝 번호 인덱스](끝번호는 미포함)|문자열 슬라이싱|
<br>
* 문자열의 요솟값은 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다.
<br>

## 문자열 포매팅
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

3. 문자열 정렬
```python
>>> f'{"hi":<10}'  # 왼쪽 정렬
결과 : 'hi        '
>>> f'{"hi":>10}'  # 오른쪽 정렬
결과 : '        hi'
>>> f'{"hi":^10}'  # 가운데 정렬
결과 : '    hi    '
```
<br>

4. 문자열 공백 채우기
```python
>>> f'{"hi":=^10}'  # 가운데 정렬하고 = 문자로 공백 채우기
결과 : '====hi===='
>>> f'{"hi":!<10}'  # 왼쪽 정렬하고 ! 문자로 공백 채우기
결과 : 'hi!!!!!!!!'
```
<br>

5. 문자열 소수점 표현
```python
>>> y = 3.42134233
>>> f'{y:0.4f}'  # 소수점 4자리까지만 표현
결과 : '3.4213'
>>> f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자릿수를 10으로 맞춤
결과 : '    3.4213'
```
<br>
<br>
<br>

## 문자열 관련 함수
1. count
```python
>>> a = "hobby"
>>> a.count('b')  # 문자열 중 문자 b의 개수를 돌려준다.
결과 : 2
```
<br>

2. find
```python
>>> a = "Python is the best choice"
>>> a.find('b')
결과 : 14 # 문자열에서 b가 처음 나온 위치
>>> a.find('k')
결과 : -1 # 문자열이 존재하지 않으면 -1을 반환한다.
```
<br>

3. index
```python
>>> a = "Life is too short"
>>> a.index('t')
결과 : 8 # 문자열에서 b가 처음 나온 위치
>>> a.find('k')
결과 :   # k가 없기 때문에 오류 발생 
      ''' 
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: substring not found
      '''
```
<br>

4. join
```python
>>> ",".join('abcd')
결과 : 'a,b,c,d' #문자열 abcd 각각의 문자 사이에 ','를 삽입
```
<br>

5. upper
```python
>>> a = "hi"
>>> a.upper()
결과 : 'HI' # 소문자를 대문자로 변환
```
<br>

6. lower
```python
>>> a = "HI"
>>> a.lower()
결과 : 'hi' # 대문자를 소문자로 변환
```
<br>

7. lstrip, rstrip, strip
```python
>>> a = " hi "
>>> a.lstrip()
결과 : 'hi ' # 왼쪽 공백 제거

>>> a = " hi "
>>> a.rstrip()
결과 : ' hi' # 오른쪽 공백 제거

>>> a = " hi "
>>> a.strip()
결과 : 'hi' # 양쪽 공백 제거
```
<br>

8. replace
```python
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
결과 : 'Your leg is too short' # 문자열 안의 특정한 값을 다른 값으로 치환
```
<br>

9. split
```python
>>> a = "Life is too short"
>>> a.split() # 공백을 기준으로 문자열 나눔
결과 : ['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':') # : 기호를 기준으로 문자열 나눔
결과 : ['a', 'b', 'c', 'd']
```
<br>
<br>
<br>

## 리스트 자료형
* 리스트를 만뜰 때는 대괄호([])로 감싸 주고 각 요솟값은 쉽표(,)로 구분해 준다.
```
  리스트명 = [요소1, 요소2, 요소3, ...]
```
### 예제
```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = ['Life', 'is', 'too', 'short']
>>> d = [1, 2, 'Life', 'is']
>>> e = [1, 2, ['Life', 'is']]
```
<br>
<br>
<br>

#### 리스트의 인덱싱과 슬라이싱
* 문자열과 비슷하므로 생략한다
<br>
<br>
<br>

#### 리스트 연산하기
```python
# 리스트 더하기 ( + )
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a + b
결과 : [1, 2, 3, 4, 5, 6]

# 리스트 반복하기 ( * )
>>> a = [1, 2, 3]
>>> a * 3
결과 : [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
>>> a = [1, 2, 3]
>>> len(a)
결과 : 3
```
<br>
<br>
<br>

#### 리스트 수정과 삭제
```python
# 값 수정하기
>>> a = [1, 2, 3]
>>> a[2] = 4
>>> a
결과 : [1, 2, 4] # a[2]의 요솟값3이 4로 변경되었다.

# del 함수로 요소 삭제하기
>>> a = [1, 2, 3]
>>> del a[1]
결과 : [1, 3]

# 슬라이싱 기법을 사용하여 요소 여러 개를 한번에 삭제 가능
>>> a = [1, 2, 3, 4, 5]
>>> del a[2:]
>>> a
결과 : [1, 2]
```
<br>
<br>
<br>

## 리스트 관련 함수
1. append
```python
>>> a = [1, 2, 3]
>>> a.append(4)  # 리스트의 맨 마지막에 4를 추가
>>> a
결과 : [1, 2, 3, 4]

# 리스트에 리스트를 추가
>>> a.append([5, 6])  # 리스트의 맨 마지막에 4를 추가
>>> a
결과 : [1, 2, 3, 4, 5, 6]
```
<br>

2. sort
```python
>>> a = [1, 4, 3, 2]
>>> a.sort()  # 요소를 순서대로 정렬
>>> a
결과 : [1, 2, 3, 4]

>>> a = ['a', 'c', 'b']
>>> a.sort()  # 문자열 역시 요소를 순서대로 정렬
>>> a
결과 : ['a', 'b', 'c']
```
<br>

3. reverse
```python
>>> a = ['a', 'c', 'b']
>>> a.reverse()  # 문자열 역시 요소를 순서대로 정렬
>>> a
결과 : ['b', 'c', 'a']
```
<br>

4. index
```python
>>> a = [1, 2, 3]
>>> a.index(3)  # 인덱스를 반환한다.
>>> a
결과 : 1

결과 :   # 존재하지 않으면 오류(ValueError)가 발생
      ''' 
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: substring not found
      '''
```
<br>

5. insert
```python
>>> a = [1, 2, 3]
>>> a.insert(0, 4)  # a[0] 위치에 4 삽입
>>> a
결과 : [4, 1, 2, 3]
```
<br>

6. remove
```python
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)  # 첫번째로 나오는 요솟값을 삭제
>>> a
결과 : [1, 2, 1, 2, 3]
```
<br>

7. pop
```python
>>> a = [1, 2, 3]
>>> a.pop()  # 맨 마지막 요소를 돌려주고 그 요소는 삭제
결과 : 3
>>> a
결과 : [1, 2]
# pop(x) 리스트의 x(인덱스)번째 요소를 돌려주고 삭제
```
<br>

8. count
```python
>>> a = [1, 2, 3, 1]
>>> a.count(1)  # 리스트 안에 몇 개 있는지 개수를 돌려준다
결과 : 2
```
<br>

8. extend
```python
# extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더한다.
>>> a = [1, 2, 3]
>>> a.extend([4, 5])  # 리스트 안에 몇 개 있는지 개수를 돌려준다
>>> a
결과 : [1, 2, 3, 4, 5]
>>> b = [6, 7]
>>> a.extend(b)
>>> a
결과 : [1, 2, 3, 4, 5, 6, 7]
```
<br>

## 튜플 자료형
* 리스트는 []으로 둘러싸지만 튜플은()으로 둘러싼다.
* 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
### 예제
```python
# 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
>>> t1 = ()
>>> t2 = (1,)
>>> t3 = (1, 2, 3)
>>> t4 = 1, 2, 3
>>> t5 = ('a', 'b', ('ab', cd))
```
* 인덱싱, 슬라이싱, +, *, len()는 값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일하다.(리스트 참고)

## 딕셔너리 자료형
* 연관 배열 = 해시 = 딕셔너리
* Key와 Value의 쌍 여러 개가 {}로 둘러싸여 있다.
### 예제
```python
# 생성 방법
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
>>> dic = {'name':'pey', 'phone':'01011111111', 'birth':'1230'}
```
<br>
<br>
<br>

### 딕셔너리 관련 함수
1. keys, values, items, clear, get
```python
# keys()
>>> a = {'name':'pey', 'phone':'01011111111', 'birth':'1230'}
>>> a.keys()
>>> a
결과 : dict_keys(['name', 'phone', 'birth'])
# a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다.
# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
>>> list(a.keys)
결과 : ['name', 'phone', 'birth']

# values()
>>> a.values()
결과 : dict_values(['pey', '01011111111', '1230'])

# items()
>>> a.items()
결과 : dict_items([('name','pey'), ('phone','01011111111'), ('birth','1230')])
# key와 value를 튜플로 묶은 값을 dict_items 객체로 돌려준다.

# clear()
>>> a.clear()
>>> a
결과 : {}
# 딕셔너리 안의 모든 요소를 삭제

# get()
>>> a.get('name')
결과 : 'pey'
>>> a.get('phone')
결과 : '01011111111'
# 키값이 없을 경우에는 오류를 발생시키지 않고 None을 돌려준다.
```
<br>

2. 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
```python
>>> a = {'name':'pey', 'phone':'01011111111', 'birth':'1230'}
>>> 'name' in a
결과 : True
>>> 'email' in a
결과 : False
```
<br>
<br>
<br>

## 집합 자료형
* 집함(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.
* 중복을 허용하지 안흔ㄴ다.
* 순서가 없다.(Unordered)
### 예제
```python
# set 키워드를 사용해 만들 수 있다.
>>> s1 = set([1,2,3])
>>> s1
결과 : {1, 2, 3}

# 문자열을 입력하여 만들 수도 있다.
>>> s2 = set("Hello")
>>> s2
결과 : {'e', 'H', 'l', 'o'}
```

### 교집합(&), 합집합(|), 차집합(-) 구하기
```python
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
>>> s1 & s2
결과 : {4, 5, 6}
>>> s1.intersection(s2)
결과 : {4, 5, 6}

# 합집합
>>> s1 | s2
결과 : {1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1.union(s2)
결과 : {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
>>> s1 - s2
결과 : {1, 2, 3}
>>> s1.difference(s2)
결과 : {1, 2, 3}

# 교집합
>>> s1 & s2
결과 : {4, 5, 6}
```
<br>

### 집합 자료형 관련 함수
1. add
```python
# 1개의 값만 추가할 경우에 사용
# 이미 만들어진 set자료형에 값을 추가할 수 있다.
>>> s1 = set([1,2,3])
>>> s1.add(4)
>>> s1
결과 : {1, 2, 3, 4}
```
<br>

2. update
```python
# 여러개의 값을 추가할 경우에 사용
>>> s1 = set([1,2,3])
>>> s1.update([4, 5, 6])
>>> s1
결과 : {1, 2, 3, 4, 5, 6}
```
<br>

3. remove
```python
# 특정 값을 제거하고 싶을 때 사용
>>> s1 = set([1,2,3])
>>> s1.remove(2)
>>> s1
결과 : {1, 3}
```
<br>
<br>

## 불 자료형
* 불(bool)자료형이란 참(true)과 거짓(false)을 나타내는 자료형이다.
### 자료형의 참과 거짓
|자료형|값|참 or 거짓| 
|:---:|:---:|:---:|
|문자열|"python"|참|
||""|거짓|
|리스트|"[1, 2, 3]"|참|
||[]|거짓|
|튜플|()|거짓|
|딕셔너리|{}|거짓|
|숫자형|0이 아닌 숫자|참|
||0|거짓|
||None|거짓|