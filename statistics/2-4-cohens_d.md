[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>import nsfg as ns
>preg = ns.ReadFemPreg()
>birth_order_x_weight = preg[['birthord', 'totalwgt_lb']].dropna()
>first_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb.mean()
>first_babies_mean
>result:7.201094430437772
>other_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb.mean()
>other_babies_mean
>result: 7.325855614973262
>birth_order_x_weight.totalwgt_lb.mean()
>result: 7.265628457623368
<br>
>The first babies are lighter than the other babies by an average of around .1 pounds. That's 1.6% of the average weight of all babies.
<br>
>first_babies = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb
>other_babies = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb
>Cohen's D
>import math
>def CohenEffectSize(group1, group2):
>    diff = group1.mean() - group2.mean()
<br>
>    var1 = group1.var()
>    var2 = group2.var()
>    n1, n2 = len(group1), len(group2)
<br>
>    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
>    d = diff / math.sqrt(pooled_var)
>    return d
<br>
>CohenEffectSize(first_babies, other_babies)
>result: --0.08867236333202932

