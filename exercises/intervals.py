"""
L = [1, 3, 4, 5, 7, 12, 13, 15] #1,3-5,7,12-13,15
"""

# O(n)
def fun1(L):
    res = []
    start = stop = 0
    for i in range(start, len(L) - 1):
        if L[i + 1] - L[i] == 1:
            stop = i + 1
        else:
            if start == stop:
                res.append(str(L[i]))
            else:
                res.append(str(L[start]) + "-" + str(L[stop]))
            start = stop = i + 1
    else:
        if start == stop:
            res.append(str(L[start]))
        else:
            res.append(str(L[start]) + "-" + str(L[stop]))
    return ','.join(res)

# O(n)
def fun2(L):
    res = []
    start = stop = 0
    while start < len(L) and stop < len(L):
        if stop == len(L) - 1:
            if start == stop:
                res.append(str(L[start]))
                stop += 1
                start = stop
                continue
            else:
                res.append(str(L[start]) + "-" + str(L[stop]))
                stop += 1
                start = stop
                continue
        if L[stop + 1] == L[stop] + 1:
            stop += 1
        else:
            if start == stop:
                res.append(str(L[start]))
                stop += 1
                start = stop
            else:
                res.append(str(L[start]) + "-" + str(L[stop]))
                stop += 1
                start = stop
    return ",".join(res)

print(fun1([1, 3, 4, 5, 7, 12, 13, 15]))
print(fun2([1, 3, 4, 5, 7, 12, 13, 15]))
