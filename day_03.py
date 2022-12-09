#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""^>v<
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_03"]

def work_p1(inputs):
    houses = {(0, 0)}
    pos = [0, 0]
    for line in inputs:
        line = line.strip()
        for c in line:
            pos[0] += 1 if c == '>' else -1 if c == '<' else 0
            pos[1] += 1 if c == '^' else -1 if c == 'v' else 0
            houses.add(tuple(pos))
        return len(houses)

def work_p2(inputs):
    houses = {(0, 0)}
    pos1 = [0, 0]
    pos2 = [0, 0]
    for line in inputs:
        line = line.strip()
        it = iter(line)
        try:
            while True:
                c = next(it)
                pos1[0] += 1 if c == '>' else -1 if c == '<' else 0
                pos1[1] += 1 if c == '^' else -1 if c == 'v' else 0
                houses.add(tuple(pos1))
                c = next(it)
                pos2[0] += 1 if c == '>' else -1 if c == '<' else 0
                pos2[1] += 1 if c == '^' else -1 if c == 'v' else 0
                houses.add(tuple(pos2))
        except:
            return len(houses)

def test_p1():
    assert(work_p1(test_input) == 4)
test_p1()

def p1():
    with fileinput.input() as inputs:
        print(work_p1(inputs))
p1()

def test_p2():
    assert(work_p2(test_input) == 3)
test_p2()

def p2():
    with fileinput.input() as inputs:
        print(work_p2(inputs))
p2()
