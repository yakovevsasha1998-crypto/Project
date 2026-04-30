person = {"name": "Oleg", "age": 25, "city": "Moscow", "job": "dev"} 

for i in person:
    if 'city' not in person:
        print('Нету такого ключа')
        break
    else:
        del person['city']
print(person)