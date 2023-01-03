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

table = defaultdict()
table = {key: val for key, val in sorted(look_up.items(), key = lambda ele: ele[0])}
table['b'] = 46065

def compute(key: str) -> int:
    global table
    try:
        out = ctypes.c_uint16(int(table[key].value))
        table[key] = out
        return out
    except:
        try:
            out = ctypes.c_uint16(int(table[key]))
            table[key] = out
            return out
        except:
            try:
                out = ctypes.c_uint16(int(key))
                table[key] = out
                return out
            except:
                pass

    op = table[key].lower().replace('lshift', '<<').replace('rshift', '>>').replace('or', '|').replace('not', '~').replace('and', '&').split()
    if len(op) == 1:
        return compute(op[0])
    elif '~' in op:
        return ctypes.c_uint16(~compute(op[1]).value)
    else:
        try:
            left = ctypes.c_uint16(int(op[0].value))
        except:
            left = compute(op[0])

        try:
            right = ctypes.c_uint16(int(op[2].value))
        except:
            right = compute(op[2])

    
        match op[1]:
            case '<<':
                ret = ctypes.c_uint16(left.value << right.value)
            case '>>':
                ret = ctypes.c_uint16(left.value >> right.value)
            case '&':
                ret = ctypes.c_uint16(left.value & right.value)
            case '|':
                ret = ctypes.c_uint16(left.value | right.value)
            case other:
                print(f'Error: {op[1]}')
        table[key] = ret
        return ret

print(compute('a'))