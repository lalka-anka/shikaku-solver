#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий запуск программы"""
import argparse
import numpy as np
from solver import return_result_matrix
from rendering import get_gui
from parsing import parse_input
from process_not_square_mat import create_square_field
from process_not_square_mat import back_to_orig
from process_str_matrix import process_res_matrix
import re


def get_contains(filename):
    """Метод, считывающий данные из файла"""
    matrix = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            int_arr = []
            line = l.split()
            for num in line:
                int_num = int(num)
                int_arr.append(int_num)
            matrix.append(int_arr)
    matrix = np.array(matrix)
    result_matrix = return_result_matrix(matrix)
    return result_matrix


def parsing():
    """Метод, осуществляющий парсинг и выводящий результат"""
    parser = argparse.ArgumentParser(description='Shikaku solver')
    parser.add_argument('-mt', '--matrix', type=str, metavar='', help='Matrix with a field for the game')
    parser.add_argument('-doc', '--document', type=str, metavar='', help='Document with a field for the game')
    parser.add_argument('-save', '--save', type=str, metavar='', help='The path of the file in which to save result '
                                                                      'field')
    parser.add_argument('-gui', '--interface', type=str, metavar='', help='Using the GUI (true or None)')
    parser.add_argument('-len', '--length', type=str, metavar='', help='Length of field')
    parser.add_argument('-wd', '--width', type=str, metavar='', help='Width of field')
    args = parser.parse_args()
    matrix = args.matrix
    doc = args.document
    save = args.save
    gui = args.interface
    ln = args.length
    wd = args.width
    result = None
    if gui is not None and ln is not None and wd is not None:
        return get_gui(int(ln), int(wd))
    elif gui is not None and ln is None and wd is None:
        length = int(input('Введите длину игрового поля: '))
        width = int(input('Введите ширину игрового поля: '))
        return get_gui(length, width)
    else:
        if matrix is None and doc is None:
            mt = input('Введите игровое поле: ')
            mt = mt[1:-1]
            mt = parse_input(mt)
            length = len(mt)
            width = len(mt[0])
            if length != width:
                new_mat, key = create_square_field(length, width, mt)
                new_mat = np.array(new_mat)
                result = return_result_matrix(new_mat)
                result = process_res_matrix(result)
                result = back_to_orig(result, key)
            else:
                result = return_result_matrix(np.array(mt))
        elif doc is not None and matrix is None:
            result = get_contains(doc)

        elif doc is None and matrix is not None:
            mt = parse_input(matrix)
            length = len(mt)
            width = len(mt[0])
            if length != width:
                new_mat, key = create_square_field(length, width, mt)
                new_mat = np.array(new_mat)
                result = return_result_matrix(new_mat)
                result = process_res_matrix(result)
                result = back_to_orig(result, key)
            else:
                result = return_result_matrix(np.array(mt))

        if len(re.findall(r'\w+', str(result))) == 0:
            result = 'Решений нет'

        if save is None:
            print(result)
        else:
            with open(save, 'w') as f:
                f.write(result)


if __name__ == '__main__':
    parsing()
