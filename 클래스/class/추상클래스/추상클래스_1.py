from abc import *

# 추상클래스 생성
# 추상클래스는 인스턴스로도 만들 수 없다.
class StudentBase(metaclass=ABCMeta):
    # 추상메서드 생성
    @abstractmethod
    def study(self):
        pass

    # 추상메서드 생성
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    # 부모클래스에서 추상메서드로 구현된 메서드는
    # 자식클래스에서 반드시 구현해줘야 함.
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()

try:
    maria = StudentBase()
except Exception:
    print('추상클래스는 인스턴스로 만들 수 없습니다.')