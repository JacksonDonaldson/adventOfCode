use std::fs;
use std::collections::HashMap;

fn check_vertical(map: &str, index: usize, len: usize) -> Vec::<usize>{
    let mut gears = Vec::<usize>::new();
    if "*".contains(map.chars().nth(index).unwrap()){
        gears.push(index);
    }
    let below = index + len;
    if index >= len {
        let above = index - len;
        if "*".contains(map.chars().nth(above).unwrap()){
            gears.push(above);
        }
    }

    if below < map.len() {
        if "*".contains(map.chars().nth(below).unwrap()){
            gears.push(below);
        }
    }
    return gears;
}

fn main() {
    let contents = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let first = contents.chars().nth(10).unwrap();
    let len = contents.find("\n").unwrap() + 1;

    println!("{first}, {len}");

    let mut current_num = String::new();

    let mut prev_was_number = false;

    let mut gears = HashMap::new();
    let mut adjacent_gears = Vec::<usize>::new();


    for (i,c) in contents.chars().enumerate(){

        if "0123456789".contains(c) {
            //println!("{c}");
            current_num.push(c);
            {
                adjacent_gears.extend(check_vertical(&contents, i, len));
            }
            prev_was_number = true;

        }
        else{
            if prev_was_number {
                adjacent_gears.extend(check_vertical(&contents, i, len));
                for gear in &adjacent_gears{
                    //total += current_num.parse::<i32>().unwrap();
                    let values = gears.entry(*gear).or_insert(Vec::new());
                    values.push(current_num.parse::<i32>().unwrap());
                } 
                current_num.clear();
            }
            adjacent_gears.clear();
            adjacent_gears.extend(check_vertical(&contents, i, len));
            prev_was_number = false;
        }
    }

    let mut total = 0;
    for (_gear, adjacent) in &gears{
        if adjacent.len() == 2{
            total += adjacent[0] * adjacent[1];
        }
    }

    println!("total: {total}");

}
//> 520597, < 537359