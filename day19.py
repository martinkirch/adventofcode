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

INPUT = load("day19_test_input.txt")

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

def find_12_overlaps(a:list[int], b:list[int]) -> Optional[int]:
    """
    Assumes a and b are sorted and of same length
    Returns:
        number of overlapping distances, if >= 12
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
        if i > (max_i - 12 + nb_matching) or j > (max_j - 12 + nb_matching):
            return None
    if nb_matching < 12:
        return None
    return nb_matching

def match_distances(d1:list, d2:list):
    nb_matching = 0
    for point_i in range(len(d1)):
        for point_j in range(len(d2)):
            matches = find_12_overlaps(d1[point_i], d2[point_j])
            if matches:
                nb_matching += 1
    return nb_matching


for scanner_id in range(len(distances)):
    for other_scanner_id in range(scanner_id):
        nb_overlaps = match_distances(distances[scanner_id], distances[other_scanner_id])
        if nb_overlaps:
            print(f"Scanners {scanner_id} and {other_scanner_id} overlap")


