from collections import defaultdict
import numpy as np

with open('input.txt') as fh:
    data = [line.strip() for line in fh.readlines()]

vars = defaultdict(np.uint16)

for line in data:
    sp = line.split()   
    if len(sp) != 3:
        continue
    else:
        try:
            vars[sp[-1]] = np.uint16(sp[0])
        except ValueError:
            vars[sp[-1]] = vars[sp[0]]

for line in data:
    sp = line.split()
    if 'AND' in line:
        try:
            left = np.uint16(sp[0])
        except:
            left = vars[sp[0]]
        right = vars[sp[2]]
        dest = sp[-1]

        vars[dest] = np.uint16(left & right)
    elif 'OR' in line:
        try:
            left = np.uint16(sp[0])
        except:
            left = vars[sp[0]]
        right = vars[sp[2]]
        dest = sp[-1]

        vars[dest] = np.uint16(left | right)
    elif 'LSHIFT' in line:
        vars[sp[-1]] = np.uint16(vars[sp[0]] << int(sp[2]))
    elif 'RSHIFT' in line:
        vars[sp[-1]] = np.uint16(vars[sp[0]] >> int(sp[2]))
    elif 'NOT' in line:
        vars[sp[-1]] = np.uint16(~vars[sp[1]])
    else:
        pass

print(vars['a'])