#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
"""Модуль, преобразующий строку с решением в матрицу"""


def process_res_matrix(str_res):
    lines = str(str_res).split('\n')
    res_arr = []
    lines = lines[1:]
    for line in lines:
        res_arr.append(re.findall(r'\w', line))
    for i in range(len(res_arr)):
        for j in range(len(res_arr)):
            res_arr[i][j] = res_arr[i][j]
    return res_arr
