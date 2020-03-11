#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


class Field:
    """Класс, осуществляющий работу с игровой картой"""

    def __init__(self, value, ind, matrix, piece):
        self.ind = ind
        self.piece = piece
        self.value = value
        self.matrix = np.full((len(matrix), len(matrix)), 0)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.matrix[i, j] = matrix[i, j]
        self.set()

    def set(self):
        for i in range(len(self.piece)):
            self.matrix[self.piece[i]] = self.value

    def is_solution(self):
        condition = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i, j] == 0:
                    condition = False
        return condition

    def __str__(self):
        res = 'Result matrix: \n {}'
        return res.format(self.matrix)
