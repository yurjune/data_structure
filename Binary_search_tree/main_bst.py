from bst import BST

if __name__ == "__main__":
    bst = BST()
    bst.put(500, 'apple')
    bst.put(600, 'banana')
    bst.put(200, 'melon')
    bst.put(100, 'orange')
    bst.put(400, 'lime')
    bst.put(250, 'kiwi')
    bst.put(150, 'grape')
    bst.put(800, 'peach')
    bst.put(700, 'cherry')
    bst.put(50, 'pear')
    bst.put(350, 'lemon')
    bst.put(10, 'plum')

    print('전위순회:\t', end='')
    bst.pre_order(bst.root)
    print('\n중위순회:\t', end='')
    bst.in_order(bst.root)

    print('\n250:', bst.get(250))

    bst.delete(200)
    print('200 삭제 후:')
    print('전위순회:\t', end='')
    bst.pre_order(bst.root)
    print('\n중위순회:\t', end='')
    bst.in_order(bst.root)
