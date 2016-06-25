[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

<pre>
<b>Code </br>
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


##<b>Intuitions </b>
</pre>
