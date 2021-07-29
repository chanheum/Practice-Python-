class Person:
    def __greeting(self):
        print('hello')
    def hello(self):
        self.__greeting()

james = Person()
james.hello()
try:
    james.__greeting()
except AttributeError:
    print('클래스 바깥에서는 비공개 메서드를 호출할 수 없습니다.')
