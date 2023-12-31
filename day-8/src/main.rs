use std::fs;
use std::collections::HashMap;


fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let dirs = "LRRLRRRLRRRLLRRLRRLRLRLRRLLRRLRRLRRRLLLRRRLRRRLRRRLLRRRLRRLLRRLRRLRLRRRLRRLRLRRLRRRLLRRLLRLRRRLLRRLRRLLLRLRRRLRLRLRLLRRRLRLLRRRLRLRRRLRRRLLRRLRRRLLRRLRLLRLRRLLLRRLRRLLLRLLRLRRRLRLRLRRRLRRLLRRRLRLRLRRLRRRLRLRRLRRLRRRLRRRLRRRLRRRLRRLLRRLRLLRRLLRRRLRLLRLRLRRLRRLRLRLRRRLRLRLRRLRLRRLRRRR";
    //let dirs = "LR";
    let mut map = HashMap::new();
    let mut starts = Vec::new();

    for val in content.split("\n"){
        let mut v = val.split(" = (");
        let label = v.next().unwrap();
        let mut nexts = v.next().unwrap().split(", ");
        let left = nexts.next().unwrap();
        let right_w_paren = nexts.next().unwrap();
        let right: String = right_w_paren.chars().take(right_w_paren.len() - 1).collect();
        //println!("{right}");
        map.insert(label, (left, right));
        if label.chars().nth(2).unwrap() == 'A'{
            starts.push(label);
        }
    }

    let mut i = 0;
    //let mut current = "AAA";
    //let mut saved_start_nodes = starts.copy();
    //let mut dists = Vec::new();

    let len = starts.len();
    println!("len: {len}");

    loop{
        for d in dirs.chars(){

            if d == 'R'{
                for i in 0..starts.len(){
                    starts[i] = &map[starts[i]].1;
                }
                //current = &map[current].1;
            }
            else{
                for i in 0..starts.len(){
                    starts[i] = &map[starts[i]].0;
                }
                //current = &map[current].0;
            }
            i+=1;
            //let mut is_done = true;
            for j in 0..6{
                if starts[j].chars().nth(2).unwrap() == 'Z'{
                    println!("{j} at {i} found");
                }
            }
            
            
        }
    }

}

//0: 14999, 29998, 44997
//1: 20093
//2: 17263
//3: 16697
//4: 12169
//5: 20659
// < 24061561718938 