import pytest
import csv
from main import check_age  

csv_file = 'test_results.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Input Age', 'Expected Result', 'Actual Result', 'Valid/Invalid'])

def write_to_csv(age, expected, actual):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        valid_invalid = 'Valid' if expected == actual else 'Invalid'
        writer.writerow([age, expected, actual, valid_invalid])

def run_test_cases(test_cases):
    for age, expected in test_cases:
        actual = check_age(age)
        write_to_csv(age, expected, actual)
        assert actual == expected

def test_check_age():
    test_cases_valid = [
        (50, True),
        (1, True),
        (100, True),
    ]
    
    test_cases_invalid = [
        (0, False),
        (101, False),
        (200, False),
    ]

    run_test_cases(test_cases_valid)
    run_test_cases(test_cases_invalid)
