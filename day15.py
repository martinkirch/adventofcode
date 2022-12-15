import re

parse = re.compile(r"Sensor at x=(?P<sx>[-0-9]+), y=(?P<sy>[-0-9]+): closest beacon is at x=(?P<bx>[-0-9]+), y=(?P<by>[-0-9]+)")

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = int(sx)
        self.sy = int(sy)
        self.bx = int(bx)
        self.by = int(by)
        self.maxdist = self.dist(self.bx, self.by)
    
    def __str__(self):
        return f"Sensor at x={self.sx}, y={self.sy}: closest beacon is at x={self.bx}, y={self.by}"

    def dist(self, x, y):
        return abs(x - self.sx) + abs(y - self.sy)
    
    def gen_positions_around(self, y):
        # quite BF but good enough for phase1 thanks to `y`
        for x in range(self.sx - self.maxdist, self.sx + self.maxdist + 1):
            if self.dist(x, y) <= self.maxdist:
                yield (x, y)

    def intersect_increment(self, x, y) -> int:
        """
        return 0 if (x,y) is not in sensor range
        otherwise, return how much y can be incremented to get out of reach

        slow AF too (4 minutes!), but hey i got the star on first attempt
        """
        d = self.dist(x, y)
        if d <= self.maxdist:
            if y <= self.sy:
                increment = 2 * (self.sy - y) + 1
            else:
                remaining_dist = self.maxdist - abs(x - self.sx)
                increment = remaining_dist - (y - self.sy) + 1
            return increment

lines = open("day15_input.txt").readlines()
sensors = []
for line in lines:
    m = parse.match(line)
    sensor = Sensor(m.group('sx'), m.group('sy'), m.group('bx'), m.group('by'))
    print(str(sensor) + f" dist is {sensor.dist(sensor.bx, sensor.by)}")
    sensors.append(sensor)

# search_row = 2000000
# no_beacon = set()
# for s in sensors:
#     for p in s.gen_positions_around(search_row):
#         if p[1] == search_row:
#             no_beacon.add(p)

# for s in sensors:
#     try:
#         no_beacon.remove((s.sx, s.sy))
#     except KeyError:
#         pass
#     try:
#         no_beacon.remove((s.bx, s.by))
#     except KeyError:
#         pass

# print(f"phase1: at {search_row}, {len(no_beacon)} cannot contain a beacon")

size = 4000001
for x in range(size):
    y = 0
    while y < size:
        for s in sensors:
            increment = s.intersect_increment(x, y)
            if increment:
                y += increment
                break
        else:
            print(f"{x,y} works")
            print(f"frequency is {(4000000*x) + y}")
            y += 1

