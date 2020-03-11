#!/usr/bin/python -i
# -*- coding: utf-8 -*-
from tkinter import *
from get_dict_with_values import get_matrix_with_color
"""Модуль, рисующий решение головоломки с характерной раскраской"""


def get_all_colorings(mt, count):
    solutions = []
    for i in range(1, count+1):
        solutions.append(get_matrix_with_color(mt, i, len(mt), len(mt[0])))
    return solutions


def create_matrix_buttons(count, mt):
    solutions = get_all_colorings(mt, count)
    top = Tk()
    top.title('solution')
    canvas = Canvas(top, height=len(mt) * 50, width=len(mt) * 50)
    set_buttons(mt, solutions[0], top, canvas)
    x = 0
    for i in range(len(solutions)):
        set_switch_button(i, x, str(i+1), top, mt, solutions, canvas)
        x += 52
    canvas.pack(side='top')
    top.mainloop()


def set_switch_button(i, x, title, top, mt, solutions, canvas):
    b = Button(top, text='#'+title, justify='center', command=lambda: set_buttons(mt, solutions[i], top, canvas))
    b.place(x=x, y=100, height=25, width=50)


def set_buttons(mt, matrix_value, top, canvas):
    canvas.delete(ALL)
    for col in range(len(mt)):
        for row in range(len(mt[0])):
            key = (col, row)
            val = matrix_value[key][0]
            co = matrix_value[key][1]
            button_row_col = Button(top, text=val, highlightbackground=co, disabledforeground='black', state=DISABLED)
            button_row_col.place(x=row * 30, y=col * 30)
