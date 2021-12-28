"""
Day 19: Beacon Scanner
"""
from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
@dataclass
class Point():
    x:int
    y:int
    z:int

    def sq_dist_to(self, p:Point) -> int:
        return ((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2)

def load(filename):
    beacons_per_scanner = []
    scanner_id = -1
    with open(filename) as f:
        for l in f.readlines():
            l = l.strip()
            if l.startswith('---'):
                scanner_id += 1
                beacons_per_scanner.append([])
            elif l:
                coordinates = [int(i) for i in l.split(",")]
                beacons_per_scanner[scanner_id].append(Point(coordinates[0], coordinates[1], coordinates[2]))
    return beacons_per_scanner

def print_points(l:list[Point]):
    for p in l:
        print(p)

INPUT = load("day19_puzzle_input.txt")

def compute_sorted_distances(l:list[Point]):
    """
    to detect overlaps, we rely on distances between beacons because these
    are scanner-independant. We do not know which 12 among the 25 match, so we
    need a complete matrix. Distances are sorted, with the distance to self (0)
    excluded, to simplify the matching - but it breaks the matrix' symetry.
    """
    distances = []
    for i in range(len(l)):
        distances.append([])
        for j in range(i):
            distances[i].append(l[i].sq_dist_to(l[j]))
        distances[i].append(0) # that's distances[i][i]
    # so far we did the lower half of distances
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            distances[i].append(distances[j][i])
    for i in range(len(l)):
        distances[i].sort()
        distances[i].pop(0)
    return distances

distances = [compute_sorted_distances(scanner) for scanner in INPUT]

def find_overlaps(a:list[int], b:list[int]) -> Optional[int]:
    """
    Assumes a and b are sorted and of same length
    Returns:
        number of overlapping distances
    """
    i = 0
    j = 0
    nb_matching = 0
    max_i = len(a)
    max_j = len(b)
    while i < max_i and j < max_j:
        if a[i] == b[j]:
            i += 1
            j += 1
            nb_matching += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return nb_matching

def match_distances(scanner1:list, scanner2:list):
    """
    we search for common beacons seen from scanner1 and scanner2 - but as seen
    from one point it means we try to find 11 similar distances
    """
    matching_points = {}
    matched = set()
    for point_i in range(len(scanner1)):
        for point_j in range(len(scanner2)):
            if point_j in matched:
                continue
            matches = find_overlaps(scanner1[point_i], scanner2[point_j])
            if matches:
                matching_points[point_i] = point_j
                matched.add(point_j)
                break
    return matching_points

points_count = 0

for scanner_id in range(len(distances)):
    points_in_scanner_id_or_more = set([i for i in range(len(distances[scanner_id]))])
    for other_scanner_id in range(scanner_id):
        overlaps = match_distances(distances[scanner_id], distances[other_scanner_id])
        if len(overlaps) >= 12:
            print(f"Scanners {scanner_id} and {other_scanner_id} overlap ({len(overlaps)} points)")
        #     for point_i, point_j in overlaps.items():
        #         print(f"matching_points[{point_i}] = {point_j}")
        points_in_scanner_id_or_more.difference_update(overlaps.keys())
    print(f"points_in_{scanner_id}_or_more: {points_in_scanner_id_or_more}")
    points_count += len(points_in_scanner_id_or_more)

print(f"points count: {points_count}")

# test input: points count=79
# puzzle input: points count=318 is too low!
