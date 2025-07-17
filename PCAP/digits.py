#!/usr/bin/env python3

digits = [
    ["###", "  #", "###", "###", "# #", "###", "###", "###", "###", "###"],
    ["# #", "  #", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"],
    ["# #", "  #", "###", "###", "###", "###", "###", "  #", "###", "###"],
    ["# #", "  #", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"],
    ["###", "  #", "###", "###", "  #", "###", "###", "  #", "###", "###"]
]

def fun(num):
    global digits
    res = [[] for i in range(5)]
    for i in range(5):
        for s in num:
            res[i].append(digits[i][int(s)])
    for i in range(5):
        print(" ".join(res[i]))

fun(input("Please, enter number: "))
