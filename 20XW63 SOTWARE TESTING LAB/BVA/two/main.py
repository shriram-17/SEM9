import csv

def validate_password_length(password: str) -> bool:
    return 6 <= len(password) <= 12

def run_test_cases():
    test_cases = [
        ("abcde", False),            # Case 1: Less than 6 characters (Invalid)
        ("abcdef", True),            # Case 2: Exactly 6 characters (Valid)
        ("abcdefgh", True),          # Case 3: Between 7 and 11 characters (Valid)
        ("abcdefghijkl", True),      # Case 4: Exactly 12 characters (Valid)
        ("abcdefghijklm", False)     # Case 5: More than 12 characters (Invalid)
    ]
    
    results = []

    for i, (password, expected) in enumerate(test_cases, 1):
        result = validate_password_length(password)
        outcome = "Passed" if result == expected else "Failed"
        results.append({
            "Test Case": i,
            "Password": password,
            "Expected": expected,
            "Actual": result,
            "Outcome": outcome
        })
        print(f"Test Case {i} {outcome}")

    # Write results to a CSV file
    with open('test_results.csv', 'w', newline='') as csvfile:
        fieldnames = ["Test Case", "Password", "Expected", "Actual", "Outcome"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)

run_test_cases()
