class Person:
    # Person 객체가 생성될 때 만들어지는 스페셜 메서드 (__로 시작)
    def __init__(self):
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)

charle = Person()
charle.greeting()