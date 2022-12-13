#!/usr/bin/python3
#encoding: UTF-8

import fileinput
import sys
import copy
from enum import Enum

test_input="""Hit Points: 13
Damage: 8
""".splitlines()

if len(sys.argv) == 1:
    sys.argv += ["input_22"]

with fileinput.input() as inputs:
    it = iter(inputs)
    input_boss_hp = int(next(it).strip().split(": ")[1])
    input_boss_damage = int(next(it).strip().split(": ")[1])

class Spell(Enum):
    MISSILE = 53
    DRAIN = 73
    SHIELD = 113
    POISON = 173
    RECHARGE = 229

# ordered by mana
all_spells = [ \
    Spell.MISSILE, \
    Spell.DRAIN, \
    Spell.SHIELD, \
    Spell.POISON, \
    Spell.RECHARGE]

class State(object):
    def __init__(self, hp, mana, boss_hp, boss_damage):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        
        self.effect_shield = 0
        self.effect_poison = 0
        self.effect_recharge = 0
        
        self.mana_spent = 0
                
    def can_cast(self, spell, best=None):
        if self.mana < spell.value:
            return False
        if best != None and self.mana_spent + spell.value >= best:
            return False
        if spell == Spell.SHIELD and self.effect_shield > 0:
            return False
        if spell == Spell.POISON and self.effect_poison > 0:
            return False
        if spell == Spell.RECHARGE and self.effect_recharge > 0:
            return False
        return True
    
    def apply_effects(self):
        if self.effect_shield > 0:
            self.armor = 7
            self.effect_shield -= 1
        else:
            self.armor = 0
        if self.effect_poison > 0:
            self.boss_hp -= 3
            self.effect_poison -= 1
        if self.effect_recharge > 0:
            self.mana += 101
            self.effect_recharge -= 1
        
        if self.boss_hp <= 0:
            return True
    
    def hard(self):
        self.hp -= 1
        return self.hp <= 0
    
    def round_player(self, cast):      
        if cast == Spell.MISSILE:
            self.boss_hp -= 4
        elif cast == Spell.DRAIN:
            self.boss_hp -= 2
            self.hp += 2
        elif cast == Spell.SHIELD:
            self.effect_shield = 6
        elif cast == Spell.POISON:
            self.effect_poison = 6
        elif cast == Spell.RECHARGE:
            self.effect_recharge = 5
        
        self.mana -= cast.value
        self.mana_spent += cast.value
        
        return self.boss_hp <= 0
    
    def round_boss(self):        
        damage = max(self.boss_damage - self.armor, 1)
        self.hp -= damage
        
        return self.boss_hp <= 0 or self.hp <= 0
    
    def win(self):
        return self.boss_hp <= 0

    def __repr__(self):
        return repr({"hp": self.hp, "mana":self.mana, "armor":self.armor, "boss": self.boss_hp, "shield": self.effect_shield, "poison": self.effect_poison, "recharge": self.effect_recharge, "mana_spent": self.mana_spent})

def work_p1(hp, mana, boss_hp, boss_dmg):
    best = None
    
    def mark(s):
        nonlocal best
        if s.win():
            if best == None or s.mana_spent < best:
                print(s)
                best = s.mana_spent
    
    stack = [State(hp, mana, boss_hp, boss_dmg)]
    while len(stack) != 0:
        state = stack.pop(0)
        if best != None and state.mana_spent >= best:
            continue
        for spell in all_spells:
            s = copy.deepcopy(state)
            if s.apply_effects():
                mark(s)
                continue
            if not s.can_cast(spell, best):
                continue
            if s.round_player(spell):
                mark(s)
                continue
            if s.apply_effects():
                mark(s)
                continue
            if s.round_boss():
                mark(s)
                continue
            
            if best == None or s.mana_spent < best:
                stack.append(s)
    return best
    
def work_p2(hp, mana, boss_hp, boss_dmg):
    best = None
    
    def mark(s):
        nonlocal best
        if s.win():
            if best == None or s.mana_spent < best:
                # print(s)
                best = s.mana_spent
    
    stack = [State(hp, mana, boss_hp, boss_dmg)]
    while len(stack) != 0:
        state = stack.pop(0)
        if best != None and state.mana_spent >= best:
            continue
        for spell in all_spells:
            s = copy.deepcopy(state)
            if s.hard():
                continue
            if s.apply_effects():
                mark(s)
                continue
            if not s.can_cast(spell, best):
                continue
            if s.round_player(spell):
                mark(s)
                continue
            if s.apply_effects():
                mark(s)
                continue
            if s.round_boss():
                mark(s)
                continue
            
            if best == None or s.mana_spent < best:
                stack.append(s)
    return best

def test_p1():
    assert(work_p1(10, 250, 14, 8) == 641)
test_p1()

def p1():
    print(work_p1(50, 500, input_boss_hp, input_boss_damage))
p1()

def p2():
    print(work_p2(50, 500, input_boss_hp, input_boss_damage))
p2()
