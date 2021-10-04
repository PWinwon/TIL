```sql
CREATE TABLE {테이블명} (
	id INTEGER PRIMARY KEY AUTOINCREMENT, # id는 선택사항
    {필드명} {필드타입} {NOT NULL},
    ...
);

ALTER TABLE {테이블명} RENAME TO {새로운테이블이름};

ALTER TABLE {테이블명} RENAME COLUMN {기존컬럼이름} TO {새로운컬럼이름};

ALTER TABLE {테이블명} ADD COLUMN {새로운컬럼이름} {데이터타입설정} {NOT NULL DEFAULT {기본값}};
															# 선택사항

DROP TABLE {테이블명};

INSERT INTO {테이블명} (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...), (값1, 값2, ...);

SELECT (DISTINCT) 컬럼1, 컬럼2, ... FROM {테이블명} WHERE 조건 LIMIT 숫자 OFFSET 숫자;

SELECT FUNC(컬럼) AS 지정컬럼명 FROM {테이블명};

SELECT 컬럼1, 컬럼2, ... FROM {테이블명} ORDER BY 컬럼, 컬럼, ... DESC LIMIT 숫자;

SELECT 컬럼1, FUNC(컬럼2) FROM {테이블명} GROUP BY 컬럼1, 컬럼2;

DELETE FROM {테이블명} WHERE 조건;

UPDATE {테이블명} SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
```



```python
{모델명}.objects.filter(조건).values('필드명')
```

