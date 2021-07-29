class Person:
    def __init__(self):
        print('Person Init')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student Init')
        super().__init__()              # super()로 기반 클래스의 __init__ 메서드를 호출할 수 있다.
        self.school = '파이썬 코딩도장'    # 인스턴스 속성 추가

james = Student()
print(james.hello)
print(james.school)