[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
<pre>
<b>Problem</b>
Using the variable totalwgt_lb, investigate whether first babies are lighter
or heavier than others. Compute Cohen’s d to quantify the difference between
the groups. How does it compare to the difference in pregnancy length?

<i>#Import Data</i>
import nsfg as ns 
preg = ns.ReadFemPreg() 

<i>#Cleaning Data</i>
birth_order_x_weight = preg[['birthord', 'totalwgt_lb']].dropna() 

<i>#Mean Weight of First Babies</i>
first_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb.mean() 
first_babies_mean 
result:7.201094430437772 

<i>#Mean Weight of Other Babies</i>
other_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb.mean()
other_babies_mean
result: 7.325855614973262

<i>#Mean of all Babies</i>
birth_order_x_weight.totalwgt_lb.mean()
result: 7.265628457623368

<b>Conclusion from Means:</b>
The first babies are lighter than the other babies by an average of around .1 pounds. 
That's 1.6% of the average weight of all babies.

<i>#Calculating Cohen's D</i>
first_babies = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb
other_babies = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb

import math
def CohenEffectSize(group1, group2):
     diff = group1.mean() - group2.mean()
     var1 = group1.var()
     var2 = group2.var()
     n1, n2 = len(group1), len(group2)
     pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
     d = diff / math.sqrt(pooled_var)
     return d

CohenEffectSize(other_babies, first_babies)
result: 0.08867236333202932

<i>#Cohen's D</i>
The difference between the baby weights is .08 standard deviations which is low. So there is not much difference.

<b>Results</b>
When using Cohen's D and baby weight means as measures of difference, they reveal 
that the difference between the baby weights is not significant.
</pre>
