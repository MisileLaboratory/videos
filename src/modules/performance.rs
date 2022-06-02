use std::time::Instant;

pub fn performance_check(repeat: u128) {
    let a: u128 = 0;
    let timer = Instant::now();
    
    loop {
        if (a == 1000) {
            break
        }
    }

    return timer.eslaped();
}