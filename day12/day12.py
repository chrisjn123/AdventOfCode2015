import json
fname = 'input.txt'

with open(fname, 'r') as fh:
    data = json.load(fh)

def get_numbers(d):
    total = 0
    for i in d:
        if isinstance(i, int):
            total += i
        elif isinstance(i, dict):
            if i == 'red' or 'red' in i.values():
                continue
            total += get_numbers(i.values())
        elif isinstance(i, list):
            if i == 'red':
                continue
            total += get_numbers(i)
    return total

print(get_numbers(data))