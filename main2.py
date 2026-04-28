def average(numbers):
    total = 0
    len_count = 0
    if type(numbers) == list:
        if not numbers:
            return '0.0'
    for i in numbers:
        if type(i) in (int,float):
            total += i
            len_count += 1
    if len_count == 0:
        return '0.0'
    
    return round(total/len_count,2)
     
print(average([3, 5, 7, 4, 2, 1, 4]))
    
