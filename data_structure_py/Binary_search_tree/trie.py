# 트라이 자료구조

class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
    
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        
        curr_node.data = string
        
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
            
        return curr_node.data != None
    
    # string 이 다른 문자의 접두어가 되는지 확인
    def is_prefix(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
            
        return bool(curr_node.children)
