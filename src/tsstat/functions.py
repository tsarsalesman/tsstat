"""
    Functions Component
    -------------------


"""
from utils import qSort

def mode (values):
    freq= {}

    for i in values


def mean (values): 
    """
    Calculates the mean of a dataset.

    Params
    ------
    values : list or tuple
        The dataset.

    Returns
    -------
    float
        The mean value.
    """
    return sum(values) / len(values)

def median (values):
    N = len(values)

def sumsqr (values):
    """
    Calculates sum of squares of a dataset.
    
    Params
    ------
    values : list or tuple
        The dataset

    Returns
    -------
    float
        The sum of squares of the dataset.
    """
    sqrs = []
    for val in values:
        sqrs.append(val**2)
    return sum(sqrs) - ((sum(values))**2)/len(values)

def var (values, sample=False):
    """
    Calculates the variance of a dataset.

    Params
    ------
    values : list or tuple
        The dataset.
    sample : bool
        When True will calculate the sample variance,
        When False (default) will calculate variance for population size.


    Returns
    -------
    float
        The variance of the dataset.
    """
    _sumsqr = sumsqr(values)
    if size == "sample"
