# quiz-02/test_solution.py
import pytest
from solution import calculate_grade

def test_valid_boundary_scores():
    # Arrange & Act & Assert
    assert calculate_grade(80) == "A"
    assert calculate_grade(79) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(59) == "F"

def test_out_of_range_scores_raise_value_error():
    with pytest.raises(ValueError):
        calculate_grade(-1)
    with pytest.raises(ValueError):
        calculate_grade(101)

def test_invalid_type_raises_type_error():
    with pytest.raises(TypeError):
        calculate_grade("eighty")