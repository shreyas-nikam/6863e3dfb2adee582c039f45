
def calculate_variance(budgeted: float, actual: float) -> float:
    """
    Calculates the difference between the actual and budgeted amounts.

    Args:
        budgeted (float): The planned or expected expenditure for a category.
        actual (float): The actual expenditure incurred.

    Returns:
        float: The difference (actual - budgeted).

    Raises:
        TypeError: If either argument is not a float or int.
    """
    if not isinstance(budgeted, (int, float)):
        raise TypeError(f"Expected budgeted to be a float or int, got {type(budgeted)}")
    if not isinstance(actual, (int, float)):
        raise TypeError(f"Expected actual to be a float or int, got {type(actual)}")
    return float(actual - budgeted)


def calculate_variance(budgeted: float, actual: float) -> float:
    """
    Calculates the difference between the actual and budgeted amounts.

    Args:
        budgeted (float): The planned or expected expenditure for a category.
        actual (float): The actual expenditure incurred.

    Returns:
        float: The difference (actual - budgeted).

    Raises:
        TypeError: If either argument is not a float or int.
    """
    if not isinstance(budgeted, (int, float)):
        raise TypeError(f"Expected budgeted to be a float or int, got {type(budgeted)}")
    if not isinstance(actual, (int, float)):
        raise TypeError(f"Expected actual to be a float or int, got {type(actual)}")
    return float(actual - budgeted)
