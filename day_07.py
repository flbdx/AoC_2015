#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re
from abc import ABC, abstractmethod

class Source(ABC):
    @abstractmethod
    def value(self):
        return None

class Source_Int(Source):
    def __init__(self, v):
        self.v = v
    def value(self):
        return self.v

class Wire(Source):
    def __init__(self, source):
        self.source = source
        self.cache = None
    def set_source(self, source):
        self.source = source
    def value(self):
        if not self.cache:
            self.cache = self.source.value()
        return self.cache

class Gate_AND(Source):
    def __init__(self, source1, source2):
        self.source1 = source1
        self.source2 = source2
    def value(self):
        return self.source1.value() & self.source2.value()

class Gate_OR(Source):
    def __init__(self, source1, source2):
        self.source1 = source1
        self.source2 = source2
    def value(self):
        return self.source1.value() | self.source2.value()

class Gate_LSHIFT(Source):
    def __init__(self, source1, n):
        self.source1 = source1
        self.n = n
    def value(self):
        return (self.source1.value() << self.n) & 0xFFFF

class Gate_RSHIFT(Source):
    def __init__(self, source1, n):
        self.source1 = source1
        self.n = n
    def value(self):
        return (self.source1.value() >> self.n) & 0xFFFF

class Gate_NOT(Source):
    def __init__(self, source1):
        self.source1 = source1
    def value(self):
        return self.source1.value() ^ 0xFFFF

if len(sys.argv) == 1:
    sys.argv += ["input_07"]

def parse_inputs(inputs):
    wires = {}
    
    re_and = re.compile("([a-z0-9]+) AND ([a-z0-9]+) -> ([a-z]+)")
    re_or = re.compile("([a-z0-9]+) OR ([a-z0-9]+) -> ([a-z]+)")
    re_not = re.compile("NOT ([a-z0-9]+) -> ([a-z]+)")
    re_rshift = re.compile("([a-z0-9]+) RSHIFT ([0-9]+) -> ([a-z]+)")
    re_lshift = re.compile("([a-z0-9]+) LSHIFT ([0-9]+) -> ([a-z]+)")
    re_connect = re.compile("([a-z0-9]+) -> ([a-z]+)")
    
    def source_from_operand(name):
        if name.isdecimal():
            return Source_Int(int(name))
        return wires.setdefault(name, Wire(None))
    def wire_from_dest(name):
        return wires.setdefault(name, Wire(None))
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        
        if match := re_and.fullmatch(line):             # S1 AND S2 -> D
            s1 = source_from_operand(match.group(1))
            s2 = source_from_operand(match.group(2))
            d = wire_from_dest(match.group(3))
            d.set_source(Gate_AND(s1, s2))
        elif match := re_or.fullmatch(line):            # S1 OR S2 -> D
            s1 = source_from_operand(match.group(1))
            s2 = source_from_operand(match.group(2))
            d = wire_from_dest(match.group(3))
            d.set_source(Gate_OR(s1, s2))
        elif match := re_not.fullmatch(line):           # NOT S1 -> D
            s1 = source_from_operand(match.group(1))
            d = wire_from_dest(match.group(2))
            d.set_source(Gate_NOT(s1))
        elif match := re_rshift.fullmatch(line):        # S1 RSHIFT N -> D
            s1 = source_from_operand(match.group(1))
            n = int(match.group(2))
            d = wire_from_dest(match.group(3))
            d.set_source(Gate_RSHIFT(s1, n))
        elif match := re_lshift.fullmatch(line):        # S1 LSHIFT N -> D
            s1 = source_from_operand(match.group(1))
            n = int(match.group(2))
            d = wire_from_dest(match.group(3))
            d.set_source(Gate_LSHIFT(s1, n))
        elif match := re_connect.fullmatch(line):       # S1 -> D
            s1 = source_from_operand(match.group(1))
            d = wire_from_dest(match.group(2))
            d.set_source(s1)
        else:
            raise Exception(line)
    return wires

def work_p1(inputs):
    wires = parse_inputs(inputs)
    return wires["a"].value()

def work_p2(inputs):
    wires = parse_inputs(inputs)
    va = wires["a"].value()
    wires["b"].set_source(Source_Int(va))
    for n, w in wires.items():
        wires[n].cache = None
    return wires["a"].value()

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
