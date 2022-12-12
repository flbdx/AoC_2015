#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""150
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_20"]

test_input=int(next(iter(test_input)))
real_input=int(next(iter(fileinput.input())))

# it's not cute, but I guess it works
def all_factors(n):
    factors = all_factors.cache.get(n, [1])
    n_ = n
    if len(factors) > 1:
        return factors
    i = 2
    while i * i <= n:
        if n %i :
            i += 1
        else:
            n //= i
            factors.append(i)
            factors += list(i*e for e in all_factors(n))
    if n > 1:
        factors.append(n)
    factors = sorted(list(set(factors)))
    all_factors.cache[n_] = factors
    return factors
all_factors.cache = {}
    

def work_p1(target):
    n = 1
    while True:
        v = sum(all_factors(n))
        if v >= target // 10:
            return n
        n += 1

def work_p2(target):
    n = 1
    while True:
        v = sum(i for i in all_factors(n) if i*50 >= n)
        if v * 11 >= target:
            return n
        n += 1

def test_p1():
    assert(work_p1(test_input) == 8)
test_p1()

def p1():
    print(work_p1(real_input))
p1()

def p2():
    print(work_p2(real_input))
p2()
