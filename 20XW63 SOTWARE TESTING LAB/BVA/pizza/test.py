import pytest
from main import check_pizza  
import csv

def test_check_pizza():
    test_cases = [
        (1, "Success"),                         # Valid order
        (10, "Success"),                        # Valid order
        (11, "Invalid order quantity"),         # Invalid (greater than 10)
        (0, "Invalid order quantity"),          # Invalid (less than 1)
        (-1, "Invalid order quantity"),         # Invalid (negative number)
        (100, "Invalid order quantity"),        # Invalid (3-digit number)
        (-100, "Invalid order quantity")        # Invalid (negative 3-digit number)
    ]

    results = []

    for count, expected in test_cases:
        result = check_pizza(count)
        assert result == expected, f"Test failed for count: {count}. Expected: {expected}, Got: {result}"
        results.append({
            "Test Case": count,
            "Expected": expected,
            "Actual": result,
            "Outcome": "Passed" if result == expected else "Failed"
        })

    # Write results to a CSV file
    with open('test_results.csv', 'w', newline='') as csvfile:
        fieldnames = ["Test Case", "Expected", "Actual", "Outcome"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

# Run the test case (this will be handled by pytest when executed in the terminal)
if __name__ == "__main__":
    pytest.main()