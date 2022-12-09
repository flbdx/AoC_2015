#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input_p1="""ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
""".splitlines()

test_input_p2="""qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_05"]

def is_nice_p1(string):
    n_vowels = 0
    seq2 = False
    for c in string:
        if c in "aeiou":
            n_vowels += 1
            if n_vowels == 3:
                break
    if n_vowels < 3:
        return False
    for p in range(len(string) - 1):
        if string[p] == string[p+1]:
            seq2 = True
            break
    if not seq2:
        return False
    for seq in ["ab", "cd", "pq", "xy"]:
        if seq in string:
            return False
    return True

def is_nice_p2(string):
    got_pair = False
    got_triple = False
    for p in range(len(string) - 3):
        pair = string[p:p+2]
        for p2 in range(p+2, len(string) - 1):
            if pair == string[p2:p2+2]:
                got_pair = True
                break
        if got_pair:
            break
    if not got_pair:
        return False
    
    for p in range(len(string) - 2):
        if string[p] == string[p+2]:
            got_triple = True
            break
    if not got_triple:
        return False
    
    return True

def work_p1(inputs):
    ret = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            break
        if is_nice_p1(line):
            ret += 1
    return ret

def work_p2(inputs):
    ret = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            break
        b = is_nice_p2(line)
        if b:
            ret += 1
    return ret

def test_p1():
    assert(work_p1(test_input_p1) == 2)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input_p2) == 2)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
