"""
Functions Component
-------------------

@author tsarsalesman
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

def cohen(data1, data2, ddof1, ddof2):
    """
    Compute the Cohen's D effect size.

    Params
    ------
    data1 : list or tuple or set
        Dataset 1.
    data2 : list or tuple or set
        Dataset 2.
    ddof1 : int, optional
        Delta degrees of freedom for 1st dataset. Defaults to 1.
    ddof2 : int, optional
        Delta degrees of freedom for 2nd dataset. Defaults to 1.
    """
    n = [len(data1), len(data2)]
    return (mean(data1) - mean(data2))/((((n[0]-1)*(std(data1, ddof=ddof1))**2)+
            ((n[1]-1)*(std(data2, ddof=ddof2))**2))/(n[0]+n[1]-2))**0.5)

def diff(A, B):
    """Finds the difference between two given lists of ints.

    Params
    ------
    A : array_like
        An array of integers
    B : array_like
        An array of integers

    Returns
    -------
    Difference : array_like
        The difference between each associated value.
    """
    diffs = []
    for i in range(len(A)):
        diffs.append(A[i] - B[i])
    return diffs

def cv(df, alternative = 'two-sided', q = 0.05):
    """Finds the t critical value

    Parameters
    ----------
    df : int
        Degrees of freedom
    alternative : str, optional
        The type of t test based on alternative hypothesis, by default 'two-sided'
    q : float, optional
        The significant level, by default 0.05

    Returns
    -------
    Critical value : float
        The position of value on the curve
    """
    if (alternative == "greater"):
        return t.ppf(1 - q, df)
    if (alternative == "lesser"):
        return t.ppf(q, df)
    if (alternative == 'two-sided'):
        return t.ppf(1 - q/2, df)
    else:
        return None
