[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
<pre>
import nsfg as ns 
preg = ns.ReadFemPreg() 

birth_order_x_weight = preg[['birthord', 'totalwgt_lb']].dropna() 

first_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb.mean() 
first_babies_mean 
result:7.201094430437772 

other_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb.mean()
other_babies_mean
result: 7.325855614973262

birth_order_x_weight.totalwgt_lb.mean()
result: 7.265628457623368

####The first babies are lighter than the other babies by an average of around .1 pounds. That's 1.6% of the average weight of all babies.

first_babies = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb
other_babies = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb


Cohen's D:

import math

 style="text-indent: 5em;"
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
####The difference between the baby weights is .08 standard deviations which is low. So there is not much difference.

reOverall Results:
When using Cohen's D and baby weight means as measures of difference, they reveal 
that the difference between the baby weights is not significant.
</pre>
