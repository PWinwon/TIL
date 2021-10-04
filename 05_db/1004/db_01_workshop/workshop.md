1) 

```sql
CREATE TABLE countries(
  room_num TEXT,
  check_in TEXT,
  check_out TEXT,
  grade TEXT,
  price INTEGER
);
```

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT,
```



2. 

```sql
INSERT INTO countries
VALUES 
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);
```



3. 

```sql
ALTER TABLE countries RENAME TO hotels;
```



4. 

```sql
SELECT room_num, price
FROM hotels
ORDER BY price DESC
LIMIT 2;
```



5.

```sql
SELECT grade, COUNT(grade)
FROM hotels
GROUP BY grade
ORDER BY COUNT(grade) DESC;
```



6.

```sql
SELECT *
FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';
```



7.

```sql
SELECT *
FROM hotels
WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04';
```



1.

```python
User.objects.all()

User.objects.filter(id=19)

User.objects.values('age')

User.objects.filter(age__lte=40).values('id', 'balance')

User.objects.filter(last_name='김', balance__gte=500).values('first_name')

User.objects.filter(first_name__endswith='수', country='경기도').values('balance')

User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()

User.objects.filter(phone__startswith='010').count()

User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
User.objects.filter(first_name='옥자', last_name='김').values('country')

User.objects.filter(first_name='진호', last_name='백').delete()
User.objects.filter(first_name='진호', last_name='백')

User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]

User.objects.filter(phone__contains='123', age__lt=30)

User.objects.filter(phone__startswith='010').values('country').distinct()

User.objects.aggregate(Avg('age'))

User.objects.filter(last_name='박').aggregate(Avg('balance'))

User.objects.filter(country='경상북도').aggregate(Max('balance'))

User.objects.filter(country='제주특별자치도').order_by('-balance')[:1]
```



