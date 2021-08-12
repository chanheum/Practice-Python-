class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for i in range(self.size)]
    ## 
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    ## 키를 가지고 주소값을 생성
    def hashfunc(self, key):
        return key % self.size
        
    ## 키를 가지고 주소값을 조회
    def getAddr(self, key):
        mykey = self.getKey(key)

        hash_address = self.hashfunc(mykey)
        return hash_address

    ## 해당하는 주소에 key와 value를 저장하는 함수
    def save(self, key, value):
        hash_address = self.getAddr(key)
        self.hash_table[hash_address] = value

    def read(self, key):
        hash_address = self.getAddr(key)
        return self.hash_table[hash_address]

    def delete(self, key):
        hash_address = self.getAddr(key)

        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        return False


ht = HashTable(8)
ht.save('a','1111')
ht.save('b','3333')
ht.save('c','5555')
ht.save('d','7777')
print(ht.hash_table)
print(ht.read('d'))

ht.delete('d')

print(ht.hash_table)