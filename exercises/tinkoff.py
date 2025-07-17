"""
Сколько слов 'tinkoff' можно составить из символов данной строки
input: ffoknittinkoff
output: 2
"""

def fun(a, b):
    dict_a = {}
    dict_b = {}
    res = []
    for i in a:
        if i in dict_a:
            dict_a[i] += 1
        else:
            dict_a[i] = 1
    for i in b:
        if i in dict_b:
            dict_b[i] +=1
        else:
            dict_b[i] = 1
    for i in dict_b:
        if i in dict_a:
            res.append(dict_a[i] // dict_b[i])
        else:
            return 0
    return min(res)

print(fun('ffoknittinkoff', 'tinkoff'))
