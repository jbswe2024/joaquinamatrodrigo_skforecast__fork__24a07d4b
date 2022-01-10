# Unit test __init__
# ==============================================================================
import pytest
import numpy as np
import pandas as pd
from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
from sklearn.linear_model import LinearRegression

def test_init_lags_when_integer():
    '''
    Test creation of attribute lags when integer is passed.
    '''
    forecaster = ForecasterAutoregMultiOutput(LinearRegression(), lags=10, steps=2)
    assert (forecaster.lags == np.arange(10) + 1).all()
    
def test_init_lags_when_list():
    '''
    Test creation of attribute lags when list is passed.
    '''
    forecaster = ForecasterAutoregMultiOutput(LinearRegression(), lags=[1, 2, 3], steps=2)
    assert (forecaster.lags == np.array([1, 2, 3])).all()
    
def test_init_lags_when_range():
    '''
    Test creation of attribute lags when range is passed.
    '''
    forecaster = ForecasterAutoregMultiOutput(LinearRegression(), lags=range(1, 4), steps=2)
    assert (forecaster.lags == np.array(range(1, 4))).all()
    
def test_init_lags_when_numpy_arange():
    '''
    Test creation of attribute lags when numpy arange is passed.
    '''
    forecaster = ForecasterAutoregMultiOutput(LinearRegression(), lags=np.arange(1, 10), steps=2)
    assert (forecaster.lags == np.arange(1, 10)).all()

def test_init_exception_when_lags_is_int_lower_than_1():
    '''
    Test exception is raised when lags is initialized with int lower than 1.
    '''
    with pytest.raises(Exception):
        ForecasterAutoregMultiOutput(LinearRegression(), lags=-10, steps=2)
        
def test_init_exception_when_lags_has_values_lower_than_1():
    '''
    Test exception is raised when lags is initialized with any value lower than 1.
    '''
    for lags in [[0, 1], range(0, 2), np.arange(0, 2)]:
        with pytest.raises(Exception):
            ForecasterAutoregMultiOutput(LinearRegression(), lags=lags, steps=2)