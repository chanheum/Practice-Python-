# 데이터 및 다음 노드 정보를 담을 Node 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Node 클래스를 가지고 본격적으로 LinkedList 기능을 구현할 Class 선언
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # Node를 LinkedList의 마지막에 추가하기
    def append(self, data):
        cur = self.head
        # 다음 Node가 없을 때까지 Node 넘어가기
        while cur.next != None:
            cur = cur.next
        # 마지막 Node에서 다음 Node를 추가해주기
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        # Node가 없을 때까지 탐색하면서 Data 출력하기
        while cur != None:
            print(cur.data)
            cur = cur.next

    # idx 번째 Node를 불러오기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    
    # 원하는 위치에 Node 추가하기
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        # Node를 위치에 추가 했을 때 다음 Node와 이전 Node를 지정해 준다.
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

test = LinkedList(10)
test.append(100)
test.append(1000)
test.add_node(1, 15)
test.delete_node(2)
test.print_all()