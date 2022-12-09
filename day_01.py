#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_01"]

def work_p1(inputs):
    ret = 0
    line = next(iter(inputs)).strip()
    for c in line:
        ret += 1 if c == '(' else -1
    return ret

def work_p2(inputs):
    ret = 0
    floor = 0
    line = next(iter(inputs)).strip()
    for c in line:
        ret += 1
        floor += 1 if c == '(' else -1
        if floor < 0:
            return ret

def p1():
    with fileinput.input() as inputs:
        print(work_p1(inputs))
p1()

def p2():
    with fileinput.input() as inputs:
        print(work_p2(inputs))
p2()
