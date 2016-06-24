[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>import nsfg as ns <br>
>preg = ns.ReadFemPreg() <br>
>birth_order_x_weight = preg[['birthord', 'totalwgt_lb']].dropna() <br>
>first_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb.mean() <br>
>first_babies_mean <br>
>result:7.201094430437772 <br>
>other_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb.mean()\n
>other_babies_mean<br>
>result: 7.325855614973262<br>
>birth_order_x_weight.totalwgt_lb.mean()<br>
>result: 7.265628457623368<br>
>>The first babies are lighter than the other babies by an average of around .1 pounds. That's 1.6% of the average weight of all babies.<br>
<br>
>first_babies = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb<br>
>other_babies = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb<br>
<br>
<br>
>Cohen's D:<br>
<br>
>import math<br>
>def CohenEffectSize(group1, group2):<br>
>    diff = group1.mean() - group2.mean()<br>
<br>
>    var1 = group1.var()<br>
>    var2 = group2.var()<br>
>    n1, n2 = len(group1), len(group2)<br>
<br>
>    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)<br>
>    d = diff / math.sqrt(pooled_var)<br>
>    return d<br>
<br>
>CohenEffectSize(other_babies, first_babies)<br>
>result: 0.08867236333202932<br>
>>The difference between the baby weights is .08 standard deviations which is low. So there is not much difference.

>Overall Results:<br>
> By looking at both Cohen's D and means of baby weights, the difference between the weights of the first babies and the other babies is not significant. 
