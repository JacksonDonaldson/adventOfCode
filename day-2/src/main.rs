use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have read file");

    let split = contents.split("\n");

    let mut total = 0;
    for part in split {
        let mut temp = part.split(":");
        temp.next();
        let value = temp.next().expect("f");
        let draws = value.split(";");
        let mut max_r = 0;
        let mut max_g = 0;
        let mut max_b = 0;
        for draw in draws {
            let colors = draw.split(",");


            for color in colors{
                let mut values = color.split(" ");
                values.next();
                let count = values.next().expect("really?");
                let actual = values.next().expect("cmon").trim();

                let actual_count = count.parse::<i32>().unwrap();
                
                if actual == "red" && actual_count > max_r {
                    max_r = actual_count
                }
                if actual == "green" && actual_count > max_g {
                    max_g = actual_count;
                }
                if actual == "blue" && actual_count > max_b {
                    max_b = actual_count;
                }
            }
            
        }
        println!("Power: {max_b}, {max_r}, {max_g}");
        total += max_b * max_r * max_g;

        
        
    }
    println!("total: {total}")
    
}
// > 70263