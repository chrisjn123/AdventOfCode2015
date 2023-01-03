from itertools import groupby
in_val = '1113222113'
next_val = str()

def make_next(line: str) -> str:
    dig = ''
    for k, g in groupby(line):
        dig += str(len(list(g)))
        dig += str(k)
    return dig

for _ in range(50):
    in_val = make_next(in_val)
print(f'{len(in_val)}')