# Locally weighted Regression (loess)

Locally weighted regression, or loess, is a way of estimating a regression surface through a multivariate smoothing procedure, fitting a function of the independent variables locally and in a moving fashion analogous to how a moving average is computed for a time series.

## Paper Recreation:

In the notebook <a href="https://github.com/santifiorino/loess/blob/master/section_5.ipynb">section_5.ipynb</a> I've recreated every single plot from Section 5 of Cleveland's Paper [1]. Using the same dataset, I got the same results as the ones they displayed, so the algorithm recreation was working.

## Personal Experimentation:

In the notebook

<img src="https://i.imgur.com/EFFffFP.png"  width="800"/>

### Surfaces with added noise:

<img src="https://i.imgur.com/lSCxor8.png"  width="800"/>

### Loess estimation with f=.5, degree=2

<img src="https://i.imgur.com/wwDZCq4.png"  width="800"/>

## References:

<a id="1" href="https://www.jstor.org/stable/2289282">[1]</a>
William S. Cleveland and Susan J. Devlin (1968).
Locally Weighted Regression: An Approach to Regression Analysis by Local Fitting.
Journal of the American Statistical Association, Vol. 83, No. 403 (Sep., 1988), pp. 596-610
