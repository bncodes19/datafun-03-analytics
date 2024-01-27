''' This module provides functions for creating a series of project folders. '''

import math
import statistics
import neely_analytics_utils
from pathlib import Path
import time

# Functions

def create_folders_for_range(start_year, end_year):
    """ Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years)."""
    for year in range(start_year, end_year):
        folder_name = "Year_"+str(year)
        Path(folder_name).mkdir(exist_ok=True)
        print(f"Folder {folder_name} has been created.")

def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    """ Function 2. For Item in List: Develop a function to create folders from a list of names."""
    for i in folder_list:
        if to_lowercase:
            i = i.lower()
        if remove_spaces:
            i = i.replace(" ", "")
        folder_list = str(i)
        Path(folder_list).mkdir(exist_ok=True)
        print(f"Folder {folder_list} has been created.")

def create_prefixed_folders (folder_list, prefix):
    """ Function 3. List Comprehension: Create a function to create prefixed folders by transforming"
        a list of names and combining each with a prefix (e.g., "data-")."""
    for i in folder_list:
        folder_list = str(prefix)+str(i)
        Path(folder_list).mkdir(exist_ok=True)
        print(f"Folder {folder_list} has been created.")

def create_folders_periodically(duration, iterations):
    """ Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds)."""
    i = 1
    while i <= iterations:
        folder_list = "folder_number_"+str(i)
        Path(folder_list).mkdir(exist_ok=True)
        print(f"Folder {folder_list} has been created.")
        i += 1
        time.sleep(duration)

# Main function

def main():
    ''' Main funciton to demeonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {neely_analytics_utils.byline}")

    # Call function 1 to create folders for a range (e. g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call funciton 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 1 # duration in seconds
    count_iterations = 3 # number of iterations to perform in the while loop
    create_folders_periodically(duration_secs, count_iterations)

    # Add options e.g., to force lowercase and remove spaces
    # to one or more of your functions (e.g. function 2)
    # Call your function and test these options
    regions = [
        "North America",
        "South America",
        "Europe",
        "Asia",
        "Africa",
        "Oceania",
        "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    print("All folders created. Processing complete!")

if __name__ == '__main__':
    main()