#!/usr/bin/env python3

def fun(n):
    if n == 0:
        return
    else:
        fun(n - 1)
        print(n, end = " ")

fun(5)
