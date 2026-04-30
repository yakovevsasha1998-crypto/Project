# Пример
text = "яблоко банан яблоко апельсин банан яблоко"
new_text = {}
# Твой код должен создать словарь:
# {
#     "яблоко": 3,
#     "банан": 2,
#     "апельсин": 1
# }


listing = text.split()

for i in listing:
    if i not in new_text:
        new_text[i] = 1
    else:
        new_text[i] = new_text[i] + 1
print(new_text)