
from grades import compute_hw_average
"""
Helps with the grades 1
Especially the average 2 
"""

def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42
