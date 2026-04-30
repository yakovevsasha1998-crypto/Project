numbers = [1, 2, 3, 4, 5, 6]
number = 0
number2 = 0
new = []
new2 = []
if len(numbers) % 2 == 0:
    for i in numbers:
        new.append(i)
        number += 1
        if number >= 3:
            break


refreshing = numbers[::-1]
for i in refreshing:
    new2.append(i)
    number2 += 1
    if number2 >= 3:
        break

sum_first = sum(new)    # 1+2+3 = 6
sum_second = sum(new2)  # 6+5+4 = 15

print(f"Первая половина: {new}, сумма = {sum_first}")
print(f"Вторая половина (перевёрнутая): {new2}, сумма = {sum_second}")
print(f"Результат деления: {sum_first / sum_second}")  # 6 / 15 = 0.4





        
