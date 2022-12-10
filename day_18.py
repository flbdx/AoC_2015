#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input=""".#.#.#
...##.
#....#
..#...
#.#..#
####..
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_18"]

def read_grid(inputs):
    grid = {}
    width = 0
    height = 0
    for y, line in enumerate(inputs):
        line = line.strip()
        if len(line) == 0:
            break
        height += 1
        width = len(line)
        for x, c in enumerate(line.strip()):
            if c == '#':
                grid[complex(x,y)] = 1
    return grid, width, height

def read_grid(inputs):
    grid = {}
    width = 0
    height = 0
    for y, line in enumerate(inputs):
        line = line.strip()
        if len(line) == 0:
            break
        height += 1
        width = len(line)
        for x, c in enumerate(line.strip()):
            grid[complex(x,y)] = 1 if c == '#' else 0
    return grid, width, height

neighs = [-1-1j, 0-1j, 1-1j,\
          -1+0j,       1+0j,\
          -1+1j, 0+1j, 1+1j]

def work_p1(inputs, steps):
    grid, width, height = read_grid(inputs)
    
    def neighbours(c):
        d = [grid.get(c + n, 0) for n in neighs]
        return d
    
    
    for s in range(steps):
        ngrid = {}
        for y in range(height):
            for x in range(width):
                c = complex(x,y)
                n = sum(neighbours(c))
                if (grid.get(c, 0) and n in [2,3]) or n == 3:
                    ngrid[c] = 1
        grid = ngrid
        
    return len(grid)

def work_p2(inputs, steps):
    grid, width, height = read_grid(inputs)
    
    def neighbours(c):
        d = [grid.get(c + n, 0) for n in neighs]
        return d
    
    corners = [complex(0,0), complex(0, height-1), complex(width-1, 0), complex(width-1, height-1)]
    
    for c in corners:
        grid[c] = 1
    
    for s in range(steps):
        ngrid = {}
        for y in range(height):
            for x in range(width):
                c = complex(x,y)
                n = sum(neighbours(c))
                if c in corners or (grid.get(c, 0) and n in [2,3]) or n == 3:
                    ngrid[c] = 1
        grid = ngrid
        
    return len(grid)

def test_p1():
    assert(work_p1(test_input, 4) == 4)
test_p1()

def p1():
    print(work_p1(fileinput.input(), 100))
p1()

def test_p2():
    assert(work_p2(test_input, 5) == 17)
test_p2()

def p2():
    print(work_p2(fileinput.input(), 100))
p2()
