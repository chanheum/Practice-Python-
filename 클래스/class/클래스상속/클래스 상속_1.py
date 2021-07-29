# class 기반클래스이름:
#     코드
#
# class 파생클래스이름(기반클래스이름):
#     코드
# ------------------------------------------------------------
class Person:
    def gretting(self):
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')

james = Student()
james.gretting()        # 기반 클래스 Person의 메서드 호출
james.study()           # 공부하기 : 파생 클래스 Student에 추가한 Study 메서드

# issubclass(파생클래스, 기반클래스) : 상속관계 확인
print(issubclass(Student,Person))