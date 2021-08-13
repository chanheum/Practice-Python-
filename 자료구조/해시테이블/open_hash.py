# open hashing
class OpenHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]

    def getKey(self, data):
        # 앞 문자의 값만 가져와서 아스키로 변환하여 키를 생성
        self.key = ord(data[0])
        return self.key

    ## 해시 테이블의 실제 Integer Key값을 생성
    def hashFunction(self, key):
        # 아스키로 변환된 키를 Size만큼 Division하여 최종적인 저장 Address를 생성
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)

        # 만약 Address에 이미 값이 들어가 있다면
        if self.hash_table[hash_address] != 0:
            # Address에서 키 찾기
            for a in range(len(self.hash_table[hash_address])):
                # 값은 키값의 데이터가 들어가 있다면 그 키값에 값만 덮어쓴다.
                if self.hash_table[hash_address][a][0] == key:
                    self.hash_table[hash_address][a][1] = value
                    return
            # 같은 키값이 없으면 키를 추가해서 저장하기
            self.hash_table[hash_address].append([key, value])
        else:
            # 처음 데이터를 넣는데 '0'으로 되어있다면 키와 값을 리스트로 함께 넣어준다.
            self.hash_table[hash_address] = [[key, value]]

    def read(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                # 같은 키값을 가진 부분을 탐색한다
                if self.hash_table[hash_address][a][0] == key:
                    return self.hash_table[hash_address][a][1]
            return False
        else:
            return False

    def delete(self, key):
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    # 해당 주소에 중복된 키의 데이터가 들어가 있지 않으면, 그냥 '0'으로만 값을 초기화
                    if len(self.hash_table[hash_address]) == 1:
                        self.hash_table[hash_address] = 0
                    else:
                        # 해당 주소에 중복된 키를 가진 데이터가 들어가 있다면 해당 리스트는 삭제
                        del self.hash_table[hash_address][a]
                    return
            return False
        else:
            return False

# Test Code
h_table = OpenHash(8)

h_table.save('aa', '1111')
h_table.read('aa')

data1 = 'aa'
data2 = 'ad'

## 해시값이 동일함.
print(ord(data1[0]))
print(ord(data2[0]))

h_table.save('ad', '2222')
print(h_table.hash_table)

h_table.save('aa', '3333')
print(h_table.hash_table)

print(h_table.read('aa'))
print(h_table.read('ad'))

h_table.delete('aa')
print(h_table.hash_table)
print(h_table.delete('Data'))
h_table.delete('ad')
print(h_table.hash_table)