#!/usr/bin/env python3

program = []
regs = {}
max_val = 0

def get_reg_val(name):
    val = regs.get(name)
    if val is None:
        regs[name] = 0
        return 0
    return val

def inc_reg_val(name, amt):
    global max_val
    val = regs.get(name)
    if val is None:
        regs[name] = 0
    regs[name] += amt
    if regs[name] > max_val:
        max_val = regs[name]

def dec_reg_val(name, amt):
    global max_val
    val = regs.get(name)
    if val is None:
        regs[name] = 0
    regs[name] -= amt
    if regs[name] > max_val:
        max_val = regs[name]

with open("input.txt", "r") as f:
    program = [l.strip() for l in f.readlines()]

for instr in program:
    reg, op, amt, _, cond = instr.split(" ", 4)
    amt = int(amt)
    c_reg, c_op, c_val = cond.split(" ")
    c_val = int(c_val)
    a = get_reg_val(c_reg)

    cmp_res = False
    if c_op == ">":
        cmp_res = a > c_val
    elif c_op == "<":
        cmp_res = a < c_val
    elif c_op == "==":
        cmp_res = a == c_val
    elif c_op == ">=":
        cmp_res = a >= c_val
    elif c_op == "<=":
        cmp_res = a <= c_val
    elif c_op == "!=":
        cmp_res = a != c_val

    if not cmp_res:
        continue

    if op == "inc":
        inc_reg_val(reg, amt)
    elif op == "dec":
        dec_reg_val(reg, amt)

print(regs[max(regs, key=regs.get)])
print(max_val)