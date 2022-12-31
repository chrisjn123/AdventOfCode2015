from collections import defaultdict

data = [line.strip() for line in open('input.txt').readlines()]
nice_count = 0

def double(line: str) -> bool:
    dbs = defaultdict(int)
    to_test = set()
    for i, ch in enumerate(line[:-1]):
        key = ch + line[i+1]
        dbs[key] += 1
        if dbs[key] > 1:
            to_test.add(key)

    for pair in to_test:
        p1 = line.find(pair)
        p2 = line[p1+2:].find(pair)

        if p2 != -1:
            return True

    return False


def repeat(line: str) -> bool:
    for i, ch in enumerate(line[:-2]):
        if ch == line[i+2]:
            return True
    return False

for line in data:

    if not double(line) or not repeat(line):
        continue
    nice_count += 1

print(nice_count)