class Node:
    """定义节点"""

    def __init__(self, elem):  # element是节点保存的数据
        self.elem = elem
        self.next = None


class SingleLinkList:
    """单项循环链表链表"""
    def __init__(self, node=None):
        self.__head = node 
        if node:
            node.next = self.__head 

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head  # cur是游标，挑起第一个节点，开始织链表
        count = 0  # 空列表返回0
        while cur:   # while cur != None:
            count += 1
            if cur.next == self.__head:
                break
            else:
                cur = cur.next  # 游标向下一个节点移动
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        for i in range(self.length()):
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, new_elem):
        """链表头部添加元素，头插法"""
        new_node = Node(new_elem)
        cur = self.__head

        # 1.尾节点指针指向新节点
        try:    # 若链表非空，则执行
            for i in range(self.length()-1):  # cur移动到尾节点
                cur = cur.next
            cur.next = new_node #尾节点next指向新结点

        except:
            pass

        finally:
            # 2.新节点插入self.__head位
            new_node.next, self.__head = self.__head, new_node
            # 注意，此句不能放在1的指针移动之前，否则length会因找不到self.__head而无限循环。


    def append(self, new_elem):
        """链表尾部添加元素,尾插法"""
        new_node = Node(new_elem)
        cur = self.__head

        # 空链表
        if self.is_empty():
            self.__head = new_node
            new_node.next = self.__head

        # 非空链表
        else:        
            for i in range(self.length()-1):
                cur = cur.next
            cur.next = new_node
            new_node.next = self.__head


    def insert(self, pos, new_elem):
        """指定位置添加元素"""
        cur = self.__head  
        new_node = Node(new_elem)
        if pos <= 0:
            self.add(new_elem)

        elif pos > self.length()-1:
            self.append(new_elem)

        else:
            for i in range(pos-1):
                cur = cur.next    # 从0位移动pos-1次，此时指向pos位的前一个节点。
            new_node.next, cur.next = cur.next, new_node

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        for i in range(self.length()): 
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return

        pre = self.__head   # 第一个游标pre
        cur = pre.next      # 第二个游标cur，指向pre的下一个节点

        if pre.elem == item:  # 如果是头结点
            self.__head = cur # 头指针指向下一节点
            # 更改尾节点next指向
            for i in range(self.length()-1):  # cur移动到尾节点
                pre = pre.next
            pre.next = self.__head #尾节点next指向新的头结点
            return

        else: # 中间节点和尾节点的场合
            while cur:
                if cur.elem == item:
                    pre.next = cur.next
                    break
                else:  # 两指针向下一位移动
                    pre ,cur = cur, cur.next

                if cur == self.__head: # cur返回头结点，便利结束
                    break
                    


if __name__ == "__main__":
    link_list = SingleLinkList()

    print(f"length:{link_list.length()}")
    link_list.append(3)
    link_list.add(2)
    link_list.travel()
    link_list.insert(0, 1)
    print(link_list.search(3))
    link_list.append(4)
    link_list.append(5)
    link_list.remove(4)
    print(f"length:{link_list.length()}")
    link_list.travel()

