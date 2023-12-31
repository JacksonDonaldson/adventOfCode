use std::fs;
use std::cmp::Ordering;
use std::collections::HashMap;

fn getCounts(hand: &str) -> Vec<i32>{
    let mut counts = HashMap::new();
    let mut jcount = 0;
    for c in hand.chars(){
        if c == 'J'{
            jcount += 1;
            continue;
        }
        let count = counts.entry(c).or_insert(0);
        *count += 1;
    }
    let mut result = Vec::new();
    for (_c, count) in counts{
        result.push(count);
    }
    result.sort();
    if result.len() == 0{
        result.push(0);
    }
    let end = result.len() - 1;
    result[end] += jcount;
    return result;
}
fn is5(hand: &str) -> bool{
    return getCounts(hand) == [5];
}
fn is4(hand: &str) -> bool{
    return getCounts(hand) == [1,4];
}
fn ishouse(hand: &str) -> bool{
    return getCounts(hand) == [2,3];
}
fn is3(hand: &str) -> bool{
    return getCounts(hand) == [1,1,3];
}
fn is2pair(hand: &str) -> bool{
    return getCounts(hand) == [1,2,2];
}
fn ispair(hand: &str) -> bool{
    return getCounts(hand) == [1,1,1,2];
}

fn getType(hand: &str) -> i32{
    if is5(hand){
        return 5;
    }
    if is4(hand){
        return 4;
    }
    if ishouse(hand){
        return 3;
    }
    if is3(hand){
        return 2;
    }
    if is2pair(hand){
        return 1;
    }
    if ispair(hand){
        return 0;
    }
    return -1;
}

fn getValue(a: char)-> i32{
    if "0123456789".contains(a){
        return a.to_digit(10).unwrap().try_into().unwrap();
    }
    if a == 'T'{
        return 10;
    }
    if a == 'J'{
        return 0;
    }
    if a == 'Q'{
        return 12;
    }
    if a == 'K'{
        return 13;
    }
    if a == 'A'{
        return 14;
    }
    println!("fail {a}");
    return -1;
    
}
fn compare(a: &(&str, i32), b: &(&str, i32))-> Ordering{
    let atype = getType(a.0);
    let btype = getType(b.0);

    if atype > btype{
        return Ordering::Greater;
    }
    else if btype > atype{
        return Ordering::Less;
    }
    
    for i in 0..5{
        if getValue(a.0.chars().nth(i).unwrap()) > getValue(b.0.chars().nth(i).unwrap()){
            return Ordering::Greater;
        }
        else if getValue(a.0.chars().nth(i).unwrap()) < getValue(b.0.chars().nth(i).unwrap()){
            return Ordering::Less;
        }
    }
    return Ordering::Equal;
    
}

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");

    let mut hands = Vec::new();
    
    for line in content.split("\n"){
        let mut values = line.split(" ");
        let hand = values.next().unwrap();
        let value = values.next().unwrap().parse::<i32>().unwrap();

        hands.push((hand, value));
    }

    hands.sort_by(|a, b| compare(a,b));

    let mut total = 0;
    let mut i = 1;
    for hand in hands{
        total += i * hand.1;
        i +=1;
    }
    println!("score: {total}");
}
