from dataclasses import dataclass

@dataclass
class Race():
    time: int
    best_distance: int

    def distance_when(self, holding_t:int) -> int:
        return holding_t * (self.time - holding_t)

    def number_ways_to_beat(self) -> int:
        n = 0
        for i in range(self.time):
            if self.distance_when(i) > self.best_distance:
                n += 1
        return n

def today(data:list[str]) -> int:
    times = data[0].split()
    times.pop(0)
    distances = data[1].split()
    distances.pop(0)
    races = [Race(int(times[i]), int(distances[i])) for i in range(len(times))]
    total = 1
    for race in races:
        n = race.number_ways_to_beat()
        total = total * n
    return total
