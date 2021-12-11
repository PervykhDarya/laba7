#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    s = 0
    b = []
    for item in a:
        if (item % 4 == 0):
            s += 1
            b.append(item**2)
        else:
            b.append(item)

    print('количество возведённых в квадрат', s , '\nb ={}'.format(b))
 
