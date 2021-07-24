from binary_tree import BinaryTree, Node

if __name__ == "__main__":
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
