def get_alphabet_dictionary():
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
             'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
             'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
             }
    return d

def get_code(s:str):
    d = get_alphabet_dictionary()
    for i in s:
        print(d[i.lower()],end='')

get_code("AOR")

def get_code_list(s:str):
    d = get_alphabet_dictionary()
    l = [d[i.lower()] for i in s]
    return l

print(get_code_list("AOR"))

def get_squared_codes(d:dict):
    squared_dict = {l : d[l] ** 2 for l in d}
    return squared_dict

sd = get_squared_codes(get_alphabet_dictionary())
print(sd['c'], sd['e'])