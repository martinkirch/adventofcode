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
    race = Race(
        time=int(data[0][11:].replace(' ', '')),
        best_distance=int(data[1][11:].replace(' ', ''))
    )
    return race.number_ways_to_beat()
