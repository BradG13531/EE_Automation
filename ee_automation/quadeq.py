from cmath import sqrt


def quadeq(a: float, b: float, c: float) -> tuple:
    """Numerically solves a quadratic equation

    Args:
        a (float): Quadratic Coefficient
        b (float): Linear Coefficient
        c (float): Constant Term

    Returns:
        tuple: The solutions in the form (x1, x2)
    """

    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x1, x2)
