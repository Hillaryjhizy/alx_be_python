# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform a division operation with error handling.
    
    Args:
    numerator (str): The numerator of the division operation.
    denominator (str): The denominator of the division operation.

    Returns:
    str: The result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        try:
            result = num / denom
            return f"The result of the division is {result:.1f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
