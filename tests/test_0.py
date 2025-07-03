import pytest
from definition_aad47934f03a4a95ba3c7144de701840 import calculate_variance

@pytest.mark.parametrize("budgeted, actual, expected", [
    # Standard cases: actual > budgeted (overspending)
    (100, 120, 20),
    (100.0, 120.5, 20.5),
    (50, 75.5, 25.5),
    (123.45, 124.45, 1.0),

    # Standard cases: actual < budgeted (underspending)
    (100, 80, -20),
    (120.5, 100.0, -20.5),
    (75.5, 50, -25.5),
    (124.45, 123.45, -1.0),

    # Standard cases: actual == budgeted (no variance)
    (100, 100, 0),
    (100.0, 100.0, 0.0),
    (50.5, 50.5, 0.0),

    # Zero values
    (0, 50, 50),        # Budgeted zero, actual positive
    (50, 0, -50),       # Budgeted positive, actual zero
    (0, 0, 0),          # Both zero
    (0.0, 0.0, 0.0),    # Both zero floats
    (0, -50, -50),      # Budgeted zero, actual negative

    # Negative values (for mathematical robustness, even if not typical financial inputs)
    (-100, -80, 20),    # Actual > Budgeted (less negative)
    (-100, -120, -20),  # Actual < Budgeted (more negative)
    (-50, 50, 100),     # Actual positive, Budgeted negative (50 - (-50) = 100)
    (50, -50, -100),    # Actual negative, Budgeted positive (-50 - 50 = -100)

    # Large numbers
    (1_000_000, 1_000_001, 1),
    (1_000_000, 999_999, -1),
    (1_234_567_890.123, 1_234_567_890.124, 0.001), # Large floats with precision
    (1_234_567_890.123, 1_234_567_890.122, -0.001),

    # Boolean values (treated as 0 or 1 in arithmetic operations)
    (True, 50, 49),     # True is 1, so 50 - 1 = 49
    (50, True, -49),    # True is 1, so 1 - 50 = -49
    (False, 50, 50),    # False is 0, so 50 - 0 = 50
    (50, False, -50),   # False is 0, so 0 - 50 = -50
    (True, False, -1),  # False is 0, True is 1, so 0 - 1 = -1

    # Invalid types - should raise TypeError
    ("100", 120, TypeError),       # Budgeted is string
    (100, "120", TypeError),       # Actual is string
    (None, 120, TypeError),        # Budgeted is None
    (100, None, TypeError),        # Actual is None
    ([100], 120, TypeError),       # Budgeted is list
    (100, [120], TypeError),       # Actual is list
    ({}, 120, TypeError),          # Budgeted is dict
    (100, {}, TypeError),          # Actual is dict
    (set(), 120, TypeError),        # Budgeted is set
    (100, set(), TypeError),       # Actual is set
    (complex(1, 2), 10, TypeError), # Budgeted is complex (not a real number type for typical financial ops)
    (10, complex(1, 2), TypeError)  # Actual is complex
])
def test_calculate_variance(budgeted, actual, expected):
    try:
        result = calculate_variance(budgeted, actual)
        assert result == expected
    except Exception as e:
        # Check if the raised exception is of the expected type
        assert isinstance(e, expected)
