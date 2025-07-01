
def calculate_compound_interest(
    principal: float,
    rate: float,
    duration: int,
    compounding_frequency: str
) -> list:
    """
    Calculates the future value of an investment using compound interest formula over each year.

    Args:
        principal (float): The initial amount of money invested.
        rate (float): The annual interest rate as a decimal.
        duration (int): The total number of years for the investment.
        compounding_frequency (str): 'Monthly' or 'Annually'.

    Returns:
        list: A list of floating point numbers representing the future value at each year.

    Raises:
        ValueError: If compounding_frequency is invalid.
        TypeError: If principal, rate, or duration are not numbers or are invalid.
    """
    if principal is None or rate is None or duration is None:
        raise TypeError("Principal, rate, and duration must not be None")
    if not isinstance(principal, (int, float)):
        raise TypeError("Principal must be a number")
    if not isinstance(rate, (int, float)):
        raise TypeError("Rate must be a number")
    if not isinstance(duration, int):
        raise TypeError("Duration must be an integer")
    if duration < 0:
        return []

    if compounding_frequency == 'Monthly':
        n = 12
    elif compounding_frequency == 'Annually':
        n = 1
    else:
        raise ValueError("Invalid compounding frequency. Expected 'Monthly' or 'Annually'.")

    result = []
    for year in range(1, duration + 1):
        total_periods = n * year
        future_value = principal * (1 + rate / n) ** total_periods
        result.append(future_value)
    return result


def calculate_compound_interest(
    principal: float,
    rate: float,
    duration: int,
    compounding_frequency: str
) -> list:
    """
    Calculates the future value of an investment using compound interest formula over each year.

    Args:
        principal (float): The initial amount of money invested.
        rate (float): The annual interest rate as a decimal.
        duration (int): The total number of years for the investment.
        compounding_frequency (str): 'Monthly' or 'Annually'.

    Returns:
        list: A list of floating point numbers representing the future value at each year.

    Raises:
        ValueError: If compounding_frequency is invalid.
        TypeError: If principal, rate, or duration are not numbers or are invalid.
    """
    if principal is None or rate is None or duration is None:
        raise TypeError("Principal, rate, and duration must not be None")
    if not isinstance(principal, (int, float)):
        raise TypeError("Principal must be a number")
    if not isinstance(rate, (int, float)):
        raise TypeError("Rate must be a number")
    if not isinstance(duration, int):
        raise TypeError("Duration must be an integer")
    if duration < 0:
        return []

    if compounding_frequency == 'Monthly':
        n = 12
    elif compounding_frequency == 'Annually':
        n = 1
    else:
        raise ValueError("Invalid compounding frequency. Expected 'Monthly' or 'Annually'.")

    result = []
    for year in range(1, duration + 1):
        total_periods = n * year
        future_value = principal * (1 + rate / n) ** total_periods
        result.append(future_value)
    return result
