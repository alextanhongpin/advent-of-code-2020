use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file = File::open("input_01.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let mut tree = HashMap::new();
    for line in lines {
        let line: u32 = line.unwrap().parse().unwrap();
        let diff = 2020 - line;
        if tree.contains_key(&diff) {
            println!("{}", diff * line);
            break;
        }
        tree.insert(line, true);
    }

    let file = File::open("input_01.txt").unwrap();
    let lines = io::BufReader::new(file).lines();
    let mut numbers = lines
        .map(|line| line.unwrap().parse().unwrap())
        .collect::<Vec<u32>>();
    numbers.sort();

    if let Some(pair) = find_pair(&numbers, 2020, 0, numbers.len() - 1) {
        println!("{}", pair.0 * pair.1);
    }

    if let Some(triplet) = find_triplet(&numbers, 2020) {
        println!("{}", triplet.0 * triplet.1 * triplet.2);
    }
}

fn find_pair(numbers: &Vec<u32>, tgt: u32, mut i: usize, mut j: usize) -> Option<(u32, u32)> {
    while i < j {
        let sum = numbers[i] + numbers[j];
        if sum == tgt {
            return Some((numbers[i], numbers[j]));
        } else if sum > tgt {
            j -= 1;
        } else {
            i += 1;
        }
    }
    None
}

fn find_triplet(numbers: &Vec<u32>, tgt: u32) -> Option<(u32, u32, u32)> {
    let mut i = 0;
    let mut j = numbers.len() - 1;
    while i < j && j > i {
        let k = i + 1;
        let sum = numbers[i] + numbers[k] + numbers[j];
        if sum == tgt {
            return Some((numbers[i], numbers[k], numbers[j]));
        } else if sum > tgt {
            j -= 1;
        } else {
            let tgt = tgt - numbers[i];
            if let Some(pair) = find_pair(&numbers, tgt, i + 1, j) {
                return Some((numbers[i], pair.0, pair.1));
            }
            i += 1;
        }
    }
    None
}
