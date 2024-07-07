def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_inplace(arr):
    stack = []
    low = 0
    high = len(arr) - 1
    stack.append((low, high))
    
    while stack:
        low, high = stack.pop()
        pivot_index = partition(arr, low, high)
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

# Przykład użycia:
arr = [64, 25, 12, 22, -11, 0, 11,123,-1999,1.1]
print("Przed sortowaniem:", arr)
quicksort_inplace(arr)
print("Po sortowaniu:", arr)