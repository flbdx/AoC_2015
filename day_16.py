#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

MFCSAM={"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,\
    "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2,"perfumes": 1}

if len(sys.argv) == 1:
    sys.argv += ["input_16"]

def parse_input(inputs):
    sues = {}
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        sep = line.find(":")
        n = int(line[:sep].split(" ")[1])
        attributes = line[sep+2:].split(", ")
        sue = {}
        for att in attributes:
            k, v = att.split(": ")
            sue[k] = int(v)
        sues[n] = sue
    return sues

def work_p1(inputs):
    sues = parse_input(inputs)
    
    def is_compatible(sue):
        for k, v in MFCSAM.items():
            if sue.get(k, v) != v:
                return False
        return True
    
    for n, sue in sues.items():
        if is_compatible(sue):
            return n

def work_p2(inputs):
    sues = parse_input(inputs)
    
    def is_compatible(sue):
        for k in ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"]:
            v = MFCSAM[k]
            v2 = sue.get(k, None)
            if v2 != None and v2 != v:
                return False
        for k in ["cats", "trees"]:
            v = MFCSAM[k]
            v2 = sue.get(k, None)
            if v2 != None and v2 <= v:
                return False
        for k in ["pomeranians", "goldfish"]:
            v = MFCSAM[k]
            v2 = sue.get(k, None)
            if v2 != None and v2 >= v:
                return False
        return True
    
    for n, sue in sues.items():
        if is_compatible(sue):
            return n

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
