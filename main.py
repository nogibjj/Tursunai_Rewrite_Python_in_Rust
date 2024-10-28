"""
ETL-Query script
"""

import argparse
import sys
import time
import tracemalloc  # Import for memory usage tracking
from datetime import datetime  # Import for timestamp
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import general_query, create_rec, update_rec, delete_rec, read_data


# Handle arguments function
def handle_arguments(args):
    """Handles actions based on initial calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")

    # Define the action argument
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_rec",
            "delete_rec",
            "create_rec",
            "general_query",
            "read_data",
        ],
    )

    # Parse only the action first
    action_args, remaining_args = parser.parse_known_args(args[:1])
    action = action_args.action

    # Define specific arguments for each action
    if action == "extract":
        parser.add_argument(
            "--url",
            default="https://github.com/fivethirtyeight/data/raw/refs/heads/master/urbanization-index/urbanization-census-tract.csv",
        )
        parser.add_argument("--file_path", default="data/urbanization.csv")

    if action == "transform_load":
        parser.add_argument("--dataset", default="data/urbanization.csv")

    if action == "create_rec":
        parser.add_argument("statefips", type=int)
        parser.add_argument("state")
        parser.add_argument("gisjoin")
        parser.add_argument("lat_tract", type=float)
        parser.add_argument("long_tract", type=float)
        parser.add_argument("population", type=int)
        parser.add_argument("adj_radiuspop_5", type=float)
        parser.add_argument("urbanindex", type=float)

    if action == "update_rec":
        parser.add_argument("statefips", type=int)
        parser.add_argument("state")
        parser.add_argument("gisjoin")
        parser.add_argument("lat_tract", type=float)
        parser.add_argument("long_tract", type=float)
        parser.add_argument("population", type=int)
        parser.add_argument("adj_radiuspop_5", type=float)
        parser.add_argument("urbanindex", type=float)

    if action == "delete_rec":
        parser.add_argument("gisjoin")

    if action == "general_query":
        parser.add_argument("query")

    # Parse again with the remaining arguments specific to the action
    full_args = parser.parse_args(args)
    return full_args


def main():
    # Start memory tracking and timing
    tracemalloc.start()
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Execute main logic
    args = handle_arguments(sys.argv[1:])
    result = f"Action performed: {args.action}"

    if args.action == "extract":
        extract(args.url, args.file_path)
    elif args.action == "transform_load":
        load(args.dataset)
    elif args.action == "create_rec":
        create_rec(
            args.statefips,
            args.state,
            args.gisjoin,
            args.lat_tract,
            args.long_tract,
            args.population,
            args.adj_radiuspop_5,
            args.urbanindex,
        )
    elif args.action == "update_rec":
        update_rec(
            args.statefips,
            args.state,
            args.gisjoin,
            args.lat_tract,
            args.long_tract,
            args.population,
            args.adj_radiuspop_5,
            args.urbanindex,
        )
    elif args.action == "delete_rec":
        delete_rec(args.gisjoin)
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        result = f"Data read: {data}"

    # End timing and memory usage tracking
    end_time = time.time()
    elapsed_time = (
        end_time - start_time
    ) * 1_000_000  # Convert seconds to microseconds
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_used_kb = peak / 1024  # Convert bytes to kilobytes

    # Append results to file in the specified format
    with open("python_time.md", "a") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"The action was: {args.action}\n")
        file.write(f"Result: {result}\n")
        file.write(f"Elapsed time: {elapsed_time:.2f} microseconds\n")
        file.write(f"Memory used: {memory_used_kb:.2f} kB\n")
        file.write("\n" + "-" * 40 + "\n\n")  # Divider for readability


if __name__ == "__main__":
    main()
