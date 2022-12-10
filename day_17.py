#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys

test_input="""20
15
10
5
5
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_17"]

class Container(object):
    def __init__(self, c, uniq):
        self.c = c
        self.uniq = uniq    # the problem requires us to uniquely identify each container
    def __repr__(self):
        return repr(self.c)

def work(inputs, target, part2 = False):
    containers = set()
    uniq = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        containers.add(Container(int(line), uniq))
        uniq += 1
        
    cache = set()
    def gen(used_containers, available_containers, rem):
        if rem == 0:
            yield used_containers
        else:
            for c in available_containers:
                if c.c <= rem:
                    nxt = used_containers | {c}
                    cache_entry = tuple(sorted([e.uniq for e in nxt]))  # something hashable
                    if not cache_entry in cache:
                        cache.add(cache_entry)
                        for seq in gen(nxt, available_containers - {c}, rem - c.c):
                            yield seq

    if not part2:
        ret = 0
        for p in gen(set(), containers, target):
            ret += 1
        return ret
    else:
        counts = {}
        min_len = len(containers)
        for p in gen(set(), containers, target):
            l = len(list(p))
            counts[l] = counts.setdefault(l, 0) + 1
            if l < min_len:
                min_len = l
        return counts[min_len]

def test_p1():
    assert(work(test_input, 25) == 4)
test_p1()

def p1():
    print(work(fileinput.input(), 150))
p1()

def test_p2():
    assert(work(test_input, 25, True) == 3)
test_p2()

def p2():
    print(work(fileinput.input(), 150, True))
p2()
