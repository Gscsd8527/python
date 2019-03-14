class BTree:
    class Node:
        def push(self,link):
            if self.left is not None:
                self.left.push(link)
            link.add(self)
            if self.right is not None:
                self.right.push(link)
        def zhongxu(self):
           if self.left is not None:
               self.left.zhongxu()
           print(self.data)
           if self.right is not None:
               self.right.zhongxu()
        def __init__(self,data=None,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
        def add(self,node):
            if self.data > node.data :
                if self.left is None:
                    self.left=node
                else:
                    self.left.add(node)
            if self.data < node.data:
                if self.right is None:
                    self.right=node
                else:
                    self.right.add(node)
        def __str__(self):
            return str(self.data)
    def __init__(self,root=None):
        self.root=None
    def add(self,data):
        n=self.Node(data=data)
        if self.root is None:
            self.root = n
        else:
            self.root.add(n)
    def __iter__(self):
        #创建线性链表
        link = self.MyLink()
        self.pushDataToLink(link)
        #返回
        return link
    def pushDataToLink(self,link):
        self.root.push(link)
    class MyLink:
        def __init__(self):
            self.head=None
            self.tail=None
        def add(self,node):
            if self.head is None:
                self.head=node
            else:
                self.tail.right=node

            self.tail = node
        def __next__(self):
            p=self.head
            if p is None:
                raise StopIteration
            self.head=self.head.right
            return p
    def zhongxu(self):
        self.root.zhongxu()

btree = BTree()
btree.add(17)
btree.add(9)
btree.add(28)
btree.add(13)
btree.add(19)
btree.add(5)
btree.add(29)
btree.add(11)

print("----------------")
btree.zhongxu()
for n in btree:
    print(n)

