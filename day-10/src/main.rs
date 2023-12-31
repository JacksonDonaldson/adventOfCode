use std::fs;
use std::collections::HashSet;

struct Map{
    map: Vec<String>,
}

impl Map {
    fn access(&self, x: i32, y: i32) -> char{
        if x as usize >= self.map.len() || y as usize >= self.map[0].chars().count(){
            return 'X';
        }
        return self.map[x as usize].chars().nth(y as usize).unwrap();
    }
}

fn main() {
    let content = str::replace(&fs::read_to_string("input.txt").expect("Should have read file"), "\r", "");
    let split = content.split("\n");
    let mut vals: Vec<String> = Vec::new();
    
    for s in split{
        vals.push(s.to_string());
        println!("{s}");
    }
    let xlen = vals.len() as i32;
    let ylen = vals[0].chars().count() as i32;
    let map = Map{map: vals};

    let mut start = (0,0);
    for x in 0..xlen{
        for y in 0..ylen{
            if map.access(x, y) == 'S'{
                start = (x,y);
            }
        }
    }


    let mut x = start.0;
    let mut y = start.1;
    println!("start: {x},{y}");

    let mut dx: i32 = 1;
    let mut dy: i32 = 0;
    let mut current_char = 'X';

    let mut len = 0;

    let mut interiors = HashSet::new();
    let mut wall = HashSet::new();
    while current_char != 'S'{
        wall.insert((x,y));
        x += dx;
        y += dy;
        len += 1;

        current_char = map.access(x, y);
        match current_char{
        '|'=>{
            if dx == 1{
                interiors.insert((x, y-1));
            }
            else{
                interiors.insert((x, y+1));
            }
        }
        '-'=>{
            if dy == 1{
                interiors.insert((x+1, y));
            }
            else{
                interiors.insert((x-1, y));
            }
        }
        'L'=>{
            if dx == 1{
                //interiors.insert((x+1,y));
                //interiors.insert((x,y-1));
                //interiors.insert((x+1,y-1));
                dx = 0;
                dy = 1;
            }
            else{
                dx = -1;
                dy = 0;
            }
        }
        'J'=>{
            if dx == 1{
                dx = 0;
                dy = -1;
            }
            else{
                //interiors.insert((x+1, y));
                //interiors.insert((x, y+1));
                //interiors.insert((x+1, y+1));
                dx = -1;
                dy = 0;
            }
        }
        '7'=>{
            if dx == -1{
                //interiors.insert((x, y+1));
                //interiors.insert((x-1, y));
                //interiors.insert((x-1,y+1));
                dx = 0;
                dy = -1;
            }
            else{
                dx = 1;
                dy = 0;
            }
        }
        'F'=>{
            if dx == -1{
                dx = 0;
                dy = 1;
            }
            else{
                //interiors.insert((x-1, y));
                //interiors.insert((x, y-1));
                //interiors.insert((x-1,y-1));
                dx = 1;
                dy = 0;
            }
        }
        _=>{}
        }
    }
    println!("len: {len}");
    let mut inside = HashSet::new();

    for (x,y) in interiors{
        let mut search = Vec::new();
        search.push((x,y));
        while search.len() > 0{
            let pos = search.pop().unwrap();
            if inside.contains(&pos) || wall.contains(&pos){
                let xd = pos.0;
                let yd = pos.1;
                
                continue;
            }
            inside.insert(pos);
            for dx in [-1,1]{
                for dy in [-1,1]{
                    search.push((pos.0 + dx, pos.1 + dy));
                }
            }
        }
        
    }

    for (x,y) in &inside{
        println!("{x}, {y} in");
    }

    let total = inside.len();
    println!("total: {total}");

    for x in 0..xlen{
        for y in 0..ylen{
            if inside.contains(&(x,y)){
                print!("I");
            }
            else if wall.contains(&(x,y)){
                print!("w");
            }
            else{
                let c = map.access(x, y);
                print!("{c}");
            }
        }
        println!("");
    }
}
//not 15
//>103
//>110
//not 405