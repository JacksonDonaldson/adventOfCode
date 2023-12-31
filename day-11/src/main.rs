use std::fs;

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let split = content.split("\n");

    let numtimes = 2;

    let mut rows: Vec<Vec<char>> = Vec::new();
    for row in split{
        rows.push(row.chars().collect());
    }

    let rowlen = rows[0].len();
    let mut expands = Vec::new();
    
    for (i, row) in rows.iter().enumerate(){
        let mut is_empty = true;
        for c in row{
            if *c != '.'{
                is_empty = false;
            }
        }
        if is_empty{
            expands.push(i);
        }
    }

    for (count, i) in expands.iter().enumerate(){

        for _ in 0..numtimes{
            let mut insert = Vec::new();
            for _c in 0..rowlen{
                insert.push('.');
            }
            rows.insert(i+count*numtimes, insert);
        }
    }

    

    let collen = rows.len();

    let mut colinserts = Vec::new();
    for i in 0..rowlen{
        let mut is_empty = true;
        for j in 0..collen{
            if rows[j][i] != '.'{
                is_empty = false;
            } 
        }
        if is_empty{
            colinserts.push(i);
        }
    }

    for (i, col) in colinserts.iter().enumerate(){
        for j in 0..collen{
            for _  in 0..numtimes{
                rows[j].insert(i*numtimes+col, '.');
            }
            
        }
    }

    //for line in &rows{
        //for c in line{
       //     print!("{c}");
      //  }
     //   println!();
    //}

    let mut locations = Vec::new();
    for row in 0..rows.len(){
        for col in 0..rows[0].len(){
            if rows[row][col] != '.'{
                locations.push((row, col));
            }
        }
    }

    let mut total = 0;
    for i in 0..locations.len(){
        for j in i+1..locations.len(){
            let xdiff = locations[i].0.abs_diff(locations[j].0);
            let ydiff = locations[i].1.abs_diff(locations[j].1);
            //println!("{i}, {j}, {xdiff}, {ydiff}");
            total += xdiff + ydiff;
        }
    }
    println!("total: {total}");
}
