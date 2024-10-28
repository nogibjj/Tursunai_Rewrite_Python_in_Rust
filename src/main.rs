mod db_operations;

use rusqlite::Connection;
use std::fs::File;
use std::io::Write;
use std::time::Instant;

fn main() {
    // Start timing
    let start = Instant::now();

    let file_path = "data/urbanization.csv";
    let conn = Connection::open("urbanizationDB.db").expect("Failed to open database.");

    // Extract data
    db_operations::extract(
        "https://github.com/fivethirtyeight/data/raw/refs/heads/master/urbanization-index/urbanization-census-tract.csv",
        file_path,
    ).expect("Failed to extract data");

    // Load data into SQLite
    db_operations::load_data(file_path).expect("Failed to load data");

    // Example CRUD operations
    db_operations::create_record(
        &conn,
        ("01", "Alabama", "G0100010", 34.0, -86.0, 10000, 200.0, 0.8),
    )
    .expect("Failed to create record");

    let data = db_operations::read_data(&conn).expect("Failed to read data");
    for record in data {
        println!("{:?}", record);
    }

    // Update a record using UpdateRecordParams
    let update_params = db_operations::UpdateRecordParams {
        gisjoin: "G0100010",
        state: "Alabama",
        lat_tract: 34.1,
        long_tract: -86.1,
        population: 10001,
        adj_radiuspop_5: 201.0,
        urbanindex: 0.9,
    };
    db_operations::update_record(&conn, update_params).expect("Failed to update record");

    // Delete a record
    db_operations::delete_record(&conn, "G0100010").expect("Failed to delete record");

    // End timing
    let duration = start.elapsed();

    // Write execution time to file
    let mut file = File::create("rust_time.md").expect("Unable to create file");
    write!(file, "Execution time: {:?}", duration).expect("Unable to write data");
}
