"""Program to read a CSV file and write subset into JSON formatted file."""

import csv
import json

CSV_FILE = "netflix_titles.csv"
JSON_FILE = "netflix_tv_shows.json"
FILTER = "TV Show"
SELECTED_FIELDS = ["show_id", "title", "country", "date_added", "duration"]

def import_tv_shows(file_name: str) -> list:
    """Import csv file."""
    imported_csv = []
    try:
        csv_file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found.")
    else:
        with csv_file:
            for row in csv.DictReader(csv_file):
                imported_csv.append(row)
    return imported_csv


def filter_tv_shows(data: list, filter:str, selected_fields:list) -> list:
    """Return subset of data that matches "type" filter, with only selected_fields."""
    filtered_data = []
    for row in data:
        if row["type"] == filter:
            filtered_row = {field: row[field] for field in selected_fields}
            filtered_data.append(filtered_row)
    return filtered_data


def write_tv_shows(file_name: str, data: list) -> None:
    """Write data to JSON file."""
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    """Test CSV read and JSON write functions"""
    imported_csv = import_tv_shows(CSV_FILE)
    filtered_data = filter_tv_shows(imported_csv, FILTER, SELECTED_FIELDS)
    write_tv_shows(JSON_FILE, filtered_data)


if __name__ == "__main__":
    main()

