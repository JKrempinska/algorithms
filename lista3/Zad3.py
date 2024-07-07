def sum_elements(seq):
    total = 0
    for i in range(len(seq)):
        for j in range(len(seq)):
            total += seq[i][j]
    return total

print(sum_elements([[1,2],[5,2]]))
