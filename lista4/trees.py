import collections

class Tree:
 #------------------------------- zagnieżdżona klasa Position -------------------------------
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            return not (self == other) # opposite of __eq__
# ---------- abstrakcyjne metody do zdefiniowania w podklasie ----------
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    # ---------- konkretne metody ----------
    def is_root(self, p):
        return self.root() == p
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def is_empty(self):
        return len(self) == 0
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height1(self): # works, but O(n^2) worst-case time
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    def _height2(self, p): # time is linear in size of subtree
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p) # start _height2 recursion
    def __iter__(self):
        for p in self.positions(): # use same order as positions()
            yield p.element() # but yield each element
    def positions(self):
        return self.preorder() # return entire preorder iteration
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # start recursion
                yield p
    def _subtree_preorder(self, p):
        yield p # visit p before its subtrees
        for c in self.children(p): # for each child c
            for other in self._subtree_preorder(c): # do preorder of c's subtree
                yield other # yielding each to our caller
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()): # start recursion
                yield p
    def _subtree_postorder(self, p):
        for c in self.children(p): # for each child c
            for other in self._subtree_postorder(c): # do postorder of c's subtree
                yield other # yielding each to our caller
        yield p # visit p after its subtrees

class BinaryTree(Tree):
 # --------------------- dodatkowe metody abstrakcyjne ---------------------
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    # ---------- metody konkretne zaimplemetowane w tej klasie ----------
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent) # possibly None
            else:
                return self.left(parent) # possibly None
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self, p):
        if self.left(p) is not None: # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p # visit p between its subtrees
        if self.right(p) is not None: # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other
    def positions(self):
        return self.inorder() # make inorder the default
    
class LinkedBinaryTree(BinaryTree):
 #-------------------------- zagnieżdżona klasa Node --------------------------
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right 
#-------------------------- zagnieżdżona klasa Position --------------------------
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        #-------------------------- metody publiczne --------------------------
        def __len__(self):
            return self._size

    def root(self):
        return self._make_position(self._root)
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None: # left child exists
            count += 1
        if node._right is not None: # right child exists
            count += 1
        return count
#-------------------------- metody niepubliczne --------------------------
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node) # node is its parent
        return self._make_position(node._left)
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node) # node is its parent
        return self._make_position(node._right)
    
class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__() # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token) # use inherited, nonpublic method
        if left is not None: # presumably three-parameter form
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right) # use inherited, nonpublic method
    
    def __str__(self):
        pieces = [] # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)
        
    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element())) # leaf value as a string
        else:
            result.append('(') # opening parenthesis
            self._parenthesize_recur(self.left(p), result) # left subtree
            result.append(p.element()) # operator
            self._parenthesize_recur(self.right(p), result) # right subtree
            result.append(')') 