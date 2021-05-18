use std::collections::HashMap;
use std::io;

fn read_line() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input
}

fn get_current_vec() -> Vec<usize> {
    let first_line = read_line();
    let values: Vec<usize> = first_line
        .trim()
        .split_whitespace()
        .map(|content| content.parse::<usize>().unwrap())
        .collect();

    values
}

// Servers
// https://codeforces.com/problemset/problem/747/C
pub fn out_put_servers() {
    let two_value = get_current_vec();
    let (server_count, task_count) = (two_value[0], two_value[1]);
    let mut time_can_use: HashMap<usize, usize> = HashMap::new();

    for value in 0..server_count {
        time_can_use.insert(value, 0);
    }

    for _value in vec![0; task_count] {
        let three_value: Vec<usize> = get_current_vec();
        let (from_time, need_count, need_time) = (three_value[0], three_value[1], three_value[2]);

        let mut can_use_index: Vec<usize> = Vec::new();
        let mut has_count = 0;
        let mut sum_print = 0;
        for num in 0..server_count {
            if time_can_use.get(&num).unwrap() <= &from_time {
                can_use_index.push(num);
                has_count += 1;
                sum_print += num + 1;
                if has_count == need_count {
                    break;
                }
            }
        }
        if can_use_index.len() == need_count {
            for elem in can_use_index {
                time_can_use.insert(elem, from_time + need_time);
            }
            println!("{}", sum_print);
        } else {
            println!("{}", -1);
        }
    }
}