"""
Starter code: Fetch covid cases data for Utah from the CDC API

Dataset:
Weekly United States COVID-19 Cases by State (ARCHIVED)

IMPORTANT:
- This dataset is WEEKLY, not daily.  The day shown is the end of week date.
- This starter code prints RAW JSON text.
- You are expected to parse and analyze the data.
"""
# IMPORTS

import csv
import requests
from datetime import datetime
import json


# REMEMBER, The outer loop handles states; the inner loops handle that state's COVID records.

# CSV SECTION
populations = {} # empty list

with open("states.csv", "r") as file: # reading in the csv
    reader = csv.DictReader(file)

    for row in reader:
        state = row["STATE_ABBREV"] # creating the states variable
        population = int(row["POPULATION"]) # creating the pop variable ang making it an int

        populations[state] = population 

# STATE NAME DICTIONARY
state_names = { # going from abbrev to full names for output
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


# API SECTION
DATASET_ID = "pwn4-m3yp"

BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# VARIABLES FOR OVERALL SUMMARY
highest_percentage = None
lowest_percentage = None

highest_state = None
lowest_state = None

highest_month_high = None
highest_cases_high = None
highest_population = None

lowest_month_low = None
lowest_cases_low = None
lowest_population = None

# LOOP THROUGH EACH STATE
for state, population in populations.items(): # starting loop that'll loop for each state

    state_name = state_names[state]

    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }

    req = requests.get(BASE_URL, params=params)

    data = req.json()

    # SAVE RAW JSON DATA
    with open(f"{state}.json", "w") as file:
        json.dump(data, file, indent=4) # making the string readable

    # AVERAGE CALCULATION
    weekly_cases = [] # empty list

    for record in data:
        cases = float(record["new_cases"]) # creating case variable
        weekly_cases.append(cases)

    average_cases = sum(weekly_cases) / len(weekly_cases) # calculation


    # WEEK WITH HIGHEST # OF CASES
    highest_record = max(data, key=lambda record: float(record["new_cases"]))

    highest_cases = float(highest_record["new_cases"])
    highest_date = highest_record["end_date"][:10] # :10 helps clean the date

    print(
    "Date with the highest new number of covid cases:",
    highest_date,
    "(",
    int(highest_cases),
    ")"
)

    # CALCULATING MONTH WITH HIGHEST TOTAL CASES
    monthly_cases = {} # new list for holding each months cases

    for record in data:
        date = datetime.strptime(record["end_date"][:10], "%Y-%m-%d")
        month_year = date.strftime("%B %Y")
        cases = float(record["new_cases"]) # cleaning up the output

        if month_year not in monthly_cases:
            monthly_cases[month_year]= 0 

        monthly_cases[month_year] += cases # calculation 

# print each month's total 
    highest_month = max(monthly_cases, key=monthly_cases.get)
    highest_month_cases = monthly_cases[highest_month]

    # calculate percentage of state population
    percentage = (highest_month_cases / population) * 100

    # CHECK FOR HIGHEST PERCENTAGE ACROSS ALL STATES
    if highest_percentage is None or percentage > highest_percentage:
        highest_percentage = percentage
        highest_state = state_name
        highest_month_high = highest_month
        highest_cases_high = highest_month_cases
        highest_population = population


    # CHECK FOR LOWEST PERCENTAGE ACROSS ALL STATES
    if lowest_percentage is None or percentage < lowest_percentage:
        lowest_percentage = percentage
        lowest_state = state_name
        lowest_month_low = highest_month
        lowest_cases_low = highest_month_cases
        lowest_population = population


    # PRINT RESULTS FOR THIS STATE
    print()
    print("State name:", state_name)

    print(
        "Average number of new weekly cases for the entire state dataset:",
        round(average_cases, 2)
    )

    print(
        "Date with the highest new number of covid cases:",
        highest_date,
        "(",
        int(highest_cases),
        ")"
    )

    print(
        "Month and Year, with the highest new number of covid cases:",
        highest_month,
        "(",
        int(highest_month_cases),
        ")"
    )

    print(
        "Month and Year, with highest new number, percentage of population:",
        str(round(percentage, 2)) + "% (Population: " + str(population) + ")"
    )

    print()
    print("------------------------------------------------------------")


# SUMMARY ACROSS ALL STATES
print()
print("==================== SUMMARY ACROSS ALL STATES ====================")

print()
print("State with HIGHEST percentage of population during its highest month:")

print(
    highest_state + " - " +
    str(round(highest_percentage, 2)) + "% in " +
    highest_month_high + " (" +
    str(int(highest_cases_high)) + " cases; Population: " +
    str(highest_population) + ")"
)

print()
print("State with LOWEST percentage of population during its highest month:")

print(
    lowest_state + " - " +
    str(round(lowest_percentage, 2)) + "% in " +
    lowest_month_low + " (" +
    str(int(lowest_cases_low)) + " cases; Population: " +
    str(lowest_population) + ")"
) # printing format that matches the example

# https://chatgpt.com/share/6ac01296-1784-83ea-a6c5-ce3d9289d43a chat link
