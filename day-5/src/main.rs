use std::fs;
fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");

    let seeds = str::replace(&fs::read_to_string("seeds.txt").expect("Should have read file"), "\r", "");

    let mut maps = Vec::new();
    let mut map = Vec::new();
    for line in content.split("\n"){
        if line == ""{
            maps.push(map);
            map = Vec::new();
            println!();
            continue
        }
        if line.contains(":"){
            continue;
        }
        let mut values = line.split(" ");
        let start = values.next().unwrap().parse::<i64>().unwrap();
        let end = values.next().unwrap().parse::<i64>().unwrap();
        let range = values.next().unwrap().parse::<i64>().unwrap();

        map.push((start, end, range));
        //println!("{start} {end} {range}");

    }

    let mut it = seeds.split(" ").peekable();
    let mut current_ranges = Vec::new();
    while !it.peek().is_none(){
        let seed = it.next().unwrap().parse::<i64>().unwrap();
        let range = it.next().unwrap().parse::<i64>().unwrap();
        
        current_ranges.push((seed, range));
        //let mut current_value = seed.parse::<i64>().unwrap();
    }

    for map in &maps{
        println!("mapping");
        // for range in &current_ranges{
        //     let zero = range.0;
        //     let one = range.1;
        //     // print!("{zero}, {one}    ");
        // }
        // println!("");

        let mut new_ranges = Vec::new();
        for tuple in map{
            let src_start = tuple.1;
            let dst_start = tuple.0;
            
            let range = tuple.2;
            
            let src_end = src_start + range;
            let dst_end = dst_start + range;
            // println!("map: {src_start}, {range}, {dst_start}");
            
            //for each range in the current valid set of ranges:
            //handle overlapping cases. new_current_ranges holds all this.
            let mut new_current_ranges = Vec::new();

            for range in current_ranges{
                let start = range.0;
                let len = range.1;
                
                if src_start >= (start + len){
                    new_current_ranges.push((start, len));
                    // println!("1. Adding {start}, {len}");
                    continue;
                }
                if src_end <= start{
                    new_current_ranges.push((start, len));
                    // println!("2. Adding {start}, {len}");
                    continue;
                }
                //there is some overlap. Determine what
                if src_end >= (start + len) && src_start <= start{
                    new_ranges.push((dst_start + (start - src_start), len));
                    // println!("6. Adding {start}, {src_start}");
                }
                else if src_end >= (start + len){
                    new_current_ranges.push((start, src_start - start));
                    // println!("3. Adding {start}, {src_start}");
                    new_ranges.push((dst_start, start + len - src_start));
                }
                else if start >= src_start{
                    new_current_ranges.push((src_end, len - (src_end - start)));
                    // println!("4. Adding {src_end}, {len}");
                    new_ranges.push((dst_start + (start-src_start), (src_end - start)));
                }
                else{
                    // println!("5. Adding {start}, {src_start}");
                    new_current_ranges.push((start, (src_start - start)));
                    new_current_ranges.push((src_end, len - (src_end - start)));
                    new_ranges.push((dst_start, (dst_end - dst_start)));
                }
            }
            current_ranges = new_current_ranges;
        }

        new_ranges.extend(current_ranges);
        current_ranges = new_ranges;
        
    }

    let mut min_value = 9999999999999;
    for range in &current_ranges{

        let zero = range.0;
        //let one = range.1;

        if zero < min_value{
            min_value = zero;
        }
        //print!("{zero}, {one}    ");
    }
    println!("min: {min_value}");
}
