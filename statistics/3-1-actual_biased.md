[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

<pre>
from collections import defaultdict

import chap01soln
resp = chap01soln.ReadFemResp()

unbiased_dist = defaultdict(int)
for value in resp.numkdhh:
    unbiased_dist[value]+=1
    
unbiased_dist = dict(unbiased_dist)

def to_bias(unbiased_dist):
    bias = unbiased_dist.copy()
    
    for number, frequency in bias.items():
        bias[number] = bias[number] * number
    return bias
    
bias_dist = to_bias(unbiased_dist)

<b>Distribution Results</b>
unbiased_pmf
{0: 3563, 1: 1636, 2: 1500, 3: 666, 4: 196, 5: 82}

bias_dist:
{0: 0, 1: 1636, 2: 3000, 3: 1998, 4: 784, 5: 410}

<b>Mean</b>
<i>mean of biased_distributions</i>
sum(to_bias(bias_dist).values())/float(sum(bias_dist.values()))
2.4036791006642821

<i>mean of unbiased distributions</i>
sum(to_bias(unbiased_dist).values())/float(sum(unbiased_dist.values()))
1.0242051550438309


<b> Graph </b>


</pre>
