import pytest
from definition_4524c51d46a549beb4e10724535ccb78 import calculate_monthly_payment

@pytest.mark.parametrize("loan_amount, annual_interest_rate, loan_term, expected", [
    (200000, 0.05, 30, 1073.64),
    (100000, 0.04, 15, 739.69),
    (50000, 0.06, 10, 555.10),
    (300000, 0.035, 20, 1739.74),
    (10000, 0.07, 5, 198.01),
    (0, 0.05, 30, 0.00),
    (200000, 0, 30, 555.56),  # No interest
    (200000, 0.05, 0, ZeroDivisionError),  # Zero loan term
    (-200000, 0.05, 30, ValueError),  # Negative loan amount
    (200000, -0.05, 30, ValueError),  # Negative interest rate
    (200000, 0.05, -30, ValueError),  # Negative loan term
    (200000.50, 0.05, 30, 1073.67), # Float loan amount
    (200000, 0.055, 30, 1135.91), # Float interest rate
    (200000, 0.05, 30.5, ZeroDivisionError), # Float loan term
    ("200000", 0.05, 30, TypeError),  # String loan amount
    (200000, "0.05", 30, TypeError),  # String interest rate
    (200000, 0.05, "30", TypeError),  # String loan term
    (None, 0.05, 30, TypeError),  # None loan amount
    (200000, None, 30, TypeError),  # None interest rate
    (200000, 0.05, None, TypeError),  # None loan term
    (1000, 0.10, 1, 87.92)
])
def test_calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term, expected):
    try:
        monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term)
        assert round(monthly_payment, 2) == expected
    except Exception as e:
        assert type(e) == expected
