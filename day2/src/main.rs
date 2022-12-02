use reqwest;

static SESSION: &'static str = "session=XXX";


fn score(a: char, b: char) -> i32 {
    let mut result = b as i32 - 87;
    let d: i32 = (b as i32 - 23 - a as i32).try_into().unwrap();
    if d == 0 {
        result += 3;
    }
    else if d == 1 || d == -2 {
        result += 6
    }
    return result;
}

fn score_two(a: char, b: char) -> i32 {
    return 0;
}


fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = get_input(2, 2022)?;
    let split_input = input.split('\n');
    let mut total = 0;
    for i in split_input {
        let pieces: Vec<&str> = i.split(' ').collect();
        if pieces.len() != 2 {
            continue
        }
        total += score(pieces[0].chars().nth(0).unwrap(), pieces[1].chars().nth(0).unwrap())
    }
    println!("Got score {}", total);
    Ok(())
}


fn get_input(day: i16, year: i16) -> Result<String, Box<dyn std::error::Error>> {
    let http_client = reqwest::blocking::Client::new();
    let url = format!("https://adventofcode.com/{}/day/{}/input", year, day);
    let response = http_client
        .get(url)
        .header(reqwest::header::COOKIE, SESSION)
        .send()?
        .text()?;
    Ok(response)
}