# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        return self.__name
    
    def __repr__(self):
        return "{0}( name: {1}, gender: {2}, height: {3})"\
            .format(self.__class__.__name__,self.name, self.gender, self.height)


students = [
    Student("홍길동","남","182.1"),
    Student("이순신","남","172.1"),
    Student("유관순","여","162.1"),
    Student("강감찬","남","178.1")
]

for student in students:
    print(student)

print("name으로 오름차순 정렬 후 ======>>")

for student in sorted(students, key = lambda x: x.name):
    print(student)

print("name으로 내림차순 정렬 후 ======>>")

for student in sorted(students, key = lambda x: x.name, reverse=True):
    print(student)

print("height으로 오름차순 정렬 후 =====>>")

for student in sorted(students, key = lambda x: x.height):
    print(student)

print("height으로 내림차순 정렬 후 =====>>")

for student in sorted(students, key = lambda x: x.height, reverse= True):
    print(student)