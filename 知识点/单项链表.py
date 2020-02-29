# 重点：链表，区块，游标cur，起始位指针self._head
# 这其实是一个编制围巾的过程。游标cur是针，区块是线，链表是已经织好的部分。cur.next(实际是node.next) = new_node是游标挑着前一个区块的线头(next)向另一个区块连接的过程。若没有next，则区块间连接不上。


class Node:
    """定义区块"""

    def __init__(self, elem):  # element是区块保存的数据
        self.elem = elem
        self.next = None


class SingleLinkList:
    """单链表"""

    def __init__(self, node=None):
        self.__head = node  # self.__head是链表的起始位置。不希望被用户调用，所以设成私有。

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head  # cur是游标，挑起第一个区块，开始织链表
        count = 0  # 空列表返回0
        while cur:   # while cur != None:
            count += 1
            cur = cur.next  # 游标向下一个区块移动
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, new_elem):
        """链表头部添加元素，头插法"""
        new_node = Node(new_elem)
        # new_node.next = self.__head   # 步骤1,new_node.next指向处于起始位的区块。
        # self.__head = new_node    # 步骤2，让起始位指针指向new_node。
        new_node.next, self.__head = self.__head, new_node
        # 空链表也适用

    def append(self, new_elem):
        """链表尾部添加元素,尾插发"""
        new_node = Node(new_elem)
        cur = self.__head

        # 空链表
        if self.is_empty():
            self.__head = new_node
            # 这是一个把区块挂在链表上的动作，不可以是cur=new_node，否则只是把游标换了个指向，而没把new_node织在self._head上。

        else:        # 非空链表
            while cur.next:
                cur = cur.next
            cur.next = new_node

            """不可以用如下写法:
            while cur:
                cur = cur.next
            cur = new_node"""

    def insert(self, pos, new_elem):
        """指定位置添加元素"""
        cur = self.__head  # 在教程中用了pre替换了cur，没有影响
        new_node = Node(new_elem)
        if pos <= 0:
            self.add(new_elem)

        elif pos > self.length()-1:
            self.append(new_elem)

        else:
            for i in range(pos-1):
                cur = cur.next    # 从0位移动pos-1-1次，此时指向pos位的前一个区块。
            new_node.next, cur.next = cur.next, new_node

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
        """删除区块"""
        pre = self.__head   # 第一个游标pre
        cur = pre.next      # 第二个游标cur，指向pre的下一个区块

        if pre.elem == item:  # 如果是头结点
            self.__head = cur
            return
        else:
            while cur:
                if cur.elem == item:
                    pre.next = cur.next
                    break
                else: #若当前区块非目标区块，则前进
                    # 写法1
                    pre = cur  # 让pre指向cur(既pre.next)区块
                    cur = pre.next  # 让cur指向pre的下一个区块

                    # 写法2，OK
                    # pre ,cur = cur, cur.next

                    # 以下两种写法同样可以执行。等号右侧的cur和pre.next并没有指向同一片内存。为什么？
                    # pre ,cur = cur, pre.next
                    # cur, pre = pre.next, cur


if __name__ == "__main__":
    link_list = SingleLinkList()

    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)

    link_list.travel()
    # 1 2 3 4 5

    link_list.remove(1)
    link_list.travel()
    # 2 3 4 5

    link_list.remove(5)
    link_list.travel()
    # 2 3 4
