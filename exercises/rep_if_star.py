import re


def replace_if_star(link):
    if link.startswith("*"):
        res = "https://" + link.replace("*", "test")
    else:
        res = re.sub("(.+?)\.(.*)", "https://\\1-ms.\\2", link)
    return res


print(replace_if_star("dfsd.local.com"))
