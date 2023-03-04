# Locally weighted Regression (loess)

Locally weighted regression, or loess, is a way of estimating a regression surface through a multivariate smoothing procedure, fitting a function of the independent variables locally and in a moving fashion analogous to how a moving average is computed for a time series.

## Paper Recreation:

In the notebook <a href="https://github.com/santifiorino/loess/blob/master/section_5.ipynb">section_5.ipynb</a> I recreated every single plot from Section 5 of Cleveland's Paper [1]. Using the same dataset, I got the same results as the ones they displayed, so the algorithm recreation was working.

## Personal Experimentation:

In script <a href="https://github.com/santifiorino/loess/blob/master/synth_data_creation.py">synth_data_creation.py</a> I created the following 4 surfaces in $R^3$:

<img src="https://i.imgur.com/EFFffFP.png" width="800"/>

Then I added some noise:

<img src="https://i.imgur.com/lSCxor8.png" width="800"/>

And estimated them with Loess using different parameters, for example this is the result with $f=0.5$ and $d=2$:

<img src="https://i.imgur.com/wwDZCq4.png" width="800"/>

In the notebook <a href="https://github.com/santifiorino/loess/blob/master/experimentation.ipynb">experimentation.ipynb</a>, using the data created by the previous script, I created the plots above, and for a better look at the results, I plotted the level curves of the estimations, and how they compare with the real data, and fitted data:

Plane:

<img src="https://i.imgur.com/e87EBCF.png" width="800"/>

Saddle:

<img src="https://i.imgur.com/WFRfRdm.png" width="800"/>

Cubic:

<img src="https://i.imgur.com/ke8rhox.png" width="800">

Absolute:

<img src="https://i.imgur.com/Jlp252m.png" width="800">

## References:

<a id="1" href="https://www.jstor.org/stable/2289282">[1]</a>
William S. Cleveland and Susan J. Devlin (1968).
Locally Weighted Regression: An Approach to Regression Analysis by Local Fitting.
Journal of the American Statistical Association, Vol. 83, No. 403 (Sep., 1988), pp. 596-610
