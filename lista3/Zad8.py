def permutations(n):
    stack = [list(range(1, n + 1))]

    while stack:
        current_permutation = stack.pop()
        print(current_permutation)
       
        i = n - 2 #przedostatni element
        while i >= 0 and current_permutation[i] > current_permutation[i + 1]:
            i -= 1 #szukamy pierwszej sytuacji kiedy kolejny element jest mniejszy od poprzedniego

        if i >= 0:
            j = n - 1 #ostatni element
            while current_permutation[j] < current_permutation[i]: 
                j -= 1 #szukamy pierwszego element, który jest mniejszy od tego wyznaczonego w poprzedniej pętli
            current_permutation[i], current_permutation[j] = current_permutation[j], current_permutation[i] #zamieniamy miejscami
            current_permutation[i + 1:] = reversed(current_permutation[i + 1:]) #odwracamy
            stack.append(list(current_permutation))

permutations(4)




