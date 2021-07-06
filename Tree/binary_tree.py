class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root == None:
            return 0
        # 한 칸 내려갈때마다 길이 1증가
        return 1 + max(self.height(root.left), self.height(root.right))

    def pre_order(self, node):  # 전위순회
        if node != None:
            print(str(node.item),' ', end='')
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)

    def in_order(self, node):  # 중위순회
        if node != None:
            if node.left:
                self.in_order(node.left)
            print(str(node.item),' ', end='')
            if node.right:
                self.in_order(node.right)

    def post_order(self, node):  # 후위순회
        if node != None:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            print(str(node.item),' ', end='')

    def level_order(self, root):  # 레벨순회만 큐, 나머지는 스택
        queue = []
        queue.append(root)

        while len(queue) != 0:
            target = queue.pop(0)
            print(str(target.item),' ', end='')
            if target.left:
                queue.append(target.left)
            if target.right:
                queue.append(target.right)
