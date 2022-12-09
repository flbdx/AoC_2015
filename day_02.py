#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re

test_input="""2x3x4
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_02"]

def work_p1(inputs):
    re_int = re.compile("[0-9]+")
    ret = 0
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        dims = list(map(int, re_int.findall(line)))
        surfaces = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
        ret += sum(map(lambda x : x*2, surfaces), 0) + min(surfaces)
    return ret
    

def work_p2(inputs):
    re_int = re.compile("[0-9]+")
    ret = 0
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        dims = list(map(int, re_int.findall(line)))
        perimeters = [2 * (dims[0] + dims[1]), 2 * (dims[0] + dims[2]), 2 * (dims[1] + dims[2])]
        ret += min(perimeters) + dims[0]*dims[1]*dims[2]
    return ret

def test_p1():
    assert(work_p1(test_input) == 58)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input) == 34)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
