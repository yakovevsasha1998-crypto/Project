def char_count(s):
    new = {}
    for i in s:
        count = 1
        if i not in new:
            new[i] = count
        elif i in new:
            new[i] += 1
        else:
            print('Error')
    return new

result = char_count('stttttttring')
print(result)