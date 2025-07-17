"""
Представьте, что вы работаете в IDE и примерно (нечетко) помните название файла и хотите его найти.
Необходимо написать функцию, которая определит, можно ли из второй строки сделать первую удалением части символов.
IDESearch('crdle', 'crocodile'); // true
IDESearch('tst', 'crocodile'); // false
"""

def IDESearch(line1, line2):
    res = ''
    k = 0
    for i in range(len(line1)):
        for j in range(k, len(line2)):
            if line1[i] == line2[j]:
                res += line1[i]
                k = j + 1
                break
        if i != len(line1) - 1 and j == len(line2) - 1:
            return False
    if res == line1:
        return True
    else:
        return False

def fun1(a, b):
    start = 0
    left = len(a)
    for i in range(len(a)):
        for j in range(start, len(b)):
            if a[i] == b[j]:
                left -= 1
                start = j + 1
                break
            else:
                j += 1
        if i != len(a) - 1 and j == len(b) -1:
            return False
    if left == 0:
        return True
    else:
        return False

# O(n)
def fun2(a, b):
    pointer1 = pointer2 = 0
    res = []
    while pointer1 < len(a) and pointer2 < len(b):
        if a[pointer1] == b[pointer2]:
            res.append(a[pointer1])
            pointer1 += 1
            pointer2 += 1
        else:
            pointer2 += 1
    if a == "".join(res):
        return True
    else:
        return False

print(IDESearch('crcd', 'crocodile'), fun1('crcd', 'crocodile'), fun2('crcd', 'crocodile')) # True
print(IDESearch('tst', 'crocodile'), fun1('tst', 'crocodile'), fun2('tst', 'crocodile')) # False
print(IDESearch('rdle', 'crocodilesdfs'), fun1('rdle', 'crocodilesdfs'), fun2('rdle', 'crocodilesdfs')) # True
print(IDESearch('mbfal', 'amberfall'), fun1('mbfal', 'amberfall'), fun2('mbfal', 'amberfall')) # True
