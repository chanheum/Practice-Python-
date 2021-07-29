# 참고 | 공개 속성과 비공개 속성
# 클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고,
# 클래스 안에서만 접근할 수 있는 속성을 비공개 속성(private attribute)이라 부릅니다.
class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet          # 변수 앞에 __를 붙이면 비공개 속성으로 만들어짐

    def pay(self, amount):
        if self.__wallet < amount:
            print('돈이 {0}원 모자릅니다.'.format(amount - self.__wallet))
        else:
            self.__wallet -= amount
            print('이제 {0}원 남았어요'.format(self.__wallet))

maria = Person('마리아',20,'서초구',10000)
try:
    maria.__wallet -= 10000
except AttributeError:
    print("클래스 바깥에서는 비공개 속성에 접근할 수 없습니다.")

# 클래스 내에서만 접근 가능!!
maria.pay(3000)
maria.pay(12500)