from Zad5 import build_tree
from Zad5 import tokenize

e1 = '(2+sin(x))'
e1 = build_tree(tokenize(e1))
de1 = e1.derivative()
de1=de1.to_string()
e2 = '(exp(log(2*x)))'
e2 = build_tree(tokenize(e2))
de2 = e2.derivative()
de2=de2.to_string()
e3 = '(x/x)'
e3 = build_tree(tokenize(e3))
de3 = e3.derivative()
de3=de3.to_string()
e4 = '((x^2)+((2*x)+cos(x)))'
e4 = build_tree(tokenize(e4))
de4 = e4.derivative()
de4=de4.to_string()
print(de1)
print(de2)
print(de3)
print(de4)