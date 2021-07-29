# list를 상속받았으므로 self로 list의 모든 메서드에 접근할 수 있다.
# self는 list 처럼 사용할 수 있다.
class Advancelist(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = Advancelist([1,2,3,1,2,3,1,2,3])
x.replace(1, 100)
print(x)