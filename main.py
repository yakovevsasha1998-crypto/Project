def func(name,age,city):
    try:
        if type(age) != int:
            print('Напишите число в поле age ')
            return 
        elif age < 0 or age > 150:
            print('Возраст должен быть положительным и не больше 150')
            return
        elif name == '' or name == None or type(name) != str:
            print('Пустая строка либо некорректные символы - должна быть строка')
            return
        elif type(city) != str:
            print('Должна быть строка!')
            return
        print(f'Name: {name}, Age: {age}, City: {city} ')
    except ValueError:
        print('Некорректный возраст')

func('',6,'Cheb')