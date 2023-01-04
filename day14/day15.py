from re import findall
from collections import defaultdict


data = open('input.txt').readlines()
names = [line.split()[0] for line in data]
data = [
    list(map(int, findall(r'\d+', line)))
    for line in data
]

rd = defaultdict(tuple)

class Deer:
    def __init__(self, name, speed, move_time, wait_time) -> None:
        self.name = name
        self.move_time = move_time
        self.wait_time = wait_time
        self.speed = speed

        self.stopped_time = 0
        self.moving_left = self.move_time
        self.position = 0

    def move(self):
        if self.moving_left > 0:
            self.position += self.speed
            self.moving_left -= 1
            if self.moving_left == 0:
                self.stopped_time = self.wait_time
        
        elif self.stopped_time > 0:
            self.stopped_time -= 1
            if self.stopped_time == 0:
                self.moving_left = self.move_time

deer = []
for i, d in enumerate(data):
    deer.append(Deer(names[i], d[0], d[1], d[2]))

points = defaultdict(int)
for sec in range(2503):
    for d in deer:
        d.move()
    
    leads = [d.name for d in deer if max(d.position for d in deer) == d.position]
    for lead in leads:
        points[lead] += 1
    
