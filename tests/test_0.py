import pytest
from definition_5ed79f94d220423a943403a83410ca4a import calculate_variance

@pytest.mark.parametrize("budgeted, actual, expected", [
    (100.0, 150.0, 50.0),       # Overspending
    (200.0, 100.0, -100.0),     # Underspending
    (0.0, 0.0, 0.0),            # Zero budget and actual
    (50.0, 50.0, 0.0),          # Exact match
    (-100.0, -50.0, 50.0),      # Negative values
    (100.0, -50.0, -150.0)      # Actual less than zero
])
def test_calculate_variance(budgeted, actual, expected):
    assert calculate_variance(budgeted, actual) == expected

@pytest.mark.parametrize("budgeted, actual", [
    (100, "a string"),         # Invalid type: string
    ("100", 50),               # Invalid type: string
    (None, 50),                # None as budgeted
    (100, None),               # None as actual
    ([], 50),                  # Invalid type: list
    (100, {})                  # Invalid type: dict
])
def test_calculate_variance_type_errors(budgeted, actual):
    with pytest.raises(TypeError):
        calculate_variance(budgeted, actual)
