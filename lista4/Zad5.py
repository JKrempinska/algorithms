from Zad4 import BinaryTree
import string

def tokenize(raw):
    '''Tokenizuje podane wyrażenie wyrażenie. Zwraca listę z elementami typu set(Symbol, Typ)'''
    SYMBOLS = set('+-*^/() ') 
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])
            if raw[j] != ' ':
                tokens.append(raw[j]) 
            mark = j+1 
    if mark != n:
        tokens.append(raw[mark:n]) 
    for i in range(len(tokens)):
        if tokens[i] in ('+','-','*','^','/'):
            tokens[i] = (tokens[i], 'OPERATOR') 
        elif tokens[i] in ('(',')'):
            tokens[i] = (tokens[i], 'BRACKET')
        elif tokens[i] in ('sin', 'cos', 'exp', 'log'):
            tokens[i] = (tokens[i], 'FUNCTION')
        elif tokens[i] in set(string.ascii_letters):
            tokens[i] = (tokens[i], 'VARIABLE')
        else:
            tokens[i] = (tokens[i], 'NUMBER')
    return tokens


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def derivative(self):
        '''Metoda tworząca drzewo pochodnej wyrażenia.'''
        if self.value in ('+', '-'):
            return Node(self.value, self.left.derivative(), self.right.derivative())
        elif self.value == '*':
            return Node('+', Node('*', self.left.derivative(), self.right), Node('*', self.left, self.right.derivative()))
        elif self.value == '/':
            return Node('/', Node('-', Node('*', self.left.derivative(), self.right), Node('*', self.left, self.right.derivative())), Node('^', self.right, Node('2')))
        elif self.value == '^':
            return Node('+', Node('*', Node('*', self.right, Node('^', self.left, Node('-', self.right, Node('1')))), self.left.derivative()), Node('*', Node('log', self.left), Node('*', Node('^', self.left, self.right), self.right.derivative())))
        elif self.value == 'sin':
            if self.left is not None:
                return Node('*', Node('cos', self.left), self.left.derivative())
        elif self.value == 'cos':
            if self.left is not None:
                return Node('*', Node('-', Node('0'), Node('sin', self.left)), self.left.derivative())
        elif self.value == 'exp':
            if self.left is not None:
                return Node('*', Node('exp', self.left), self.left.derivative())
        elif self.value == 'log':
            if self.left is not None:
                return Node('/', self.left.derivative(), self.left)
        elif self.value[0] in ('0','1','2','3','4','5','6','7','8','9'):
            return Node('0') 
        elif self.value[0] in set(string.ascii_letters):
            return Node('1')
        
    def to_string(self):
        '''Metoda zamieniająca drzewo na łańcuch znaków'''
        if self.value in ('+', '-', '*', '/'):
            left_str = self.left.to_string() if self.left is not None else ""
            right_str = self.right.to_string() if self.right is not None else ""
            return f"({left_str} {self.value} {right_str})"
        elif self.value == '^':
            left_str = self.left.to_string() if self.left is not None else ""
            right_str = self.right.to_string() if self.right is not None else ""
            return f"({left_str} ^ {right_str})"
        elif self.value in ('sin', 'cos', 'exp', 'log'):
            left_str = self.left.to_string() if self.left is not None else ""
            return f"{self.value}({left_str})"
        elif self.value[0] in set(string.ascii_letters):
            return self.value
        elif self.value[0] in ('0','1','2','3','4','5','6','7','8','9'):
            return self.value

def build_tree(tokens):
    '''Funkcja budująca drzewo wyrażenia na podstawie tokenów.'''
    parentheses_count = 0
    operators = {'+', '-', '*', '/', '^'}
    
    
    for i in range(len(tokens) - 1, -1, -1):
        if tokens[i][0] == ')' and tokens[i][1] == 'BRACKET':
            parentheses_count += 1
        elif tokens[i][0] == '(' and tokens[i][1] == 'BRACKET':
            parentheses_count -= 1
        elif parentheses_count == 1 and tokens[i][0] in operators:
            right = tokens[i+1:-1]
            left = tokens[1:i]
            return Node(tokens[i][0], build_tree(left), build_tree(right))
    
    for i in range(len(tokens)):
        if tokens[i][1] == 'FUNCTION' and tokens[i+1][0] == '(' and tokens[i+2][0] == '(' and tokens[i-1] is not None:
            right = tokens[i+2:-1]
            return Node(tokens[i][0], build_tree(right))
        elif tokens[i][1] == 'FUNCTION' and tokens[i+1][0] == '(' and tokens[i+2][0] == '(' and tokens[i-1]:
            right = tokens[i+2:-1]
            return Node(tokens[i][0], build_tree(right))
        elif tokens[i][1] == 'FUNCTION' and tokens[i+1][0] == '(':
            right = tokens[i+1:-1]
            return Node(tokens[i][0], build_tree(right))
    for i in range(len(tokens)):
        if tokens[i][1] in ('VARIABLE','NUMBER'):
            return Node(tokens[i][0])
    
def print_tree(node, indent=0):
    '''Funkcja printująca drzewo.'''
    if node is not None:
        print("  " * indent + str(node.value))
        print_tree(node.left, indent + 1)
        print_tree(node.right, indent + 1)
 
