"""双链表"""


class Node:
    """定义节点"""

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList:
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self, reverse=0):
        """if set reverse==1，print linkList reversed"""
        cur = self.__head
        if reverse == False:
            while cur:
                print(cur.elem, end=" ")
                cur = cur.next
            print("")

        elif reverse == True:  # 私人订制，检查prev是否设置完全
            for i in range(self.length()-1):
                cur = cur.next
            while cur:
                print(cur.elem, end=" ")
                cur = cur.prev
            print("")

    def add(self, elem):
        """头插法"""
        node = Node(elem)
        node.next = self.__head
        self.__head = node
        if node.next:  # 后续有区块的情况下，才能用node.next.prev
            node.next.prev = node  # 把后继节点的prev指针指向新插入节点

    def append(self, elem):
        node = Node(elem)
        if self.isEmpty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, elem):
        """插入操作，pos:插入位置，elem:插入元素"""
        node = Node(elem)

        if pos <= 0:
            self.add(elem)

        elif pos > self.length()-1:
            self.append(elem)

        else:
            cur = self.__head
            for i in range(pos):  # 指向了pos位
                cur = cur.next
            # 操作4指针：node的2条，cur.prev, cur.prev.next
            node.prev, node.next, cur.prev, node.prev.next\
                = cur.prev, cur, node, node  # \是脚本换行
            # node.prev = cur.prev
            # node.next = cur
            # cur.prev.next = node
            # cur.prev = node

    def search(self, item):
        """查找区块是否存在"""
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        # 和单链表的不同之处在于只需要一根指针
        cur = self.__head

        if item == self.__head.elem:  # 如果是头节点
            self.__head = cur.next
            try:
                cur.next.prev = None  # 操作后继节点指针
            except Exception:
                pass
            return

        else:
            # 找到要删除的节点
            while cur:
                if cur.elem == item:
                    # 考虑到尾节点没有next,用try。
                    try:
                        cur.prev.next, cur.next.prev = cur.next, cur.prev
                    except Exception:
                        pass

                    # if cur.next:  # 如果不是尾节点，则调节后继节点指针
                    #     cur.next.prev = cur.prev

                    break
                else:
                    cur = cur.next  # 移动


if __name__ == "__main__":
    dll = DoubleLinkList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.insert(3, 0)
    dll.remove(1)
    dll.travel()
