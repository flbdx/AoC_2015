#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""""
"abc"
"aaa\\"aaa"
"\\x27"
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_08"]

def unescaped_len(line):
    r = 0
    escaped = False
    i = 0
    while i < len(line):
        c = line[i]
        if not escaped:
            if c == '\\':
                escaped = True
            else:
                r += 1
            i += 1
        else:
            if c == '"' or c == '\\':
                r += 1
                escaped = False
                i += 1
            else:
                try:
                    c = chr(int("0" + line[i:i+3], 16))
                    r += 1
                    escaped = False
                    i += 3
                except:
                    r += 1
                    escaped = False
                    i += 1
                    
    return r - 2

def work_p1(inputs):
    ret = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        l = unescaped_len(line)
        ret += len(line) - l
    return ret

def work_p2(inputs):
    ret = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        escaped_len = 2
        for c in line:
            if c == '"' or c == '\\':
                escaped_len += 2
            else:
                escaped_len += 1
        ret += escaped_len - len(line)
    return ret

def test_p1():
    assert(work_p1(test_input) == 12)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input) == 19)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
