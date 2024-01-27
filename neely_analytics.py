# Module 3
""" This file fetches data from the web and saves to files inside defined folders.
The data includes Text, CSV, Excel, and JSON file types.
"""

# Standard library imports
import csv
import pathlib
import json
from pathlib import Path

# External library imports (requires virtual environment)
import requests

# Local module imports
import neely_analytics_utils
import neely_projsetup

# Fetch a text file from the web and write to a folder and directory
def fetch_text_data(url, folder_name, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        write_text_data(response.text, folder_name, file_name)
    else:
        return None

# Text write function
def write_text_data(data, folder_name, file_name):
    file_path = Path(folder_name, file_name)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        file.write(data)

# Fetch a CSV file from the web and write to a folder and directory
def fetch_csv_data(url, folder_name, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_data(response.text, folder_name, file_name)
    else:
        return None

# CSV write function
def write_csv_data(data, folder_name, file_name):
    file_path = Path(folder_name, file_name)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w', newline='') as file:
        file.write(data)

# Fetch an Excel file from the web and write to a folder and directory
def fetch_excel_data(url, folder_name, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_data(response.text, folder_name, file_name)
    else:
        return None

# Excel write function
def write_excel_data(data, folder_name, file_name):
    file_path = Path(folder_name, file_name)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        file.write(data)

# Fetch a JSON file from the web and write to a folder and directory
def fetch_json_data(url, folder_name, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_data(response.content, folder_name, file_name)
    else:
        return None

# JSON write function
def write_json_data(data, folder_name, file_name):
    file_path = Path(folder_name, file_name)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('wb') as file:
         file.write(data)

# Main function utilizing file inputs to call functions
def main():

    # Byline declaration
    print(f"Byline: {neely_analytics_utils.byline}")

    # Text inputs
    text_url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
    text_folder_name = 'folder-text'
    text_file_name = 'data.txt'

    # CSV inputs
    csv_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
    csv_folder_name = 'folder-csv'
    csv_file_name = 'data.csv'

    # Excel inputs
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/inflation.xls'
    excel_folder_name = 'folder-excel'
    excel_file_name = 'data.xls'

    # JSON inputs
    json_url = 'https://anapioficeandfire.com/api/characters/583'
    json_folder_name = 'folder-json'
    json_file_name = 'data.json'

    # Call functions to fetch data from the web and write to folders and files
    fetch_text_data(text_url, text_folder_name, text_file_name)
    fetch_csv_data(csv_url, csv_folder_name, csv_file_name)
    fetch_excel_data(excel_url, excel_folder_name, excel_file_name)
    fetch_json_data(json_url, json_folder_name, json_file_name)

if __name__ == "__main__":
    main()
