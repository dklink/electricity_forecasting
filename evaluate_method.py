"""frameworks to evaluate models to streamline iteration/development"""
import pandas as pd
import numpy as np
from typing import Callable

def evaluate(method: Callable):
    """evaluates a method, which must take two arguments:
        'train' (the train dataset, pd series of Solar PV supply, datetime index)
        'pred_dt', datetimes at which to predict solar pv supply
       the method must return a float value corresponding to each 'pred_dt', representing the predicted solar pv supply
       
       returns: mean absolute error between predictions and test set; 'residuals', which is a pd Series of test - pred, datetime index
    """

    train = pd.read_csv("data/train.csv", parse_dates=["DATETIME"]).set_index("DATETIME")["SOLAR PV"]
    test = pd.read_csv("data/test.csv", parse_dates=["DATETIME"]).set_index("DATETIME")["SOLAR PV"]

    pred = method(train=train, pred_dt=test.index)
    pred = pd.Series(pred, index=test.index)

    assert all(test.index == pred.index)
    mae = MAE(test=test, pred=pred)
    residuals = test - pred

    return mae, residuals


def MAE(test: pd.Series, pred: pd.Series):
    """simple error metric for timeseries: mean absolute error"""
    return np.mean(np.abs(test-pred))
