def palindrom(text):
    if len(text) < 2:
        return True
    elif text[0] == text[-1]:
        text = text[1:-1]
        return palindrom(text)
    else:
        return False
    
print(palindrom('kajak'))