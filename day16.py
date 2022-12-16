import re

parse = re.compile(r"Valve (?P<name>[A-Z]+) has flow rate=(?P<rate>[0-9]+); tunnels? leads? to valves? (?P<connections>[A-Z, ]+)")

class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = int(flow_rate)
        self.connections = connections.split(', ')
    
    def __str__(self):
        return f"Valve {self.name} has flow rate={self.flow_rate}; tunnels lead to valves {', '.join([v.name for v in self.connections])}"

lines = open("day16_test.txt").readlines()
valves = {}
for l in lines:
    m = parse.match(l)
    if m:
        valve = Valve(m.group('name'), m.group('rate'), m.group('connections'))
        valves[valve.name] = valve
    else:
        print(f"can't match {l}")
for valve in valves.values():
    valve.connections = [valves[n] for n in valve.connections]

##### ok let's go

for valve in valves.values():
    print(valve)
