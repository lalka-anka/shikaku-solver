from tkinter import *
import numpy as np
from solver import return_result_matrix
from get_count_solutions import get_count_solutions
from process_str_matrix import process_res_matrix
from create_color_matrix import create_matrix_buttons
from process_not_square_mat import create_square_field
from process_not_square_mat import back_to_orig
"""Модуль, отвечающий за отрисовку поля и вывод решения"""

ENTRIES = []


def initialize(arr, length, width):
    res_matrix = []
    ent = ENTRIES[0]
    m = 1
    row = []
    for i in range(width):
        for j in range(length):
            if not ent.get():
                arr[i][j] = 0
            else:
                arr[i][j] = int(ent.get())
            row.append(arr[i][j])
            if len(row) == width:
                res_matrix.append(row.copy())
                row.clear()
            if m <= length * width-1:
                ent = ENTRIES[m]
                m += 1
    return res_matrix


def print_cells(arr, length, width):
    clean_state()
    ent = ENTRIES[0]
    m = 1
    for i in range(length):
        for j in range(width):
            ent.insert(1, arr[i][j])
            if m <= length * width - 1:
                ent = ENTRIES[m]
                m += 1


def solve(arr, top, size, length, width):
    raw_matrix = initialize(arr, length, width)

    if length != width:
        new_mat, key = create_square_field(length, width, raw_matrix)
        new_mat = np.array(new_mat)

        res_matrix = return_result_matrix(new_mat)
        if res_matrix is not None:
            res_matrix = process_res_matrix(res_matrix)
            res_matrix = back_to_orig(res_matrix, key)
            print_cells(res_matrix, length, width)

            count = get_count_solutions(res_matrix, raw_matrix)
            result = 'solutions: ' + str(count)
            create_buttons_dec(top, result, size)
            create_matrix_buttons(count, res_matrix)
        else:
            result = 'No solution found'
            create_buttons_dec(top, result, size)
    else:
        res_matrix = return_result_matrix(np.array(raw_matrix))
        if res_matrix is not None:
            result_matrix = process_res_matrix(res_matrix)
            print_cells(result_matrix, length, width)
            count = get_count_solutions(result_matrix, raw_matrix)
            result = 'solutions: ' + str(count)
            create_buttons_dec(top, result, size)
            create_matrix_buttons(count, result_matrix)

    #else:
     #   result = 'No solution found'
      #  create_buttons_dec(top, result, size)


def create_gui(length, width, cells):
    top = Tk()
    coord = max(length, width)
    if coord < 5:
        coord = 5
    size = 64 * coord
    top.title('Shikaku Solver')
    canvas = Canvas(top, height=size / 1.5, width=size / 1.5)
    create(top, length, width)
    create_buttons(top, size, cells, length, width)
    canvas.pack(side='top')
    top.mainloop()


def create_buttons(top, size, cells, length, width):
    button_solve = Button(top, text='solve', justify='left', default='active', command=lambda: solve(cells, top, size, length, width))
    button_reset = Button(top, text='reset', justify='center', command=lambda: clean_state())
    y_coordinate = size - (size / 2)
    button_solve.place(x=35, y=y_coordinate, height=30, width=60)
    button_reset.place(x=100, y=y_coordinate, height=30, width=60)


def create_buttons_dec(top, count, size):
    button_count = Button(top, text=count, justify='right')
    y_coordinate = size - (size / 2)
    button_count.place(x=35, y=y_coordinate + 40, height=30, width=120)


def clean_state():
    for e in ENTRIES:
        e.delete(0, END)


def create(top, length, width):
    p, q = 41, 41
    for i in range(length):
        for j in range(width):
            ent = Entry(top, width=2, font='BOLD')
            ent.grid(row=i, column=j)
            ent.place(x=p, y=q, height=20, width=20)
            ENTRIES.append(ent)
            p += 30.0
        q += 24.5
        p = 41


def get_gui(length, width):
    """Метод, возвращающий gui"""
    cells = [[0 for x in range(length)] for y in range(width)]
    create_gui(length, width, cells)
