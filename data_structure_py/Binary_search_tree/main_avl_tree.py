from avl_tree import AVLTree

if __name__ == "__main__":
    avl = AVLTree()
    avl.put(75, 'apple')
    avl.put(80, 'grape')
    avl.put(85, 'lime')
    avl.put(20, 'mango')
    avl.put(10, 'strawberry')
    avl.put(50, 'banana')
    avl.put(30, 'cherry')
    avl.put(40, 'watermelon')
    avl.put(70, 'melon')
    avl.put(90, 'plum')

    print('전위순회:\t', end='')
    avl.pre_order(avl.root)
    print('\n중위순회:\t', end='')
    avl.in_order(avl.root)

    print('\n75와 85 삭제 후:')
    avl.delete(75)
    avl.delete(85)
    print('전위순회:\t', end='')
    avl.pre_order(avl.root)
    print('\n중위순회:\t', end='')
    avl.in_order(avl.root)

    print("\n높이:", end='')
    print(avl.height(avl.root))
