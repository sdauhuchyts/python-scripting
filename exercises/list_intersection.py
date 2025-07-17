"""
Input: [1,2,4,5], [3,3,4], [2,3,4,5,6]
Output: 4
"""

# O(n)
def fun1(a, b, c):
    res = []
    for i in a:
        if i in b and c:
            res.append(i)
    return res

# O(n)
def fun2(a, b, c):
    res = []
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            res.append(a[i])
            i+=1
            j+=1
            k+=1
            continue
        if a[i] < b[j] or a[i] < c[k]:
            i+=1
            continue
        if a[i] > b[j]:
            j+=1
        if a[i] > c[k]:
            k+=1
    return res


a = [1,2,4,5]
b = [3,3,4]
c = [2,3,4,5,6]

print(fun1(a, b, c))
print(fun2(a, b, c))
