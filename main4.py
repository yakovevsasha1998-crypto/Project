def is_palindrome(text):
    reverse = text[::-1]

    if type(text) != str:
        print('Нужна строка')
        return
    if text == reverse:
        print('Является плиндромом')  
    else:
        print('Не является палиндромом')  

is_palindrome('12321')  
