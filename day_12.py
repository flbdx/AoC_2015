#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re
import json

if len(sys.argv) == 1:
    sys.argv += ["input_12"]

def work_p1(inputs):
    ret = 0
    re_int = re.compile("[-]?[0-9]+")

    return sum(map(lambda l : sum(map(int, re_int.findall(l.strip()))), inputs))

def work_p2(inputs):
    def count(obj):
        if type(obj) == dict:
            s = 0
            for k, e in obj.items():
                if e == "red":
                    return 0
                s += count(e)
            return s
        elif type(obj) == list:
            return sum(map(count, obj))
        elif type(obj) == int:
            return obj
        else:
            return 0  
    
    return sum(map(lambda l : count(json.loads(l.strip())), inputs))

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
