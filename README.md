[![Rust CI/CD Pipeline](https://github.com/tursunait/Individual_Project_2_Tursunai_DE/actions/workflows/cicd.yml/badge.svg)](https://github.com/tursunait/Individual_Project_2_Tursunai_DE/actions/workflows/cicd.yml) [![CI](https://github.com/nogibjj/Tursunai_Rewrite_Python_in_Rust/actions/workflows/pycicd.yaml/badge.svg)](https://github.com/nogibjj/Tursunai_Rewrite_Python_in_Rust/actions/workflows/pycicd.yaml)

# Urbanization Data Processing Project: Converting Python script to Rust
### By Tursunai Turumbekova

## Project Overview

This project demonstrates a comparative analysis between Python and Rust implementations for processing urbanization data and interacting with an SQLite database. Both versions support CRUD (Create, Read, Update, and Delete) operations and include a CI/CD pipeline to ensure code functionality. The project also highlights improvements in speed and resource usage achieved by rewriting the Python script in Rust.

### Key Features:
- **Data Extraction and Loading**: Extracts data from a URL and loads it into an SQLite database.
- **CRUD Operations**: Supports creating, reading, updating, and deleting records in the database.
- **Performance Comparison**: Analyzes and documents speed and memory usage differences between Python and Rust implementations.
- **CI/CD Pipeline**: Uses GitHub Actions for continuous integration and deployment.
- **Command-Line Interface (CLI)**: Executes operations via the command line.

## Project Structure

```plaintext
TURSUNAI_REWRITE_PYTHON_IN_RUST/
├── __pycache__/
├── .devcontainer/
├── .github/
│   └── workflows/
│       ├── pycicd.yaml                 # CI/CD pipeline configuration for Python
│       └── rustcicd.yaml               # CI/CD pipeline configuration for Rust
├── .pytest_cache/
├── .ruff_cache/
├── data/
├── mylib/                              # Python library containing data processing functions
│   ├── __pycache__/
│   ├── __init__.py                     # Package initializer for mylib
│   ├── extract.py                      # Data extraction module
│   ├── query.py                        # Module for SQL queries and CRUD operations
│   └── transform_load.py               # Module for data transformation and loading
├── src/                                # Rust source code
│   ├── db_operations.rs                # Rust module for database operations
│   └── main.rs                         # Main Rust program entry point
├── target/                             # Rust build artifacts (auto-generated)
├── .coverage                           # Code coverage report for Python tests
├── .gitignore                          # Git ignore file
├── Cargo.lock                          # Lock file for Rust dependencies
├── Cargo.toml                          # Rust project manifest
├── LICENSE                             # Project license
├── main.py                             # Main Python script for database operations via CLI
├── Makefile                            # Makefile with automation commands
├── pyproject.toml                      # Python project configuration
├── python_time.md                      # Log of Python script execution times and memory usage
├── query_log.md                        # Log of SQL queries executed in the project
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── rust_time.md                        # Log of Rust script execution times and memory usage
├── test_main.py                        # Python unit tests
├── test_main.rs                        # Rust unit tests
└── urbanizationDB.db                   # SQLite database for urbanization data
```

## Installation
### Python Setup
Clone the repository:

```bash
git clone https://github.com/tursunait/Individual_Project_2_Tursunai_DE.git
cd Individual_Project_2_Tursunai_DE
```
Set up a virtual environment and install dependencies:

```bash
python -m venv myenvironment
source myenvironment/bin/activate  # On Windows use: myenvironment\Scripts\activate
pip install -r requirements.txt
```

### Rust Setup

Ensure Rust is installed. If not, install it via:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
Build the Rust dependencies:

```bash
cd rust_script
cargo build
```
## Usage
### Python CLI Commands

Run the following commands in the py_script_with_SQLDatabase directory to perform CRUD operations:

Create a Record:

```bash
python main.py create_rec 1 'Alabama' 'G0100010' 32.3182 -86.9023 50000 100.5 1.0
```

Read Data:

```bash
python main.py read_data
```

Update a Record:

```bash
python main.py update_rec 1 'Alabama' 'G0100010' 32.3182 -86.9023 60000 120.5 2.0
```
Delete a Record:

```bash
python main.py delete_rec 'G0100010'
```

### Rust CLI Commands
To perform the same CRUD operations in Rust, navigate to the rust_script directory and run:

Create a Record:

```bash
cargo run -- create "01" "Alabama" "G0100010" 34.0 -86.0 10000 200.0 0.8
```

Read Data:

```bash
cargo run -- read
```

Update a Record:

```bash
cargo run -- update "G0100010" "Alabama" 34.1 -86.1 10001 201.0 0.9
```

Delete a Record:

```bash
cargo run -- delete "G0100010"
```
## Speed and Resource Usage

- [Rust Runtime Logs](rust_time.md)
- [Python Runtime Logs](python_time.md)

This project includes a performance comparison between Rust and Python for database operations. Below is a summary of the findings based on runtime logs:

### Performance Analysis

Based on the runtime data, Rust performs the same database operations significantly faster and with less memory usage compared to Python. Here are some key points of the performance comparison:

- **Execution Speed**:
  - **Rust**: Operations completed in approximately 16-17 seconds on average for comprehensive database tasks.
  - **Python**: Individual actions such as `create_rec`, `update_rec`, and `delete_rec` are quicker in isolation but become slower with complex operations like `read_data` (which took approximately 1.4 seconds).
  - Overall, Rust's static typing, zero-cost abstractions, and efficient memory handling allow it to perform complex tasks more efficiently across the board.

- **Memory Usage**:
  - **Rust**: Consumes minimal memory, averaging around 130 kB or less, with some fluctuations observed due to direct memory management.
  - **Python**: Memory usage is significantly higher, particularly in data-heavy operations like `read_data`, which consumed over 39 MB of memory.

### Detailed Comparison

| Language | Action             | Elapsed Time (microseconds) | Memory Used       |
|----------|--------------------|-----------------------------|-------------------|
| Rust     | Database Ops(avg)  | ~16,000                     | ~130 kB           |
| Python   | create_rec         | 4,449                       | 32.02 kB          |
| Python   | update_rec         | 6,724                       | 32.02 kB          |
| Python   | delete_rec         | 15,637                      | 15.73 kB          |
| Python   | read_data          | 1,395,103                   | 39,307.19 kB      |
| Python   | general_query      | 6,409                       | 16.80 kB          |


This comparison demonstrates Rust’s suitability for performance-critical applications, where both speed and memory efficiency are crucial.

## CI/CD Pipeline
The CI/CD pipeline, configured in .github/workflows/ci_cd.yml, includes the following steps:

Linting and Testing: Ensures code quality using ruff for Python and clippy for Rust.
Build: Compiles the Rust code.
Tests: Runs unit tests for both Python and Rust.
Artifact Upload: Archives the optimized Rust binary.
Running Linting, Testing, and Formatting Locally
Run Format:

```bash
make format
```
Lint Code:

```bash
make lint
```

Run Tests:

```bash
make test
```
## Makefile Commands
The Makefile includes commands for commonly used tasks:

make rust-version: Displays Rust version.
make lint: Runs code linting.
make test: Runs tests for both Python and Rust scripts.
make release: Builds the Rust project in release mode.

## Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.