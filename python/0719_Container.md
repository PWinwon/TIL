# 컨테이너(Container)

- 여러 개의 값을 저장할 수 있는 것(객체)

### 시퀀스(sequence)형 

- 순서가 있는(ordered) 데이터 (★★★index로 접근 가능하다!★★★)
- 순서가 있다 != 정렬되어 있다
- 리스트(list), 튜플(tuple), 레인지(range), 문자형(string), 바이너리(binary)

##### 리스트(list)

- 리스트는 순서가 있는 시퀀스로 인덱스를 통해 접근
- 인덱스는 0부터 시작

![image-20210719222516465](0719_Container.assets/image-20210719222516465.png)

```python
[1, 2, 3]				# [1, 2, 3]
list((1, 2, 3))			# [1, 2, 3]
print(type([1, 2, 3]))	# <class 'list'>

# 값 접근
a = [1, 2, 3]
print(a[0])				# 1

# 값 변경
a[0] = '1'
print(a)				# ['1', 2, 3]  << 서로 다른 타입의 데이터를 저장할 수 있음

#중첩 리스트
a = [[1, 2], [3, 5]]
a[0][1]					# 2
```

##### 튜플(tuple)

- 튜플은 수정 불가능한(immutable) 시퀀스로 인덱스로 접근

```python
(1, 2, 3, 1)				# (1, 2, 3, 1)
tuple((1, 2, 3, 1))			# (1, 2, 3, 1)
print(type((1, 2, 3, 1)))	# <class 'tuple'>

# 값 접근
a = (1, 2, 3, 1)
print(a[1])				# 2

# 값 변경 >> 불가능
a[1] = '3'				# 에러발생

x, y = (1, 2)			# 실제로 tuple로 처리
print(x, y)				# 1 2

print(type(divmod(5,2)))# <class 'tuple'>
```

- 하나의 항목으로 구성된 튜플은 생성시 값 뒤에 쉼표를 붙여야 함

```python
a = (1)
print(type(a))			# <class 'int'>
b = (1, )
print(type(b))			# <class 'tuple'>
```

##### 레인지(range)

- range는 숫자의 시퀀스를 나타내기 위해 사용
  - 기본형 : range(n) 	>> 	0 ~ n-1
  - 범위지정 : range(n,m)    >>    n ~ m-1
  - 범위 및 스텝 지정 : range(n, m, s)     >>    n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

```python
list(range(4))			# [0, 1, 2, 3]
print(type(range(4)))	# <class 'range'>

list(range(3))			# [0, 1, 2]
list(range(1,5))		# [1, 2, 3, 4]
list(range(1,5,2))		# [1, 3]

list(range(6, 1, -1))	# [6, 5, 4, 3, 2]
list(range(1, 3, -1))	# []
list(range(6, 1, 1))	# []
```

### 시퀀스에서 활용하는 연산자 / 함수

##### containment test

- 시퀀스 포함 여부 확인 ( in , not in)

```python
```

















































































































































