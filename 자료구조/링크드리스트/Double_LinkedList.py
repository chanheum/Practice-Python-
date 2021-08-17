class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    # 데이터를 연결 Node 맨 뒤에 삽입
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head

            while node.next:
                node = node.next
            # 마지막 Node에 추가할 Node를 연결해주고 추가할 Node의 prev에 마지막 Node를 추가
            temp = Node(data)
            node.next = temp
            temp.prev = node

    def descend(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            
    # data를 head부터 찾아서 삭제
    def delete(self, data):
        if self.head is None:
            return False
        # 데이터를 삭제하는데, head에 있는 데이터를 삭제하는 것이라면
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
        else:
            node = self.head

            # head에서부터 삭제할 데이터가 있는지 탐색
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next

                    if node.next is None:
                        pass
                    else:
                        node.next.prev = node
                    del temp

                else:
                    node = node.next

#Test Code
dLinked_list = DoubleLinkedList()

for a in range(1, 9 + 1):
    dLinked_list.insert(a)

print('Insert를 한 다음에 list를 출력합니다.')
dLinked_list.descend()
dLinked_list.delete(1)
dLinked_list.delete(9)
dLinked_list.delete(8)
dLinked_list.delete(101)

print('delete를 한 다음에 list를 출력합니다.')
dLinked_list.descend()

print(dLinked_list.head.next.prev.data)