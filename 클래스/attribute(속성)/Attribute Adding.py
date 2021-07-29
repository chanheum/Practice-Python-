# ----------------------------------------------------------------------
class Person:
    pass    # 빈 클래스 생성

maria = Person()        # 인스턴스 생성
maria.name = '마리아'    # 인스턴스를 만든 뒤 속성을 추가
print(maria.name)
# ----------------------------------------------------------------------
class Person_2:
    def greeting(self):
        self.hello = '안녕하세요'    # 메서드 호출하면서 속성을 추가

jamse = Person_2()

try:
    jamse.greeting()
    print(jamse.hello)
except AttributeError:
    print("아직 hello 속성이 없습니다.")
    print('인스턴스 내의 greeting 메서드를 호출해주셔야 hello 속성이 추가됩니다.')

