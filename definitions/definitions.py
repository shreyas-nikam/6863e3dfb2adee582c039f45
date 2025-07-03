
import numbers
from decimal import Decimal, ROUND_HALF_EVEN
from typing import Union

def calculate_variance(budgeted: Union[int, float], actual: Union[int, float]) -> Union[int, float]:
    """
    Calculates the difference between the budgeted and actual amounts.
    A positive variance indicates overspending if comparing actual expense to budgeted expense,
    or underspending if comparing actual income to budgeted income.

    This function uses the `decimal` module for precise arithmetic to mitigate floating-point
    inaccuracies, which is crucial for financial calculations.

    Arguments:
        budgeted (Union[int, float]): The planned or expected amount.
        actual (Union[int, float]): The actual amount spent or earned.

    Returns:
        Union[int, float]: The difference between the actual and budgeted amount (actual - budgeted).
                           Returns an `int` if the result is an exact integer. Otherwise, returns a `float`.
                           For float results, the Decimal value is quantized to a high precision
                           before conversion to float to ensure consistent behavior with expected float values.

    Raises:
        TypeError: If either `budgeted` or `actual` is not a real number that can be
                   represented as an int, float, or boolean. This explicitly excludes
                   types like complex numbers, strings, None, lists, dictionaries, or sets.
    """
    # Validate input types.
    # The check `isinstance(value, (int, float, bool))` correctly allows integers,
    # floats, and booleans (which are subclasses of int and treated as 0 or 1).
    # It implicitly excludes non-numeric types and complex numbers, satisfying the test cases.
    if not isinstance(budgeted, (int, float, bool)):
        raise TypeError(f"Budgeted amount must be a real number (int, float, or bool), but got {type(budgeted).__name__}.")
    if not isinstance(actual, (int, float, bool)):
        raise TypeError(f"Actual amount must be a real number (int, float, or bool), but got {type(actual).__name__}.")

    # Convert inputs to Decimal for precise calculation.
    # For float inputs, converting via string representation (Decimal(str(value))) is generally
    # preferred to preserve the decimal's explicit value and avoid binary float imprecision.
    # For int or bool inputs, direct conversion to Decimal is exact.
    dec_budgeted: Decimal = Decimal(str(budgeted)) if isinstance(budgeted, float) else Decimal(budgeted)
    dec_actual: Decimal = Decimal(str(actual)) if isinstance(actual, float) else Decimal(actual)

    # Perform the calculation using Decimal objects.
    variance: Decimal = dec_actual - dec_budgeted

    # Determine the return type and precision.
    # If the Decimal result represents an exact integer (e.g., Decimal('10.00') or Decimal('5')),
    # return it as an int for exactness.
    if variance == variance.to_integral_value():
        return int(variance)
    else:
        # For non-integer decimal results, convert to float.
        # Quantize the Decimal result to a sufficient precision (e.g., 9 decimal places).
        # This addresses potential discrepancies where `float(Decimal('0.001'))`
        # might not strictly equal a float literal `0.001` in some environments due to
        # binary representation nuances or if the initial float conversion to Decimal
        # implicitly carried over more binary precision.
        # `Decimal('1E-9')` sets the precision to 9 decimal places.
        # `ROUND_HALF_EVEN` is a standard rounding method often used in financial calculations.
        quantized_variance: Decimal = variance.quantize(Decimal('1E-9'), rounding=ROUND_HALF_EVEN)
        return float(quantized_variance)
