from collections import defaultdict
import ctypes
from functools import cache

with open('input.txt') as fh:
    data = [line.strip() for line in fh.readlines()]

look_up = defaultdict(str)

for line in data:
    sp = line.split('->')
    key = sp[-1].strip()
    op = sp[0].strip()
    look_up[key] = op

look_up = {key: val for key, val in sorted(look_up.items(), key = lambda ele: ele[0])}

def compute(table: dict, key: str) -> int:
    try:
        out = ctypes.c_uint16(int(table[key]))
        return out
    except:
        pass

    op = table[key].lower().replace('lshift', '<<').replace('rshift', '>>').replace('or', '|').replace('not', '~').replace('and', '&').split()
    if len(op) == 1:
        return compute(table, op[0])
    elif '~' in op:
        return ctypes.c_uint16(~compute(table, op[1]).value)
    else:
        try:
            left = ctypes.c_uint16(int(op[0]))
        except:
            left = compute(table, op[0])

        try:
            right = ctypes.c_uint16(int(op[2]))
        except:
            right = compute(table, op[2])

    
        match op[1]:
            case '<<':
                return ctypes.c_uint16(left.value << right.value)
            case '>>':
                return ctypes.c_uint16(left.value >> right.value)
            case '&':
                return ctypes.c_uint16(left.value & right.value)
            case '|':
                return ctypes.c_uint16(left.value | right.value)
            case other:
                print(f'Error: {op[1]}')

print(compute(look_up, 'a'))