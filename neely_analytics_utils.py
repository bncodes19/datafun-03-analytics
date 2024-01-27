''' This module provides a reusable byline for the author's services. '''

import math
import statistics

# Variables
company_name: str = 'Neely Data Analytics'
count_active_projects: int = 5
count_completed_projects: int = 3
number_of_employees: int = 1
specialties: list = ["Data Cleaning", "Data Normalization", "Data Pipelines", "Data Science", "Data Visualization"]
industries: list = ["Energy", "Telecommunications", "Hospitality"]
net_promotor_score: set = {9.4, 8.2, 3.1, 7.6, 2.9, 4.8, 6.1, 3.9, 10.9, 5.0, 8.2, 5.6, 3.6}

# Formatted Strings
active_projects_string: str = f"Projects in progress: {count_active_projects}"
completed_projects_string: str = f"Projects we've shipped: {count_completed_projects}"
specialties_offered: str = f"Specialties we offer: {specialties}"
industries_served: str = f"Industries we serve: {industries}"

# Calculate Descriptive Statistics
lowest_score = min(net_promotor_score)
highest_score = max(net_promotor_score)
total_scores = len(net_promotor_score)
mean = statistics.mean(net_promotor_score)
rounded_mean = round(statistics.mean(net_promotor_score))
mode = statistics.mode(net_promotor_score)

# Statistics String: 
stats_string: str = f"""
Descriptive Statistics for {company_name} Net Promotor Score:
Lowest Score: {lowest_score}
Highest Score: {highest_score}
Total Scores: {total_scores}
Mean: {mean}, Rounded Mean: {rounded_mean}
Mode: {mode}
"""

# Byline
byline: str = f"""
{company_name}
{active_projects_string}
{completed_projects_string}
{number_of_employees}
{specialties_offered}
{industries_served}
{stats_string}
"""

# Function
def main():
    '''Display entire output'''
    (company_name)
    (active_projects_string)
    (completed_projects_string)
    (number_of_employees)
    (specialties_offered)
    (industries_served)
    (stats_string)

if __name__ == '__main__':
    main()