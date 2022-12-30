
PART_1 = False
with open('input.txt', 'r') as fh:
    line = fh.read().strip()

    total = 0
    for pos, ch in enumerate(line):
        if ch == '(':
            dx = 1
        else:
            dx = -1
        
        total += dx
        if not PART_1 and total == -1:
            print(f'Floor == -1 at pos {pos+1}')
            break
    print(total)