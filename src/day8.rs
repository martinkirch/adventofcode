use std::collections::BinaryHeap;
use std::collections::BTreeSet;
use std::cmp::Ordering;
use std::cmp::{min, max};

pub fn compute(input:&String,) -> String {
    return real_compute(input, 1000);
}

fn real_compute(input:&String, n_closest:usize) -> String {
    let boxes:Vec<Vec<u64>> = input.lines().map(|line| line.split(',').map(|x| x.parse::<u64>().unwrap()).collect()).collect();
    let mut heap:BinaryHeap<Pair> = BinaryHeap::new();

    for (i, item) in boxes.iter().enumerate() {
        for j in i+1..boxes.len() {
            let dist = distance(&item, &boxes[j]);
            if heap.len() == n_closest {
                let head = heap.peek().unwrap();
                if dist < head.dist {
                    heap.pop();
                    heap.push(Pair {
                        i: i,
                        j: j,
                        dist: dist,
                    });
                }
            } else {
                heap.push(Pair {
                        i: i,
                        j: j,
                        dist: dist,
                    });
            }
        }
    }

    let mut circuit_ids = Vec::from_iter(0..boxes.len());

    for pair in heap {
        let circuit_id = min(circuit_ids[pair.i], circuit_ids[pair.j]);
        let old_circuit_id = max(circuit_ids[pair.i], circuit_ids[pair.j]);
        for i in circuit_ids.iter_mut() {
            if *i == old_circuit_id {
                *i = circuit_id;
            }
        }
    }

    let mut sizes = BTreeSet::new();
    let mut prev_circuit_id = 9999999;
    let mut prev_circuit_cnt = 1;
    circuit_ids.sort();
    for i in circuit_ids {
        if i == prev_circuit_id {
            prev_circuit_cnt += 1;
        } else {
            sizes.insert(prev_circuit_cnt);
            prev_circuit_id = i;
            prev_circuit_cnt = 1;
        }
    }
    sizes.insert(prev_circuit_cnt);

    sizes.into_iter().rev().take(3).reduce(|acc, e| acc * e).unwrap().to_string()
}

fn distance(first:&Vec<u64>, second:&Vec<u64>) -> u64 {
    assert!(first.len() == 3);
    assert!(second.len() == 3);
    first[0].abs_diff(second[0]).pow(2) + first[1].abs_diff(second[1]).pow(2) + first[2].abs_diff(second[2]).pow(2)
}

struct Pair {
    i: usize,
    j: usize,
    dist: u64,
}

impl Ord for Pair {
    fn cmp(&self, other: &Self) -> Ordering {
        self.dist.cmp(&other.dist)
    }
}

impl PartialOrd for Pair {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Pair {
    fn eq(&self, other: &Self) -> bool {
        self.dist == other.dist
    }
}

impl Eq for Pair {}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = real_compute(&"162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
".to_string(), 10);
        assert_eq!(result, "40");
    }
}
