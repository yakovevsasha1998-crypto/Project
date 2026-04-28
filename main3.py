items = [3,4,5,4,2,3,5,3,1,]

def unique_preseve_order(items):
    dubl = set()
    new_list = []
    for i in items:
        if i is None:
            continue
        if i not in dubl:
            dubl.add(i)
            new_list.append(i)
    return new_list

print(unique_preseve_order(items))
        
 