import pytest
from definition_e9c1d88a2d9742e28f744b4b9449ddef import calculate_compound_interest

@pytest.mark.parametrize("principal, rate, duration, compounding_frequency, expected", [
    (1000, 0.05, 10, 'Monthly', [1000 * (1 + 0.05/12)**(12 * t) for t in range(1, 11)]),
    (1000, 0.05, 10, 'Annually', [1000 * (1 + 0.05)**t for t in range(1, 11)]),
    (0, 0.05, 10, 'Monthly', [0.0 for _ in range(1, 11)]),
    (1000, 0.0, 10, 'Monthly', [1000.0 for _ in range(1, 11)]),
    (1000, 0.05, 0, 'Monthly', []),
    (1000, 0.05, 10, 'Invalid', ValueError),
    (None, 0.05, 10, 'Monthly', TypeError),
    ('abc', 0.05, 10, 'Monthly', TypeError),
])

def test_calculate_compound_interest(principal, rate, duration, compounding_frequency, expected):
    if isinstance(expected, list):
        result = calculate_compound_interest(principal, rate, duration, compounding_frequency)
        assert all(abs(a - b) < 1e-6 for a, b in zip(result, expected))
    else:
        with pytest.raises(expected):
            calculate_compound_interest(principal, rate, duration, compounding_frequency)
