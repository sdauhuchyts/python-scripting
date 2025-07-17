"""
Дан линуксовый путь /foo/../test/../test/../foo//bar/./baz.
Распарсить его и нормализовать, чтобы получился итоговый путь без перехода между уровнями вложенности по папкам.

/foo/bar/../test == /foo/test
/foo/../test/../test/../foo//bar/./baz == /foo/bar/baz
"""


def fun(path):
    list_path = path.split("/")
    res = []
    for d in list_path:
        if d == "" or d == ".":
            pass
        elif d == "..":
            del res[-1]
        else:
            res.append(d)
    res = "/".join(res)
    res = "/" + res
    return res


print(fun("/foo/../test/../test/../foo//bar/./baz"))
# Output: /foo/bar/baz
