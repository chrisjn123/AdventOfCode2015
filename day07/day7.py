from collections import defaultdict
import numpy as np

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
        out = np.uint16(table[key])
        return out
    except:
        pass

    op = table[key].lower().replace('lshift', '<<').replace('rshift', '>>').replace('or', '|').replace('not', '~').replace('and', '&').split()
    if len(op) == 1:
        return compute(table, op[0])
    elif '~' in op:
        return eval(f'{op[0]}{compute(table, op[1])}')
    else:
        try:
            left = np.uint16(op[0])
        except:
            left = compute(table, op[0])

        try:
            right = np.uint16(op[2])
        except:
            right = compute(table, op[2])

    
        return eval(f'{left}{op[1]}{right}')

print(compute(look_up, 'a'))