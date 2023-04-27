# 전위순회: ROOT-L-R
# 중위순회: L-ROOT-R
# 후위순회: L-R-ROOT

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def height(self, root):
        if root == None:
            return 0
        # 한 칸 내려갈때마다 길이 1증가
        return 1 + max(self.height(root.left), self.height(root.right))

    def pre_order(self, node):  # 전위순회
        if node != None:
            print(str(node.item), ' ', end='')
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)

    def in_order(self, node):  # 중위순회
        if node != None:
            if node.left:
                self.in_order(node.left)
            print(str(node.item), ' ', end='')
            if node.right:
                self.in_order(node.right)

    def post_order(self, node):  # 후위순회
        if node != None:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            print(str(node.item), ' ', end='')

    def level_order(self, root):  # 레벨순회만 큐, 나머지는 스택
        queue = []
        queue.append(root)

        while len(queue) != 0:
            target = queue.pop(0)
            print(str(target.item), ' ', end='')
            if target.left:
                queue.append(target.left)
            if target.right:
                queue.append(target.right)


tree = BinaryTree()
n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n5 = Node(500)
n6 = Node(600)
n7 = Node(700)
n8 = Node(800)

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

print("전위순회:\t", end='')
tree.pre_order(tree.root)
print("\n중위순회:\t", end='')
tree.in_order(tree.root)
print("\n후위순회:\t", end='')
tree.post_order(tree.root)
print("\n레벨순회:\t", end='')
tree.level_order(tree.root)
