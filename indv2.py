#!/usr/bin/env python3
# -*- coding: utf-8 -*-
i = 0
f = ""
if __name__ == '__main__':
    s = input("Введите слово: ")
    f += s[:3]+s[-1]+s[4:-1]+s[3]
    print(f)