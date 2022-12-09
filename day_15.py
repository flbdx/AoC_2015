#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re
from collections import namedtuple

test_input="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_15"]

Ingredient = namedtuple("Ingredient", ["name", "capacity", "durability", "flavor", "texture", "calories"])

def parse_input(inputs):
    ingredients = {}
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        m = re.fullmatch("([A-Za-z]+): capacity ([-]?[0-9]+), durability ([-]?[0-9]+), flavor ([-]?[0-9]+), texture ([-]?[0-9]+), calories ([-]?[0-9]+)", line)
        ingredients[m.group(1)] = Ingredient(m.group(1), *map(int, m.groups()[1:]))
    return ingredients

def work(inputs, part_2 = False):
    ingredients = parse_input(inputs)
    
    n_ingredients = len(ingredients)
    
    start_amounts = [0 for i in range(n_ingredients)]
    start_rem = 100
    
    # recursive generator for all the ingredient amounts combinations
    def gen(amounts, n, rem):
        if n == 1:
            yield amounts + [rem]
        else:
            for i in range(rem+1):
                a = amounts + [i]
                for s in gen(a, n-1, rem - i):
                    yield s
    
    if not part_2:
        def score(perm):
            ret = 1
            for metric in ["capacity", "durability", "flavor", "texture"]:
                s = 0
                for r, n in zip(ingredients, perm):
                    s += ingredients[r].__getattribute__(metric) * n
                if s <= 0:
                    return 0
                ret *= s
            return ret
    else:
        def score(perm):
            s = 0
            for r, n in zip(ingredients, perm):
                s += ingredients[r].calories * n
            if s != 500:
                return 0
            ret = 1
            for metric in ["capacity", "durability", "flavor", "texture"]:
                s = 0
                for r, n in zip(ingredients, perm):
                    s += ingredients[r].__getattribute__(metric) * n
                ret *= max(s, 0)
            return ret

    return max(map(score, gen([], n_ingredients, 100)))

def test_p1():
    assert(work(test_input) == 62842880)
test_p1()

def p1():
    print(work(fileinput.input()))
p1()

def test_p2():
    assert(work(test_input, True) == 57600000)
test_p2()

def p2():
    print(work(fileinput.input(), True))
p2()
