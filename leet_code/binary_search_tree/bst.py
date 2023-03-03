class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        # initalize new node
        new_node = Node(value)
        
        # if tree is empty, insert new node in root
        if self.root is None:
            self.root = new_node
            return True
       
       # if tree is not empty, create tmp pointer to compare new_node
        tmp = self.root
        while(True):
            # if duplicate value exist, return false
            if new_node.value == tmp.value:
                return False
            
            # if inserting value smaller -> go left
            elif new_node.value < tmp.value:
                # if end of tree -> insert new node to left
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                # else continue
                tmp = tmp.left
            # if inserting value bigger -> go right
            elif new_node.value > tmp.value:
                # if end of tree -> insert new node to right
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                # else continue
                tmp = tmp.right

    def contains(self, value):
        tmp = self.root
        while (tmp is not None):
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            elif value == tmp.value:
                return True
        return False

new = BinarySearchTree()
new.insert(10)
new.insert(100)
new.insert(200)
print(new.contains(100))
             