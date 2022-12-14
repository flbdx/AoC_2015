#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""inc a
jio a, +2
tpl a
inc a
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_23"]

# inc r     r +=  1
# hlf r     r //= 2 
# tpl r     r *=  3
# jmp i     ip += i
# jie r,i   ip += i si (r&1) == 0
# jio r,i   ip += i si r == 1

class Computer(object):
    def __init__(self):
        self.instrs = []
        self.ip = 0
        self.regs = {"a":0, "b":0}
    
    def set_code(self, lines):
        parse_int = lambda a: a if a.isalpha() else int(a)
        self.instrs = []
        
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            idx = line.index(" ")
            i, ops = line[:idx], line[idx+1:]
            i = Computer.__dict__["op_" + i]
            ops = list(map(parse_int, ops.split(", ")))
            self.instrs.append((i, ops))
    
    def reset(self):
        self.ip = 0
        self.regs = {"a":0, "b":0}   

    def op_inc(self, ops):
        self.regs[ops[0]] += 1
        return 1
    def op_hlf(self, ops):
        self.regs[ops[0]] //= 2
        return 1
    def op_tpl(self, ops):
        self.regs[ops[0]] *= 3
        return 1
    def op_jmp(self, ops):
        return ops[0]
    def op_jie(self, ops):
        if (self.regs[ops[0]] & 1) == 0:
            return ops[1]
        else:
            return 1
    def op_jio(self, ops):
        if self.regs[ops[0]] == 1:
            return ops[1]
        else:
            return 1
    
    def step(self):
        if self.ip >= len(self.instrs):
            return False
        i, ops = self.instrs[self.ip]
        self.ip += i(self, ops)
        return self.ip < len(self.instrs)
    
    def run(self):
        while self.step():
            pass
        

def work_p1(inputs):
    c = Computer()
    c.set_code(inputs)
    c.run()
    
    return c.regs["b"]

def work_p2(inputs):
    c = Computer()
    c.regs["a"] = 1
    c.set_code(inputs)
    c.run()
    
    return c.regs["b"]

def test_p1():
    assert(work_p1(test_input) == 0)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def test_p2():
    assert(work_p2(test_input) == 0)
test_p2()

def p2():
    print(work_p2(fileinput.input()))
p2()
