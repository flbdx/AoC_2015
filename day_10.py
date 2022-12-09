#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""111221
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_10"]

def expand(line):
    r = ""
    iter_line = iter(line)
    c = next(iter_line)
    while True:
        n = 1
        try:
            while (cc := next(iter_line)) == c:
                n += 1
        except:
            r += repr(n) + c
            break
        r += repr(n) + c
        c = cc
    return r

def work_p1(inputs):
    line = next(iter(inputs)).strip()
    for i in range(40):
        line = expand(line)
    return len(line)

def work_p2(inputs):
    line = next(iter(inputs)).strip()
    for i in range(50):
        line = expand(line)
    return len(line)

def test_p1():
    assert(expand("111221") == "312211")
test_p1()

def p1():
    with fileinput.input() as inputs:
        print(work_p1(inputs))
p1()

def p2():
    with fileinput.input() as inputs:
        print(work_p2(inputs))
p2()
