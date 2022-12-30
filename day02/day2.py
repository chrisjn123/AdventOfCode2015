with open('input.txt', 'r') as fh:
    data = [line.strip() for line in fh.readlines()]

class Box:
    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.height = height
        self.width = width

        self.surface_area = (
            (2 * self.length * self.height)
            + (2 * self.length * self.width)
            + (2 * self.height * self.width)
        )
        self.smallest_area = self.find_smallest_area()
        self.volume = self.length * self.width * self.height
        self.smallest_perimeter = self.find_smallest_peri()
    
    def find_smallest_area(self) -> int:
        side_1 = self.length * self.width
        side_2 = self.length * self.height
        side_3 = self.width * self.height

        return min(side_1, side_2, side_3)
    
    def find_smallest_peri(self):
        p_1 = 2 * (self.length + self.height)
        p_2 = 2 * (self.length + self.width)
        p_3 = 2 * (self.width + self.height)

        return min(p_1, p_2, p_3)

boxes = list()
surf_total = 0
ribbon_total = 0
for line in data:
    x, y, z = map(int, line.split('x'))
    b = Box(x, y, z)

    box_ribbon = b.volume + b.smallest_perimeter
    ribbon_total += box_ribbon

    box_total = b.smallest_area + b.surface_area
    surf_total += box_total

print(f'Paper : {surf_total}')
print(f'Ribbon: {ribbon_total}')