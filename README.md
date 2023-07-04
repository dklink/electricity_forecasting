# Electricity Supply Forecasting

This project compares different methods for predicting hourly electricity supply from renewables in CA.

## Data
Hourly renewables generation is pulled from publicly available CAISO data from 2018 to 2021.  The final month of data is used as the test dataset, to mimic future forecasting.

## Approaches

### Baseline
A few extremely simplistic methods are implemented in order to get a baseline of performance that more sophisticated methods should be expected to surpass.

Baseline 1: simply predict the average curve over the last month of the training set.

Baseline 2: for a given test day, predict the average over the 4 most recent days with the same day-of-week (e.g. for some unknown future monday, predict the average curve over the 4 latest mondays)
