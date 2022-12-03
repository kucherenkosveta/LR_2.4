#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Нахождение суммы элементов, кратных двум
    summ = 0
    for i in a:
        if i % 2 == 0:
            summ += i
    print(f"Сумма элементов, кратных двум: {summ}")
