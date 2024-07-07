
def max_and_min(s):

    if len(s) == 1:
        return s[0], s[0]

    if len(s) == 2:
        if s[0] > s[1]:
            return s[0], s[1]
        else:
            return s[1], s[0]

    mid = len(s) // 2
    left_max, left_min = max_and_min(s[:mid])
    right_max, right_min = max_and_min(s[mid:])

    if left_max>right_max:
        max_val = left_max
    elif left_max<right_max:
        max_val = right_max
    elif left_max==right_max:
        max_val = right_max

    if left_min>right_min:
        min_val = right_min
    elif left_min<right_min:
        min_val = left_min
    elif left_min==right_min:
        min_val = right_min
    
    return max_val, min_val

print(max_and_min([8,5,8,0,8,2,8]))

