# Person 클래스의 greeting 메서드와 Student 클래스의 greeting 메서드를 보면 '안녕하세요.'라는 문구가 중복됩니다.
# 이럴 때는 기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있습니다.
# Student의 greeting에서 super().greeting()으로 Person의 greeting을 호출했습니다.
# 즉, 중복되는 기능은 파생 클래스에서 다시 만들지 않고, 기반 클래스의 기능을 사용하면 됩니다.
# 이처럼 메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용합니다.
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 도장 학생입니다.')

maria = Student()
maria.greeting()