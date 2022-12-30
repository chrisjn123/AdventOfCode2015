with open('input.txt') as fh:
    data = [line.strip() for line in fh.readlines()]

pos = complex(0, 0)
pos_2 = complex(0, 0)
delivered = set()
delivered.add(pos)

move_map = {
    '>': complex(1, 0),
    '<': complex(-1, 0),
    '^': complex(0, -1),
    'v': complex(0, 1)
}

for i, move in enumerate(data[0]):
    dx = move_map[move]
    
    if i %2 == 0:
        pos += dx
        delivered.add(pos)
    else:
        pos_2 += dx
        delivered.add(pos_2)

print(f'Delivered to [{len(delivered)}] homes.')