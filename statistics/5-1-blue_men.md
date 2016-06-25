[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

<pre>
<b>Problem </b>
In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with 
parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com).
What percentage of the U.S. male population is in this range?
Hint: use scipy.stats.norm.cdf.

<b>Code</b>
<i>#import data </i>
import brfss
df_brfss = brfss.ReadBrfss()

mu = 178
sigma = 7.7 

<i>#Calculate the cumulative distribution functions for each point</i>
below_high_point = scipy.stats.norm.cdf(185.42, loc = 178, scale = 7.7)
below_low_point = scipy.stats.norm.cdf(177.8, loc = 178, scale = 7.7)

<i>#Calculate the difference</i>
below_high_point-below_low_point
0.34274683763147368

<b>Solution</b>
34.27% of the U.S male populations are eligible to join the Blue Man Group

</pre>
