class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST():
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, node, key):
        if node == None:
            return None
        if node.key > key:   # 왼쪽 서브트리 탐색
            return self.get_item(node.left, key)
        elif node.key < key:
            return self.get_item(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, node, key, value):
        if node == None:
            return Node(key, value)
        if node.key > key:
            node.left = self.put_item(node.left, key, value)
        elif node.key < key:
            node.right = self.put_item(node.right, key, value)
        else:
            node.value = value
        return node

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, node):
        if node.left == None:
            return node
        return self.minimum(node.left)

    def delete_min(self):
        if self.root == None:
            print("트리가 비어 있음")
        self.root = self.del_min(self.root)

    def del_min(self, node):
        if node.left == None:
            return node.right   # 부모가 오른쪽 자식으로 대체
        node.left = self.del_min(node.left)
        return node

    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.del_node(node.left, key)
            return node
        elif node.key < key:
            node.right = self.del_node(node.right, key)
            return node
        if node.right == None:
            return node.left
        if node.left == None:
            return node.right
        del_target = node
        # 오른쪽 서브트리의 노드 중 최솟값이 삭제된 자리에 들어온다
        node = self.minimum(del_target.right)
        node.right = self.del_min(del_target.right)
        node.left = del_target.left
        return node


    def pre_order(self, node):  # 전위순회
        if node != None:
            print(node.key,' ', end='')
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)

    def in_order(self, node):  # 중위순회
        if node != None:
            if node.left:
                self.in_order(node.left)
            print(node.key,' ', end='')
            if node.right:
                self.in_order(node.right)

    def post_order(self, node):  # 후위순회
        if node != None:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            print(node.key,' ', end='')

    def level_order(self, root):
        queue = []
        queue.append(root)

        while len(queue) != 0:
            target = queue.pop(0)
            print(target.key,' ', end='')
            if target.left:
                queue.append(target.left)
            if target.right:
                queue.append(target.right)
