# 1, 클래스 [상속] 관계
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')

# 2, 클래스 [포함] 관계
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)