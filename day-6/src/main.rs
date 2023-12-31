fn main() {
    //let vals = [(62, 644), (73, 1023), (75, 1240), (65, 1023)];

    let upper =
    let vals 
    let mut total = 1;
    for point in vals{
        let time = point.0;
        let dist = point.1;
        let mut success = 0;
        for i in 0..time{
            if i * (time-i) > dist{
                success += 1;
            }
        }
        total *= success;
    }
    println!("total: {total}");
}

//part 2: times = 62737565
//dis = 644102312401023
//time upper bound: 49805110
//lower bound: 12932455
// > 36872655 (off by 1)