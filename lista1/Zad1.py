#1.
def poly_1(a_list, x):
    '''Jako pierwszy argument należy podać listę współczynników przy kolejnych potęgach x (od wyrazu wolnego do współczynnika przy najwyższej potędze)'''
    sum = 0
    for i in range(len(a_list)):
        xn = 1
        if i > 0:
            for _ in range(i):
                xn = xn*x
        sum = sum + (a_list[i]*xn)
    return sum

print(poly_1([1,3,4], 2))

#2.
def poly_2(a_list, x):
    sum = 0
    for i in range(len(a_list)):
        xn = 1
        if i > 0:
            for _ in range(i//2):
                xn = xn*x
            if i%2 == 0:
                xn = xn*xn
            else:
                xn = xn*xn*x
        sum = sum + (a_list[i]*xn)
    return sum

print(poly_2([1,3,0,1], 2))

#3. Złożoność obliczniowa schematu Hornera wynosi O(n), ponieważ trzeba wykonać n mnożeń, aby otrzymać wynik.

