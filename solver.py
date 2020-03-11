#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue
from state import Field
import numpy as np


class Processor:
    """Класс, осуществляющий поиск решений"""
    def __init__(self, matrix):
        self.points = list()
        self.queue = queue.Queue()
        self.grid = matrix
        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i, j] != 0:
                    self.points.append([i, j, matrix[i, j], n])
                    n += 1

    def get_point(self, i):
        return self.points[i]

    def get_by_width(self):

        initial = Field(-1, -1, self.grid, [])
        self.queue.put(initial)
        goal = None

        while not self.queue.empty() and goal is None:
            current = self.queue.get()
            if current.is_solution():
                goal = current
            if current.ind + 1 < len(self.points):
                p = self.get_point(current.ind + 1)

                neigh = get_neighbours(p[0], p[1], p[2], current.matrix, current.ind + 1)
                for n in range(len(neigh)):
                    self.queue.put(neigh[n])

        return goal


def is_prime(number):
    for n in range(2, number):
        if (number % n) == 0:
            return False
    return True


def check(x, y, ind, new_value, mat, dim, value):
    h = []
    v = []
    hb = y - value + 1
    vb = x - dim + 1

    if hb < 0:
        hb = 0
    if vb < 0:
        vb = 0

    while hb <= y and vb <= x:
        hbaux = []

        for i in range(dim):
            for j in range(value):
                if (x, y) == (vb + i, hb + j) and hb + j < len(mat) and vb + i < len(mat):
                    hbaux.append((vb + i, hb + j))
                if hb + j < len(mat) and vb + i < len(mat) and mat[vb + i, hb + j] == 0:
                    hbaux.append((vb + i, hb + j))
        if len(hbaux) == new_value:
            p = Field(new_value, ind, mat, hbaux)
            h.append(p)

        hb += 1
        if hb > y and vb <= x:
            hb = y - value + 1
            if hb < 0:
                hb = 0
            vb += 1

    return v, h


def get_neighbours(x, y, value, matrix, ind):
    wt = st = []
    for dim in range(1, value + 1):
        if value % dim == 0:
            w, s = check(x, y, ind, value, matrix, dim, int(value / dim))
            st = st + s
            wt = wt + w
    neigh = wt + st
    return neigh


def return_result_matrix(mat):
    result = Processor(mat)
    return result.get_by_width()
