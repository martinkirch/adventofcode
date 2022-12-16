from __future__ import annotations
import re

parse = re.compile(r"Valve (?P<name>[A-Z]+) has flow rate=(?P<rate>[0-9]+); tunnels? leads? to valves? (?P<connections>[A-Z, ]+)")
REMAINING_TIME = 30

class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = Valve.name_to_int(name)
        self.flow_rate = int(flow_rate)
        self.connections = [Valve.name_to_int(c) for c in connections.split(', ')]
        self.best_per_t = [0] * (REMAINING_TIME + 1)

    @staticmethod
    def name_to_int(name):
        return (ord(name[0]) - ord('A'))*26 + ord(name[1]) - ord('A')

    @staticmethod
    def int_to_name(name):
        return chr(name // 26 + ord('A')) + chr((name % 26) + ord('A'))

    def __hash__(self) -> int:
        return self.name

    def __str__(self):
        real_name = Valve.int_to_name(self.name)
        connections = ', '.join([Valve.int_to_name(v.name) for v in self.connections])
        return f"Valve {real_name} has flow rate={self.flow_rate}; tunnels lead to valves {connections}"

lines = open("day16_input.txt").readlines()
valves = {}
WORTH_OPENING = set()
for l in lines:
    m = parse.match(l)
    if m:
        valve = Valve(m.group('name'), m.group('rate'), m.group('connections'))
        valves[valve.name] = valve
        if valve.flow_rate > 0:
            WORTH_OPENING.add(valve)
    else:
        print(f"can't match {l}")
for valve in valves.values():
    valve.connections = [valves[n] for n in valve.connections]
    print(valve)

##### ok let's go
def step(valve:Valve, t:int, worth_opening:set[Valve], flow:int, released:int, traversed:set[Valve]):
    """
    beginning of minute t, moving to valve, with given context.
    """
    released += flow
    if released > valve.best_per_t[t]:
        valve.best_per_t[t] = released
    elif valve in traversed: # already been there but not improving - stop
        return
    traversed.add(valve)

    if valve.flow_rate > 0 and t < REMAINING_TIME and valve in worth_opening:
        worth_opening.remove(valve)
        t += 1
        released += flow
        flow += valve.flow_rate
        if released > valve.best_per_t[t]:
            valve.best_per_t[t] = released

    if t == REMAINING_TIME:
        return

    if worth_opening: # move !
        for v in valve.connections:
            step(v, t+1, set(worth_opening), flow, released, set(traversed))
    else: # let it pshhit
        step(valve, t+1, worth_opening, flow, released, traversed)


step(valves[Valve.name_to_int('AA')], 0, set(WORTH_OPENING), 0, 0, set())

best_released = max(v.best_per_t[-1] for v in valves.values())
print(f"we release at most {best_released}")
