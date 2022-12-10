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
    containers = []
    uniq = 0
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        containers.append(Container(int(line), uniq))
        uniq += 1
        
    cache = set()
    def gen(used_containers, total, available_containers, rem):
        if rem == 0:
            yield used_containers
        elif rem > 0:
            for c in available_containers:
                if c.c <= rem:
                    nxt = used_containers | {c}
                    cache_entry = tuple(sorted([e.uniq for e in nxt]))  # something hashable
                    if cache_entry in cache:
                        continue
                    cache.add(cache_entry)
                    for seq in gen(used_containers | {c}, total + c.c, available_containers - {c}, rem - c.c):
                        yield seq

    if not part2:
        ret = 0
        for p in gen(set(), 0, set(containers), target):
            ret += 1
        return ret
    else:
        counts = {}
        min_len = len(containers)
        for p in gen(set(), 0, set(containers), target):
            p = list(p)
            l = len(p)
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
