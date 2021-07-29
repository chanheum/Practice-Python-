# class 기반클래스이름1:
#     코드
#
# class 기반클래스이름2:
#     코드
#
# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
#     코드
# ------------------------------------------------------
class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

# 다중 상속 클래스
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()