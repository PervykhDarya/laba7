#/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = list(map(float, input("Введите элементы массива: ").split()))
    c = float(input("Введите число С: "))

    s = 0
    for item in a:
        if item < c:
            s += 1

    print ('Количество элементов меньше С: ', s)

    sum = 0
    a.reverse()
    for item in a:
        if item < 0:
            break
        sum += int(item)

    print(f"Сумма элементов, после последнего отрицательного: {sum}")

    max_a = max(a)
    b = [num for num in a if num >= 0.8*max_a]
    c = [num for num in a if num < 0.8*max_a]
    print(f"Отсортированный массив: {b+c}")
