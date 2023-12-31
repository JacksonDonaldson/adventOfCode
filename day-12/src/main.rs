use std::fs;
use memoize::memoize;

#[memoize]
fn result(conditions: Vec<char>, lens: Vec<usize>) -> u64{
    
    if conditions.len() == 0{
        if lens.len() == 0{
            return 1;
        }
        return 0;
    }
    if lens.len() == 0{
        
        for c in conditions{
            if c == '#'{
                return 0;
            }
        }
        return 1;
    }

    if conditions[0] == '.'{
        return result(conditions[1..].to_vec(), lens);
    }

    if conditions[0] == '#'{
        if conditions.len() < lens[0]{
            return 0;
        }
        //must take next len now.
        for i in 0..lens[0]{
            if conditions[i] == '.'{
                return 0;
            }
        }
        if conditions.len() > lens[0] && conditions[lens[0]] == '#'{
            return 0;
        }
        if conditions.len() == lens[0]{
            if lens.len() == 1{
                return 1;
            }
            return 0;
        }
        return result(conditions[lens[0]+1..].to_vec(), lens[1..].to_vec());
    }

    //we must have a ?. Now we have to add some stuff up.
    let mut is_valid_take = true;

    if conditions.len() < lens[0]{
        is_valid_take = false;
    }
    else{
        for i in 0..lens[0]{
        
            if conditions[i] == '.'{
                is_valid_take = false;
                break;
            }
        }
    }

    if conditions.len() > lens[0] && conditions[lens[0]] == '#'{
        is_valid_take = false;
    }
    let mut total: u64 = 0;
    if is_valid_take{
        if lens[0] == conditions.len(){
            if lens.len() == 1{
                return 1;
            }
            return 0;
        }
        total += result(conditions[lens[0]+1..].to_vec(), lens[1..].to_vec())
    }

    total += result(conditions[1..].to_vec(), lens);

    return total;

}

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let split = content.split("\n");

    let mut total = 0;
    for line in split{

        let mut vals = line.split(" ");
        let code = vals.next().unwrap();
        let true_code = code.to_owned() + "?" + code + "?" + code + "?" + code + "?" + code;

        let points = vals.next().unwrap().split(",");
        
        let mut passed_in_points: Vec<usize> = Vec::new();
        for _ in 0..5{
            for p in points.clone(){
                passed_in_points.push(p.parse::<usize>().unwrap());
            }
        }
        
        let res = result(true_code.chars().collect(), passed_in_points);
        total += res;
        println!("Line: {code} {res}");
    }
    println!("total: {total}");
}
