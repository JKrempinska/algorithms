# set_root, add_left_child, get_left_child, add_right_child, remove_node, __str__
class BinaryTree():

    def __init__(self):
        self.tree = [None]*10
        self.size = 0
    
    def resize(self):
        new_tree = [None]*len(self.tree)*2
        for i in range(len(self.tree)):
            new_tree[i] = self.tree[i]
        self.tree = new_tree

    def set_root(self, e):
        if self.tree[0] != None:
            raise ValueError('There is a root already')
        else:
            self.tree[0] = e
            self.size += 1

    def add_left_child(self, q, e):
        if self.size == len(self.tree):
            self.resize() 
        if self.tree[q] == None:
            raise ValueError('There is no parent')
        else:
            self.tree[2*q+1] = e
            self.size += 1
    
    def get_left_child(self, p):
        if self.tree[p] == None:
            raise ValueError('There is no parent at given position')
        elif self.tree[2*p+2] == None:
            raise ValueError('There is no left child')
        else: 
            return self.tree[2*p+1]
        
    def add_right_child(self, q, e):
        if self.size == len(self.tree):
            self.resize() 
        if self.tree[q] == None:
            raise ValueError('There is no parent')
        else:
            self.tree[2*q+2] = e
            self.size += 1
        
    def get_right_child(self, p):
        if self.tree[p] == None:
            raise ValueError('There is no parent at position')
        elif self.tree[2*p+1] == None:
            raise ValueError('There is no right child')
        else: 
            return self.tree[2*p+2]
        
    def remove_node(self, p):
        if self.tree[p] == None:
            raise ValueError('There is no node at the given position')
        else:
            self.tree[p] = None
            self.size -= 1
        
    def __str__(self):
        if self.tree[0] is None:
            return 'Empty tree'
        
        result = ''
        queue = [0]

        while queue:
            current = queue.pop(0)
            result += str(self.tree[current]) + ' '

            left_child = 2 * current + 1
            right_child = 2 * current + 2

            if left_child < len(self.tree) and self.tree[left_child] is not None:
                queue.append(left_child)
            if right_child < len(self.tree) and self.tree[right_child] is not None:
                queue.append(right_child)

        return result.strip()

        
tree = BinaryTree()
tree.set_root(1)
tree.add_left_child(0, 2)
tree.add_right_child(0, 3)
tree.add_left_child(1, 4)
tree.add_right_child(1, 5)

print(tree.__str__())




    