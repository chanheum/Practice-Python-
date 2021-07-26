class Person:
    # 클래스 속성 생성
    bag = []
    def put_bag(self, stuff):
        # 클래스 속성에는 self가 어울리지 않으므로, 
        # 클래스에 속한 속성을 표현하는 것으로 변경하는게 좋음
        Person.bag.append(stuff)
        # self.bag.append(stuff)
james = Person()
james.put_bag('책')  # james 인스턴스에 '책' 삽입

maria = Person()
maria.put_bag('열쇠') # maria 인스턴스에 '열쇠' 삽입

# 인스턴스를 각각 만들었지만 모두 들어가 있음.
# 클래스 속성은 클래스에 속해있어서 인스턴스에서 공유할 수 있다.
print(james.bag)
print(maria.bag)