# 클래스 선언하기
class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting() # sel.메서드() 형식으로 클래스 안의 메서드를 호출

jamse = Person()
jamse.hello()

# 특정 클래스의 인스턴스인지 확인
print(isinstance(jamse, Person))
