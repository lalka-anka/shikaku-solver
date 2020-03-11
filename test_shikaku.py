#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль с тестами"""
import unittest
from solver import is_prime
import numpy as np
from solver import return_result_matrix
from parsing import parse_input
from process_str_matrix import process_res_matrix
from get_dict_with_values import get_matrix_with_color
from get_count_solutions import get_count_solutions


class Tests(unittest.TestCase):
    def test_for_anytask_1(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(1, 1)

    def test_for_anytask_2(self):
        self.assertEqual(2, 2)

    def test_prime_number(self):
        res = is_prime(5)
        self.assertEqual(True, res)

    def test_not_prime_number(self):
        res = is_prime(10)
        self.assertEqual(False, res)

    def test_right_solve_1(self):
        state = np.array([[2, 0], [2, 0]])
        res = str(return_result_matrix(state))
        exp = """Result matrix: 
 [[2 2]
 [2 2]]"""
        self.assertEqual(exp, res)

    def test_right_solve_2(self):
        state = np.array([[2, 0, 4, 0, 0, 2, 0], [0, 0, 0, 6, 0, 0, 0], [4, 0, 2, 0, 4, 4, 0], [0, 0, 0, 0, 0, 4, 0],
                          [0, 0, 4, 0, 2, 0, 0], [0, 2, 0, 0, 0, 0, 2], [0, 0, 0, 4, 3, 0, 0]])
        res = str(return_result_matrix(state))
        exp = """Result matrix: 
 [[2 4 4 6 4 2 2]
 [2 4 4 6 4 4 4]
 [4 2 2 6 4 4 4]
 [4 4 4 6 4 4 4]
 [4 4 4 6 2 4 4]
 [4 2 2 6 2 2 2]
 [4 4 4 4 3 3 3]]"""
        self.assertEqual(exp, res)

    def test_right_solve_3(self):
        state = np.array([[2, 0, 0, 0, 0], [2, 2, 0, 0, 0], [0, 0, 0, 0, 9], [4, 0, 0, 4, 0], [0, 0, 2, 0, 0]])
        res = str(return_result_matrix(state))
        exp = """Result matrix: 
 [[2 2 9 9 9]
 [2 2 9 9 9]
 [2 2 9 9 9]
 [4 4 2 4 4]
 [4 4 2 4 4]]"""
        self.assertEqual(exp, res)

    def test_right_solve_4(self):
        state = np.array([[2, 0, 0, 0, 0], [2, 2, 0, 0, 0], [0, 0, 0, 0, 9]])
        res = return_result_matrix(state)
        self.assertEqual(None, res)

    def test_right_parse_1(self):
        data = '2 0 0 0 0 | 2 2 0 0 0 | 0 0 0 0 9 | 4 0 0 4 0 | 0 0 2 0 0'
        exp = str([[2, 0, 0, 0, 0], [2, 2, 0, 0, 0], [0, 0, 0, 0, 9], [4, 0, 0, 4, 0], [0, 0, 2, 0, 0]])
        res = str(parse_input(data))
        self.assertEqual(exp, res)

    def test_right_parse_2(self):
        data = '2 0 | 2 0'
        exp = str([[2, 0], [2, 0]])
        res = str(parse_input(data))
        self.assertEqual(exp, res)

    def test_process_matrix_1(self):
        matrix_str = """Result matrix: 
        [[2 2]
        [2 2]]"""
        exp = [['2', '2'], ['2', '2']]
        res = process_res_matrix(matrix_str)
        self.assertEqual(exp, res)

    def test_process_matrix_2(self):
        matrix_str = """Result matrix: 
 [[2 2 9 9 9]
 [2 2 9 9 9]
 [2 2 9 9 9]
 [4 4 2 4 4]
 [4 4 2 4 4]]"""
        exp = [['2', '2', '9', '9', '9'], ['2', '2', '9', '9', '9'], ['2', '2', '9', '9', '9'], ['4', '4', '2', '4', '4'], ['4', '4', '2', '4', '4']]
        res = process_res_matrix(matrix_str)
        self.assertEqual(exp, res)

    def test_get_dict_1(self):
        mt = [['2', '2'], ['2', '2']]
        exp = {(0, 0): ('2', 'blue'), (0, 1): ('2', 'blue'), (1, 0): ('2', 'coral1'), (1, 1): ('2', 'coral1')}
        res = get_matrix_with_color(mt, 1, 2, 2)
        self.assertEqual(exp, res)

    def test_get_dict21(self):
        mt = [['2', '2'], ['2', '2']]
        exp = {(0, 0): ('2', 'blue'), (1, 0): ('2', 'blue'), (0, 1): ('2', 'coral1'), (1, 1): ('2', 'coral1')}
        res = get_matrix_with_color(mt, 2, 2, 2)
        self.assertEqual(exp, res)

    def test_get_count_1(self):
        raw = [['1', '1', '3'], ['2', '0', '0'], ['0', '2', '0']]
        arr = [['1', '1', '3'], ['2', '2', '3'], ['2', '2', '3']]
        exp = 2
        res = get_count_solutions(arr, raw)
        self.assertEqual(exp, res)

    def test_get_count_2(self):
        raw = [['1', '1', '3'], ['2', '0', '0'], ['2', '0', '0']]
        arr = [['1', '1', '3'], ['2', '2', '3'], ['2', '2', '3']]
        exp = 1
        res = get_count_solutions(arr, raw)
        self.assertEqual(exp, res)
