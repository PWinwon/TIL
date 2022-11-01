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



### 5. 동물의 아이디와 이름

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/59403?language=mysql)

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```



### 6. 과일로 만든 아이스크림 고르기

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/133025?language=mysql)

```sql
SELECT a.FLAVOR 
FROM FIRST_HALF a 
LEFT JOIN ICECREAM_INFO b
ON a.FLAVOR=b.FLAVOR
WHERE a.TOTAL_ORDER > 3000 AND b.INGREDIENT_TYPE = 'fruit_based'
ORDER BY a.TOTAL_ORDER DESC;
```

