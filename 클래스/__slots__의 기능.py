class Person:
    __slots__ = ['name','age']      # name, age만 허용 (다른 속성은 생성 제한)

maria = Person()

maria.name = '마리아'
maria.age = 20

print(maria.name)
print(maria.age)

try:
    maria.address = '서초구'
    print(maria.address)
except AttributeError:
    print("허용되지 않은 속성으로 추가할 수 없습니다.")