[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

<pre>
<b>Code </b>
import random

random_list = []
for i in range(1000):
    random_list.append(random.random())

random_pmf = thinkstats2.Pmf(random_list)
random_cdf = thinkstats2.Cdf(random_list)

thinkplot.PrePlot(2)
thinkplot.Pmfs([random_cdf, random_pmf])
thinkplot.Show()

<b>Graph</b>


<b>Intuition </b>
The distribution is uniform since in the visualization of the probability 
mass function the likelihood of each point is equal at .1%. This also means
that the slope of the cumulative distribution function close to zero, which 
it is. These two point to the conclusion that the points are indeed random.  
</pre>
