def percent_diff(a: float, b: float) -> float:
    """Calculates the difference the values are as a percentage of their average value

    Args:
        a (float): First value
        b (float): Second Value

    Returns:
        float: _description_
    """

    diff = (abs(a - b) / ((a + b) / 2)) * 100
    return diff


def percent_error(a: float, b: float) -> float:
    """Calculates the percent difference between two numbers

    Args:
        a (Theoretical Value): Value determined from theory
        b (Experimental Value): Value determined from experiment

    Returns:
        float: error in percentage between two values
    """

    diff = (abs(a - b) / a) * 100
    return diff
