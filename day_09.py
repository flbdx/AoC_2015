#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re

test_input="""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_09"]

def parse(inputs):
    re_line = re.compile("([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)")
    cities = set()
    weights = {}
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        match = re_line.fullmatch(line)
        c1, c2, w = match.group(1), match.group(2), int(match.group(3))
        cities.add(c1)
        cities.add(c2)
        weights[(c1, c2)] = w
        weights[(c2, c1)] = w
    
    cities = list(cities)
    
    return (cities, weights)

def work_p1(inputs):
    cities, weights = parse(inputs)

    best = sum(weights.values(), 0)
    
    stack = []
    for i in range(len(cities)):
        stack.append(([cities[i]], cities[0:i]+cities[i+1:], 0))
    while len(stack) != 0:
        t = stack.pop(0)
        if len(t[1]) == 0:
            best = t[2] if t[2] < best else best
        else:
            if t[2] > best:
                continue
            for i in range(0, len(t[1])):
                last_city = t[0][-1]
                next_city = t[1][i]
                stack.append((t[0] + [next_city], t[1][:i] + t[1][i+1:], t[2] + weights[(last_city, next_city)]))
    return best

def work_p2(inputs):
    cities, weights = parse(inputs)

    best = 0
    
    stack = []
    for i in range(len(cities)):
        stack.append(([cities[i]], cities[0:i]+cities[i+1:], 0))
    while len(stack) != 0:
        t = stack.pop(0)
        if len(t[1]) == 0:
            best = t[2] if t[2] > best else best
        else:
            for i in range(0, len(t[1])):
                last_city = t[0][-1]
                next_city = t[1][i]
                stack.append((t[0] + [next_city], t[1][:i] + t[1][i+1:], t[2] + weights[(last_city, next_city)]))
    return best

def test_p1():
    assert(work_p1(test_input) == 605)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input) == 982)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
