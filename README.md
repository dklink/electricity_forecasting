# Electricity Supply Forecasting

This project compares different methods for predicting hourly electricity supply from renewables in CA.

## Data
Hourly renewables generation is pulled from publicly available CAISO data from 2018 to 2021.  The final month of data is used as the test dataset, to mimic future forecasting.

## Approaches

### Baseline
A few extremely simplistic methods are implemented in order to get a baseline of performance that more sophisticated methods should be expected to surpass.  Implementation, figures, and discussion can be found in `baseline.ipynb`.

Baseline 1: calculate hourly averages across the training set; make a prediction by just looking the relevant hourly average.

Baseline 2: same as baseline 1, but only consider the final month of the training set.  This improves on seasonality error a lot.

Baseline 3: same, but only considre the final week of the training set.  Error increases - here we see the tradeoff of recency vs noise, with the final week being very recent, but more noisy.

### Long-term Pattern Approach
Next TODO:
When looking at the training set, there are two obvious long-term patterns: seasonality (more sun in summer, less in winter), and some sort of year-over-year increase (as CA installs more solar).  We can model these, perhaps a different model for each hour of day, by combining a periodic and linear function, then fitting to the training data.  This should produce a more accurate prediction, and will be an actual "forecast", extrapolating from the training data, rather than dumbly just hoping future behavior will be very similar to recent behavior.
