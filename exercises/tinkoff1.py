"""
Необходимо написать простейший алгоритм дешифровки записи.
Шифрование работает следующим образом: из исходного сообщения выписываются подряд все символы, стоявшие на четных позициях,
далее подряд все символы, стоявшие на нечетных позициях.

Input: qwertyu
Output: rqtwyeu
"""

# O(n)
def fun(a):
    res = []
    mid = len(a) // 2
    i = 0
    j = mid
    while j < len(a):
        res.append(a[j])
        if i < mid:
            res.append(a[i])
        i += 1
        j += 1
    return "".join(res)

print(fun("qwertyu"))
