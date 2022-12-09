#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re
import itertools

test_input="""Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_13"]

def parse_input(inputs):
    relationships = {}
    folks = set()
    re_line = re.compile("([a-zA-Z]+) would ([a-zA-Z]+) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+).")
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        m = re_line.fullmatch(line)
        v = int(m.group(3))
        if m.group(2) == "lose":
            v = -v
        relationships[(m.group(1), m.group(4))] = v
        folks.add(m.group(1))
    return relationships, folks

def work(relationships, folks):
    # head is a fixed position on the table. No need to turn the table N times...
    head, folks = folks[0:1], folks[1:]
    
    def score(perm):
        r = 0
        perm = head + list(perm)
        l = len(perm)
        for i in range(l):
            r += relationships[(perm[i], perm[(i+1)%l])]
            r += relationships[(perm[i], perm[(i-1)%l])]
        return r
    
    best = 0
    for perm in itertools.permutations(folks):
        s = score(perm)
        best = max(best, s)
    return best

def work_p1(inputs):
    relationships, folks = parse_input(inputs)
    folks = list(folks)
    return work(relationships, folks)

def work_p2(inputs):
    relationships, folks = parse_input(inputs)
    folks = list(folks)
    for f in folks:
        relationships[("ME", f)] = 0    # So transparent...
        relationships[(f, "ME")] = 0    # Maybe a ghost?
    
    return work(relationships, ["ME"] + folks)

def test_p1():
    assert(work_p1(test_input) == 330)
test_p1()

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
