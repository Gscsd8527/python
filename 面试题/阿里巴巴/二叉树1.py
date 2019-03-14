class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
def construct_tree(xianxu, zhongxu):
    # 判断先序的长度是否为0
    if len(xianxu) == 0:
        return None
    # 先序遍历的第一个结点一定是根结点
    root_data = xianxu[0]
    # 得到根节点，将根节点的元素放在中序中查找就能得到根节点在中序中的下标
    i = zhongxu.index(root_data)
    # 递归构造左子树和右子树
    left = construct_tree(xianxu[1: 1+i], zhongxu[:i])
    right = construct_tree(xianxu[1+i:], zhongxu[i+1:])
    return Node(root_data, left, right)

if __name__ == '__main__':
    xianxu = [1, 2, 4, 7, 3, 5, 6, 8]
    zhongxu = [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_tree(xianxu,zhongxu)
    print(root.data)
    print(root.left.data)
    print(root.right.data)
    print(root.left.left.data)
    print(root.left.left.right.data)
    print(root.right.right.left)
    print(root.right.left.data)
