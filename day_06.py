#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re

if len(sys.argv) == 1:
    sys.argv += ["input_06"]

def work_p1(inputs):
    re_int = re.compile("[0-9]+")
    grid = set()
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            break
        numbers = list(map(int, re_int.findall(line)))
        corner1 = (numbers[0], numbers[1])
        corner2 = (numbers[2], numbers[3])
        def turn_on(x,y):
            grid.add((x,y))
        def turn_off(x,y):
            if (x,y) in grid:
                grid.remove((x,y))
        def toggle(x,y):
            if (x,y) in grid:
                grid.remove((x,y))
            else:
                grid.add((x,y))
        if "on" in line:
            op = turn_on
        elif "off" in line:
            op = turn_off
        else:
            op = toggle
        for x in range(corner1[0], corner2[0]+1):
            for y in range(corner1[1], corner2[1] + 1):
                op(x,y)
    return len(grid)

def work_p2(inputs):
    re_int = re.compile("[0-9]+")
    grid = {}
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            break
        numbers = list(map(int, re_int.findall(line)))
        corner1 = (numbers[0], numbers[1])
        corner2 = (numbers[2], numbers[3])
        def turn_on(x,y):
            grid[(x,y)] = grid.setdefault((x,y), 0) + 1
        def turn_off(x,y):
            grid[(x,y)] = grid.setdefault((x,y), 0) - 1
            if grid[(x,y)] <= 0:
                    del grid[(x,y)]
        def toggle(x,y):
            grid[(x,y)] = grid.setdefault((x,y), 0) + 2
        if "on" in line:
            op = turn_on
        elif "off" in line:
            op = turn_off
        else:
            op = toggle
        for x in range(corner1[0], corner2[0]+1):
            for y in range(corner1[1], corner2[1] + 1):
                op(x,y)
    return sum(grid.values(), 0)

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
