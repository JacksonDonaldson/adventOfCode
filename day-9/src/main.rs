use std::fs;

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let split = content.split("\n");

    let mut sum = 0;
    for line in split{
        let mut dif_lists = Vec::new();

        let vals = line.split(" ");
        let mut first_line = Vec::new();
        for val in vals{
            first_line.push(val.parse::<i32>().unwrap());
        }
        dif_lists.push(first_line);
        
        loop{
            let mut next_list = Vec::new();
            let last_list = dif_lists.last().unwrap();
            let mut is_all_zero = true;
            for i in 1..last_list.len(){
                let dif = last_list[i] - last_list[i-1];
                if dif != 0{
                    is_all_zero = false;
                }
                next_list.push(dif);
            }
            dif_lists.push(next_list);
            if is_all_zero{
                break;
            }
        }

        let mut last_val = 0;
        for list in dif_lists.clone().into_iter().rev(){
            last_val = list[0] - last_val;
            //list.push(last_val);
        }
        sum+= last_val;
        println!("end value: {last_val}");
    }


    println!("sum: {sum}");
}
