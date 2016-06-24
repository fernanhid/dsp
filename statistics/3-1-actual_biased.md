[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

import chap01soln<br>
resp = chap01soln.ReadFemResp()<br>
<br>
distribution = defaultdict(int)<br>
   		for value in resp.numkdhh:<br>
    distribution[value]+=1<br>
<br>
distribution<br>
{0: 3563, 1: 1636, 2: 1500, 3: 666, 4: 196, 5: 82}
