import pytest
import random
import sys

def calculate_grade(mark1, mark2, mark3):
    if not all(isinstance(mark, (int, float)) for mark in (mark1, mark2, mark3)):
        raise ValueError("All marks must be numbers")
   
    if not all(0 <= mark <= 100 for mark in (mark1, mark2, mark3)):
        raise ValueError("All marks must be between 0 and 100")

    average = (mark1 + mark2 + mark3) / 3
    if 90 <= average <= 100:
        return "First Class Distinction"
    elif 75 <= average < 90:
        return "First Class"
    elif 60 <= average < 75:
        return "Second Class"
    elif 50 <= average < 60:
        return "Third Class"
    else:
        return "Fail"

# Test cases
@pytest.mark.parametrize("marks, expected", [
    ((75, 80, 85), "First Class"),
    ((90, 95, 100), "First Class Distinction"),
    ((60, 65, 70), "Second Class"),
    ((50, 55, 58), "Third Class"),
    ((30, 40, 45), "Fail"),
    ((90, 90, 90), "First Class Distinction"),
    ((100, 100, 100), "First Class Distinction"),
    ((75, 75, 75), "First Class"),
    ((89, 89, 89), "First Class"),
    ((60, 60, 60), "Second Class"),
    ((74, 74, 74), "Second Class"),
    ((50, 50, 50), "Third Class"),
    ((59, 59, 59), "Third Class"),
    ((0, 0, 0), "Fail"),
    ((49, 49, 49), "Fail"),
    ((80.5, 85.5, 90.5), "First Class"),
])
def test_valid_inputs(marks, expected):
    assert calculate_grade(*marks) == expected

@pytest.mark.parametrize("marks", [
    (-1, 50, 75),
    (101, 80, 90),
    (80, "A", 90),
    (80, 85),
    (80, 85, 90, 95),
    (None, None, None),
    ("", "", ""),
])
def test_invalid_inputs(marks):
    with pytest.raises(ValueError):
        calculate_grade(*marks)

def test_fuzz():
    for _ in range(1000):
        marks = [random.uniform(-100, 200) for _ in range(3)]
        try:
            result = calculate_grade(*marks)
            assert result in ["First Class Distinction", "First Class", "Second Class", "Third Class", "Fail"]
        except ValueError:
            assert True  # Expected to raise ValueError for invalid inputs

def test_stress():
    for _ in range(10000):
        marks = [random.uniform(0, 100) for _ in range(3)]
        result = calculate_grade(*marks)
        assert result in ["First Class Distinction", "First Class", "Second Class", "Third Class", "Fail"]

@pytest.mark.parametrize("marks, expected", [
    ((sys.float_info.max, sys.float_info.max, sys.float_info.max), pytest.raises(ValueError)),
    ((sys.float_info.min, sys.float_info.min, sys.float_info.min), pytest.raises(ValueError)),
    ((float('inf'), float('inf'), float('inf')), pytest.raises(ValueError)),
    ((float('nan'), float('nan'), float('nan')), pytest.raises(ValueError)),
    (('', None, []), pytest.raises(ValueError)),
    ((complex(1,1), complex(2,2), complex(3,3)), pytest.raises(ValueError)),
    ((50.0000000001, 50.0000000001, 50.0000000001), "Third Class"),
])
def test_edge_cases(marks, expected):
    if isinstance(expected, type(pytest.raises(ValueError))):
        with expected:
            calculate_grade(*marks)
    else:
        assert calculate_grade(*marks) == expected
