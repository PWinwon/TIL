# Python 기초

### 1. 저장

----

##### 1.1 저장이란?

```python
dust = 60
#dust는 60이다(X)
#dust에 60을 저장(할당)한다(O)

dust == 60
#dust에 저장된 값은 60과 같다
```



#####  1.2 무엇을 저장할 수 있을까?   

######  1.2.1 숫자

```python
#현실세계에 존재하는 모든 숫자 
#기본적인 연산 가능
a = 12
b = -365
c = 3.141592
d = 23ab    #(x)
e = ba123   #(x)
```



###### 1.2.2 글자   

```python
#현실세계에 존재하는 모든 글자
#따옴표로 둘러싼 글자 혹은 숫자
a = '미세먼지'
b = '58도 글자입니다'
c = '글자는 반드시 따옴표를 붙여야 합니다!' 
```



 ###### 1.2.3 참/거짓   

```python
#True 혹은 False   
#주로 조건 및 반복에 사용됨
 300 > 20  => True
 150 == 161 => False
```



##### 1.3 어떻게 저장할 수 있을까?  

 ###### 1.3.1 변수(Variable)  

```python
#저장된 값을 변경할 수 있는 박스
#숫자, 글자, 참거짓을 담을 수 있다
a = 3
dust = 58
pi = 3.141592
print(dust)   # 60
print('dust') # 'dust'
```



 ###### 1.3.2 리스트(List)   

```python
#박스의 목록
#여러 개의 박스가 순서대로 붙어있다
dust = [58, 40, 70]
print(dust[1])    # 40
```



###### 1.3.3 딕셔너리(Dictionary)   

```python
#견출지를 붙인 박스들의 묶음
dust = {'영등포구': 58, '강남구': 40}
print(dust[0])         #(x) 키 값으로 호출해야함
print(dust['영등포구'])   #58
```



### 2. 조건 

```python
#특정 조건일 때 코드를 실행할 수 있다
 if 조건식1:
        코드1
 elif 조건식2:
    	코드2
 else:
    	코드3
        
x = 85
if(x >= 80):
    print("성적은 A")
elif(x >= 70):
    print("성적은 B")
elif(x >= 60):
    print("성적은 C")
else:
    print("성적은 F")

```



### 3.반복

##### 3.1 while

```python
#while에 해당하는 조건일 동안 계속 반복한다.
#조건식을 만족하면 계속 반복하고, 만족하지 않으면 반복을 끝낸다. 
#종료 조건이 반드시 필요하다. 
n = 0 
while n < 3:
     print('출력')
     n = n+1
# '출력'
# '출력'
# '출력'
```



##### 3.2 for   

```python
#정해진 박스 내에서의 반복 시 사용한다.
#가지고 있는 모든 것을 꺼낸다'
#종료 조건이 필요없다.
dust = [59, 24, 102]
for i in dust:
    print(i)   
# 59
# 24
# 102
```

