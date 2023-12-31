use std::collections::HashSet;
use std::fs;

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let len = content.matches("\n").count()+1;
    println!("{len}");
    let mut counts = vec![1; len];

    let lines = content.split("\n");
    let mut total = 0;
    let mut i = 0;
    for line in lines{
        let mut split = line.split(" | ");
        let first = split.next().expect("this is dumb").split(" ");
        let second = split.next().expect("ah rust").split(" ");

        let mut winners = HashSet::new();
        for (i,item) in first.enumerate(){
            if i == 0 || i == 1 || item == "" || item.contains(":"){
                continue;
            }
            //print!("item: {item} ");
            winners.insert(item.parse::<i32>().unwrap());
            
        }
        //println!("");
        
        let mut won = 0;
        for number in second {
            if number == "" {
                continue;
            }
            //println!("{number}");
            if winners.contains(&number.parse::<i32>().expect("test")){
                won+=1;
                //println!("{number}");
            }
            //println!("{number} processed")
        }

        for offset in 1..won+1{
            counts[i+offset] += counts[i];
        }
        
        i+=1;
        //println!("total: {won}")
    }

    for c in counts{
        total += c;
        
    }
    println!("total: {total}")
}
// 21207< ans < 110344