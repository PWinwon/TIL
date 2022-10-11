### 1. 모든 레코드 조회하기

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/59034?language=mysql)

```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID
```



### 2. 역순 정렬하기

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/59035?language=mysql)

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;
```



### 3. 아픈 동물 찾기

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/59036?language=mysql)

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick';
```



### 4. 어린 동물 찾기

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/59037?language=mysql)

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != "Aged" ORDER BY ANIMAL_ID;
```


