#!/usr/bin/python -i
# -*- coding: utf-8 -*-
"""Модуль, раскрашивающий матрицу с решением"""


def get_matrix_with_color(mt, key, length, width):
    colors = ['seashell', 'deeppink', 'silver', 'plum', 'peru', 'darkgreen', 'purple', 'bisque',
              'light yellow', 'thistle', 'coral1']
    num_and_col = {'1': 'darkred', '2': 'blue', '3': 'blueviolet', '4': 'orangered', '5': 'darkorange', '6': 'deepskyblue',
                   '7': 'lightpink', '8': 'red', '9': 'lime'}
    matrix_value = {}
    count_col = {'blue': 0, 'blueviolet': 0, 'orangered': 0, 'darkorange': 0, 'deepskyblue': 0, 'lightpink': 0,
                 'red': 0, 'lime': 0, 'darkgreen': 0, 'darkred': 0, 'deeppink': 0, 'silver': 0, 'plum': 0, 'peru': 0,
                 'purple': 0, 'seashell': 0, 'bisque': 0, 'light yellow': 0, 'thistle': 0, 'coral1': 0}
    if key > 1:
        for row in range(width):
            for col in range(length):
                set_values(num_and_col, mt, col, row, count_col, colors, matrix_value)
        return matrix_value

    else:
        for col in range(length):
            for row in range(width):
                set_values(num_and_col, mt, col, row, count_col, colors, matrix_value)
        return matrix_value


def set_values(num_and_col, mt, col, row, count_col, colors, matrix_value):
    color = num_and_col[mt[col][row]]
    number = mt[col][row]
    if count_col[color] == int(number):
        num_and_col[number] = colors.pop()
        color = num_and_col[number]
    coord = (col, row)
    count_col[color] += 1
    matrix_value[coord] = (number, color)
