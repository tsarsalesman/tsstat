"""
Functions Component
-------------------


"""
from utils import qsort

def mode (data):
    """
    Calculates the mode of a dataset.

    Params
    ------
    data : list or tuple or set
        The dataset.

    Returns
    -------
    float
        The mode value.
    """
    max, mode = 0
    for val in data:
        cnt = data.count(val)
        if (cnt > max):
            max = cnt
            mode = val
    return mode


def mean (data): 
    """
    Calculates the mean of a dataset.

    Params
    ------
    data : list or tuple or set
        The dataset.

    Returns
    -------
    float
        The mean value.
    """
    return sum(data) / len(data)

def median (data):
    """
    Calculates the median of a dataset.

    Params
    ------
    data : list or tuple or set
        The dataset.

    Returns
    -------
    float
        The median value.
    """
    n=len(data)
    qsort(data)
    if n%2==0: return((data[n//2])+(data[n//2-1]))/2
    return data[n//2]

def sumsqr (values):
    """
    Calculates sum of squares of a dataset. Forgoes the definitional formula
    because it's not great for large datasets or an odd mean.
    
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

def var (data, sample=False):
    """
    Calculates the variance of a dataset.

    Params
    ------
    data : list or tuple or set
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
    if sample==True: return _sumsqr/(len(data)-1)
    return _sumsqr/len(data)

def stdev (data, sample=False):
    """
    Calculates the standard deviation of a dataset.

    Params
    ------
    data : list or tuple or set
        The dataset.
    sample : bool
        When True will calculate the sample variance,
        When False (default) will calculate variance for population size.

    Returns
    -------
    float
        The standard deviation of the dataset.
    float : optional
        The variance of the dataset.
    """
    _sumsqr = sumsqr(values)
    if sample==True: var = _sumsqr/(len(data)-1)
    else: var = _sumsqr/len(data)
    return (var)**0.5, var

def sterror(data, sample=False):
    return stdev(data, sample) / (len(data)**0.5

def coeffvar(data, sample=False):
    return (stdev(data, sample) / mean(data))*100
