from scipy import interpolate
import numpy as np


def find_intersection(x, y1, y2) -> tuple:
    """Finds the intersection point between two lines

    Args:
        x (List): np.linspace
        y1 (_type_): First Equation
        y2 (_type_): Second Equation

    Returns:
        tuple: The corresponding x and y values
    """

    # Interpolate curves to get continuous functions
    interp_line_1 = interpolate.interp1d(x, y1)
    interp_line_2 = interpolate.interp1d(x, y2)

    # Find the difference between the two functions
    diff = np.abs(y1 - y2)

    # Find when difference is minimized
    idx = np.argmin(diff)

    # Corresponding x and y values
    return x[idx], y1[idx]
