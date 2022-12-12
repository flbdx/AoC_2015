#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple("Item", ["name", "cost", "damage", "armor"])
Weapons = [\
    Item('Dagger'    ,  8, 4, 0), \
    Item('Shortsword', 10, 5, 0), \
    Item('Warhammer' , 25, 6, 0), \
    Item('Longsword' , 40, 7, 0), \
    Item('Greataxe'  , 74, 8, 0)]
Armors = [\
    Item('Leather'   ,  13, 0, 1), \
    Item('Chainmail' ,  31, 0, 2), \
    Item('Splintmail',  53, 0, 3), \
    Item('Bandedmail',  75, 0, 4), \
    Item('Platemail' , 102, 0, 5)]
Rings = [\
    Item('Damage +1' ,  25, 1, 0), \
    Item('Damage +2' ,  50, 2, 0), \
    Item('Damage +3' , 100, 3, 0), \
    Item('Defense +1',  20, 0, 1), \
    Item('Defense +2',  40, 0, 2), \
    Item('Defense +3',  80, 0, 3)]

if len(sys.argv) == 1:
    sys.argv += ["input_21"]

# generate a set of equipement from a number between 0 and 5*6*22
# 5 choices for the weapon
# 6 choices for the armor (including no armor)
# 22 choices for the ring (1x0ring, 6x1ring, 15x2rings)
def gen_equip(n):
    n, rem = divmod(n, 5)
    weapon = [ Weapons[rem] ]
    n, rem = divmod(n, 6)
    armor = [] if rem == 0 else [ Armors[rem-1] ]
    n, rem = divmod(n, 22)
    
    assert(n == 0)
    
    if rem == 0:
        rings = []
    elif rem < 7:
        rings = [ Rings[rem - 1 ] ]
    else:
        rings = list(list(combinations(Rings, 2))[rem - 8])
    return rings + armor + weapon

def equip_cst(combi):
    return sum(e.cost for e in combi)
def equip_dmg(combi):
    return sum(e.damage for e in combi)
def equip_arm(combi):
    return sum(e.armor for e in combi)

def do_I_win(equip, my_hp, boss_hp, boss_dmg, boss_arm):
    dmg = equip_dmg(equip)
    arm = equip_arm(equip)
    boss_loss = dmg - boss_arm
    if boss_loss <= 0:
        boss_loss = 1
    my_loss = boss_dmg - arm
    if my_loss <= 0:
        my_loss = 1
    
    boss_dead_after_round, rem = divmod(boss_hp, boss_loss)
    if rem != 0:
        boss_dead_after_round += 1
    I_dead_after_round, rem = divmod(my_hp, my_loss)
    if rem != 0:
        I_dead_after_round += 1
    
    return boss_dead_after_round <= I_dead_after_round

with fileinput.input() as inputs:
    it = iter(inputs)
    boss_hp = int(next(it).strip().split(": ")[1])
    boss_damage = int(next(it).strip().split(": ")[1])
    boss_armor = int(next(it).strip().split(": ")[1])
    my_hp = 100

def work_p1(inputs):
    best_cost = None
    best_equip = None
    for i in range(5*6*22):
        equip = gen_equip(i)
        cost = equip_cst(equip)
        win = do_I_win(equip, my_hp, boss_hp, boss_damage, boss_armor)
        if win and (best_cost == None or cost < best_cost):
            best_cost = cost
            best_equip = equip
    print(best_equip)
    return best_cost

def work_p2(inputs):
    worst_cost = None
    worst_equip = None
    for i in range(5*6*22):
        equip = gen_equip(i)
        cost = equip_cst(equip)
        win = do_I_win(equip, my_hp, boss_hp, boss_damage, boss_armor)
        if not win and (worst_cost == None or cost > worst_cost):
            worst_cost = cost
            worst_equip = equip
    print(worst_equip)
    return worst_cost

def p1():
    print(work_p1(fileinput.input()))
p1()

def p2():
    print(work_p2(fileinput.input()))
p2()
