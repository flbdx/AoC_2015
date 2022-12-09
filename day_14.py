#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import re

test_input="""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_14"]

class Reindeer(object):
    def __init__(self, line):
        m = re.fullmatch("([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.", line.strip())
        self.name = m.group(1)
        self.speed_km_secs = int(m.group(2))
        self.fly_secs = int(m.group(3))
        self.rest_secs = int(m.group(4))
        
        self.period = self.fly_secs + self.rest_secs
        self.position = 0
        self.time = 0
    
    # part 1
    def p1_travel_dist(self, time):
        full_periods, rem = divmod(time, self.period)
        d = full_periods * self.speed_km_secs * self.fly_secs
        d += self.speed_km_secs * min(self.fly_secs, rem)
        return d
    
    # part 2, one second step
    def p2_step(self):
        full_periods, rem = divmod(self.time, self.period)
        if rem < self.fly_secs:
            self.position += self.speed_km_secs
        self.time += 1
    
    def __repr__(self):
        return self.name + " " + repr((self.speed_km_secs, self.fly_secs, self.rest_secs))

def work_p1(inputs, time=1000):
    reindeers = []
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        reindeers.append(Reindeer(line))
    return max(r.p1_travel_dist(time) for r in reindeers)

def work_p2(inputs, time=1000):
    reindeers = []
    scores = {}
    
    for line in inputs:
        line = line.strip()
        if len(line) == 0:
            continue
        reindeers.append(Reindeer(line))
    
    for i in range(time):
        best = 0
        for r in reindeers:
            r.p2_step()
            best = max(best, r.position)
        for r in reindeers:
            if r.position == best:
                scores[r.name] = scores.setdefault(r.name, 0) + 1
    
    return max(scores.values())
    

def test_p1():
    assert(work_p1(test_input, 1000) == 1120)
test_p1()

def p1():
    print(work_p1(fileinput.input(), 2503))
p1()

def test_p2():
    assert(work_p2(test_input, 1000) == 689)
test_p2()

def p2():
    print(work_p2(fileinput.input(), 2503))
p2()
