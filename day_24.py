#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""1
2
3
4
5
7
8
9
10
11
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_24"]

def gen_target(target, packages, get_max_len):
    stack = [([], 0, packages)]
    while len(stack) != 0:
        group, v, rem = stack.pop(0)
        if len(group) >= get_max_len():
            break
        for i in range(len(rem)):
            n = rem[i]
            if len(group) > 0 and n < group[-1]:
                continue
            v2 = v + n
            if v2 > target:
                break
            elif v2 == target:
                yield (group + [n], v2, rem[0:i] + rem[i+1:])
            else:
                stack.append((group + [n], v2, rem[0:i] + rem[i+1:]))

def work_p1(inputs):
    packages = []
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        packages.append(int(line))
    
    target = sum(packages) // 3
    
    best_len = len(packages) + 1
    best_qe = None
    get_max_len = lambda: best_len
    for t1 in gen_target(target, packages, get_max_len):
        l = len(t1[0])
        if l > best_len:
            continue
        qe = 1
        for p in t1[0]:
            qe *= p
        if best_qe != None and qe > best_qe:
            continue
        for t2 in gen_target(target, t1[2], lambda: len(packages)+1):
            t3 = t2[2]
            if sum(t3) != target:
                continue
            
            if l < best_len:
                print(t1[0], t2[0], t3, qe)
                best_len = l
                best_qe = qe
            elif l == best_len and qe < best_qe:
                print(t1[0], t2[0], t3, qe)
                best_qe = qe
            break
    return best_qe

def work_p2(inputs):
    packages = []
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        packages.append(int(line))
    
    target = sum(packages) // 4
    
    best_len = len(packages) + 1
    best_qe = None
    get_max_len = lambda: best_len
    for t1 in gen_target(target, packages, get_max_len):
        l = len(t1[0])
        if l > best_len:
            continue
        qe = 1
        for p in t1[0]:
            qe *= p
        if best_qe != None and qe > best_qe:
            continue
        for t2 in gen_target(target, t1[2], lambda: len(packages)+1):
            found = False
            for t3 in gen_target(target, t2[2], lambda: len(packages)+1):
                t4 = t3[2]
                if sum(t4) != target:
                    continue
                
                if l < best_len:
                    print(t1[0], t2[0], t3[0], t4, qe)
                    best_len = l
                    best_qe = qe
                elif l == best_len and qe < best_qe:
                    print(t1[0], t2[0], t3[0], t4, qe)
                    best_qe = qe
                found = True
                break
            if found:
                break
    return best_qe

def test_p1():
    assert(work_p1(test_input) == 99)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input) == 44)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
