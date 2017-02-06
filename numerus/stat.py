"""Tools for statistical analysis and measures of probability."""

from .checks import is_numeric

def mean(*values):
    """Returns the arithmetic mean of a set of values.

    :param *values: The numbers you wish to find the mean of."""

    if not values:
        raise TypeError("Cannot take mean of no values")
    for value in values:
        if not is_numeric(value):
            raise TypeError("'%s' is not numeric" % str(value))
    return sum(values) / len(values)


def median(*values):
    """Returns the median of a set of values.

    :param *values: The numbers you wish to find the median of."""

    if not values:
        raise TypeError("Cannot take mean of no values")
    for value in values:
        if not is_numeric(value):
            raise TypeError("'%s' is not numeric" % str(value))
    values = sorted(values)
    length = len(values)
    if length % 2:
        return values[int((length / 2) - 0.5)]
    else:
        midway = int(length / 2)
        return (values[midway - 1] + values[midway]) / 2