#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_input(data):
    """Метод, осуществляющий парсинг карты"""
    matrix = []
    parse_data = data.split('|')
    for d in parse_data:
        int_arr = []
        line = d.split()
        for l in line:
            int_num = int(l)
            int_arr.append(int_num)
        matrix.append(int_arr)
    return matrix
