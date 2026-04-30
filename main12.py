dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3, 
	'd': 4,
}

new_dict = dct1 | dct2
for key, value in new_dict.items():
    print(f"{key}': {value},")
