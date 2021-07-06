class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node == None:
            return 0
        return node.height

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right    # 서브트리 이식
        left_child.right = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + \
            max(self.height(left_child.left), self.height(left_child.right))
        return left_child   # 리턴으로 연결

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + \
            max(self.height(right_child.left), self.height(right_child.right))
        return right_child

    def balance_index(self, node):
        return self.height(node.left) - self.height(node.right)

    def balance(self, node):
        if self.balance_index(node) > 1:    # 왼쪽 자식이 높은 경우
            if self.balance_index(node.left) < 0:   # 왼쪽 자식의 오른쪽 서브트리가 높은 경우
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)

        elif self.balance_index(node) < -1:
            if self.balance_index(node.right) > 0:   # 오른쪽 자식의 왼쪽 서브트리가 높은 경우
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, node, key, value):
        if node == None:
            return Node(key, value, 1)  # 높이 1인 새노드 생성
        if node.key > key:
            node.left = self.put_item(node.left, key, value)
        elif node.key < key:
            node.right = self.put_item(node.right, key, value)
        else:   # 덮어씌우기
            node.value = value
            return node
        # node의 높이 갱신
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.balance(node)

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, node):
        if node.left == None:
            return node
        return self.minimum(node.left)

    def del_min(self, node):
        if node.left == None:
            return node.right   # 부모가 오른쪽 자식으로 대체
        node.left = self.del_min(node.left)
        return node

    # 삭제연산은 삽입연산과 똑같이 이루어진다
    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.del_node(node.left, key)
        elif node.key < key:
            node.right = self.del_node(node.right, key)
        else:   # 삭제할 노드 발견
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            del_target = node
            # 오른쪽 서브트리의 노드 중 최솟값이 삭제된 자리에 들어온다
            node = self.minimum(del_target.right)
            node.right = self.del_min(del_target.right)
            node.left = del_target.left
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.balance(node)


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
