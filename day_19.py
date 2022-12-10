#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_19"]

def parse_input(inputs):
    it = iter(inputs)
    replacements = {}
    while True:
        line = next(it)
        line = line.strip()
        if len(line) == 0:
            break
        f, t = line.split(" => ")
        replacements[f] = replacements.get(f, []) + [t]
    seed = next(it).strip()
    return (replacements, seed)

def work_p1(inputs):
    repl, seed = parse_input(inputs)
    products = set()
    
    for needle in repl:
        idx = 0
        l = len(needle)
        while (idx := seed.find(needle, idx)) != -1:
            for r in repl[needle]:
                s = seed[:idx] + r + seed[idx+l:]
                products.add(s)
            idx += 1
    return len(products)

def work_p2(inputs):
    repl, target = parse_input(inputs)
    repl_inv = {}
    for r, l in repl.items():
        for m in l:
            repl_inv[m] = r            
    
    def possible_replacements(molecule):
        d = set()
        for needle in repl_inv:
            idx, l = (0, len(needle))
            r = repl_inv[needle]
            if r == "e" and l != len(molecule):
                continue
            while (idx := molecule.find(needle, idx)) != -1:
                d.add(molecule[:idx] + r + molecule[idx+l:])
                idx += 1
        return list(d)
    
    cache = set()
    stack = [(r, 1) for r in possible_replacements(target)]
    stack = sorted(stack, key=lambda e : len(e[0]))
    while True:
        r, step = stack.pop(0)
        d = possible_replacements(r)
        if len(d) == 0:
            continue
        elif len(d) == 1 and d[0] == "e":
            return step + 1
        else:
            d2 = []
            for t in [(r, step+1) for r in d]:
                if not t[0] in cache:
                    cache.add(t[0])
                    d2.append(t)
            stack = d2 + stack
            stack = sorted(stack, key=lambda e : len(e[0]))        
    
    return None
    

def test_p1():
    assert(work_p1(test_input) == 7)
test_p1()

def p1():
    with fileinput.input() as inputs:
        print(work_p1(inputs))
p1()

def test_p2():
    assert(work_p2(test_input) == 6)
test_p2()

def p2():
    with fileinput.input() as inputs:
        print(work_p2(inputs))
p2()
