# close hashing
class CloseHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]

    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            for a in range(hash_address, len(self.hash_table)):
                # 특정 addr에 데이터가 들어가 있지 않으면
                if self.hash_table[a] == 0:
                    self.hash_table[a] = [key, value]
                    return
                # 같은 key값을 가진거라면 덮어쓴다
                elif self.hash_table[a][0] == key:
                    self.hash_table[a][1] = value
                    return
            return None
        else:
            self.hash_table[hash_address] = [key, value]

    def read(self, key):
        hash_address = self.getAddress(key)

        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a][0] == key:
                return self.hash_table[a][1]
        return None

    def delete(self, key):
        hash_address = self.getAddress(key)

        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a] == 0:
                continue
            if self.hash_table[a][0] == key:
                self.hash_table[a] = 0
                return
        return False


# Test Code
h_table = CloseHash(8)

data1 = 'aa'
data2 = 'ad'
print(ord(data1[0]), ord(data2[0]), "← 같은 addr를 지칭하고 있음")

h_table.save('aa', '3333')
h_table.save('ad', '9999')
h_table.save('aa', '1777')
h_table.save('af', '888')
print(h_table.hash_table)

h_table.read('ad')

h_table.delete('aa')
print(h_table.hash_table)

h_table.delete('ad')
print(h_table.hash_table)
