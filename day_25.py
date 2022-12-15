#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re

test_input=(5, 6)

if len(sys.argv) == 1:
    sys.argv += ["input_25"]

with fileinput.input() as inputs:
    real_input = tuple(int(n) for n in re.findall("(-?[0-9]+)", next(iter(inputs)).strip()))

def work_p1(inputs):
    row, column = inputs

    rng = lambda v: (v*252533) % 33554393

    # the starting row from the diagonal of the required point
    srow = row + column - 1
    # the sequence number for the starting point of the row
    n = 1
    for i in range(1, srow+1):
        n += i-1
    # the sequence number of the required point
    n += column - 1

    # the PRNG seems to have a period of 16777196
    n %= 16777196

    # print((row, column, srow, n))
    v = 20151125
    for i in range(n-1):
        v = rng(v)
    return v

def work_p2(inputs):
    pass

def test_p1():
    assert(work_p1(test_input) == 31663883)
test_p1()

def p1():
    print(work_p1(real_input))
p1()
