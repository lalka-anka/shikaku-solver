#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, работающий с неквадратными матрицами"""


def create_square_field(length, width, mt):
    if length > width:
        for i in mt:
            i.append(1)
        return mt, 'l'
    else:
        to_add = []
        for _ in mt[0]:
            to_add.append(1)
        mt.append(to_add)
        return mt, 'w'


def back_to_orig(mt, key):
    if key == 'l':
        for i in mt:
            i.pop()
        return mt
    else:
        mt.pop()
        return mt
