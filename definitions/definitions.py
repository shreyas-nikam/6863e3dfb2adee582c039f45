
def calculate_monthly_payment(loan_amount: float, annual_interest_rate: float, loan_term: int) -> float:
    """Calculates the monthly mortgage payment.

    Args:
        loan_amount: The principal amount of the loan.
        annual_interest_rate: The annual interest rate (as a decimal).
        loan_term: The loan term in years.

    Returns:
        The calculated monthly mortgage payment.

    Raises:
        ValueError: If loan_amount, annual_interest_rate, or loan_term are negative.
        TypeError: If loan_amount, annual_interest_rate, or loan_term are of incorrect type.
        ZeroDivisionError: If loan_term is zero.
    """

    if not isinstance(loan_amount, (int, float)):
        raise TypeError("Loan amount must be a number")
    if not isinstance(annual_interest_rate, (int, float)):
        raise TypeError("Annual interest rate must be a number")
    if not isinstance(loan_term, int):
        raise TypeError("Loan term must be an integer")


    if loan_amount < 0:
        raise ValueError("Loan amount cannot be negative")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative")
    if loan_term < 0:
        raise ValueError("Loan term cannot be negative")

    if loan_amount == 0:
        return 0.0

    if annual_interest_rate == 0:
        return loan_amount / (loan_term * 12)

    if loan_term == 0:
        raise ZeroDivisionError("Loan term cannot be zero")

    monthly_interest_rate = annual_interest_rate / 12
    num_payments = loan_term * 12

    try:
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-num_payments))
    except ZeroDivisionError:
        return loan_amount / (loan_term * 12)

    return monthly_payment
