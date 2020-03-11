#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, возвращающий количество вариантов решения"""


def get_count_solutions(arr, raw_arr):
    length = len(arr)
    width = len(arr[0])
    d = 2
    count = 1
    key = 1
    for r in range(len(arr)-1):
        if set(arr[r]) == set(arr[r+1]) and raw_arr[r] != raw_arr[r+1] and '1' not in arr[r]:
            key = 2
    if key != 1:
        return key
    for r in range(len(arr)-1):
        if set(arr[r]) == set(arr[r+1]) and raw_arr[r] == raw_arr[r+1]:
            return 1
    while d <= len(arr):
        for col in range(width - d + 1):
            for row in range(length - d + 1):
                if arr[row][col] == arr[row + d - 1][col + d - 1] == arr[row + d - 1][col] == arr[row][col + d - 1]:
                    count += 1
        d += 1
    if int(count / len(arr)) != 0:
        return int(count / len(arr))
    else:
        return 1
