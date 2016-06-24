[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>import nsfg as ns <br>
>preg = ns.ReadFemPreg() <br>
>birth_order_x_weight = preg[['birthord', 'totalwgt_lb']].dropna() <br>
>first_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb.mean() <br>
>first_babies_mean <br>
>result:7.201094430437772 <br>
>other_babies_mean = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb.mean()<br>
>other_babies_mean<br>
>result: 7.325855614973262<br>
>birth_order_x_weight.totalwgt_lb.mean()<br>
>result: 7.265628457623368<br>
<br>
>The first babies are lighter than the other babies by an average of around .1 pounds. That's 1.6% of the average weight of all babies.<br>
<br>
>first_babies = birth_order_x_weight[birth_order_x_weight.birthord == 1].totalwgt_lb<br>
>other_babies = birth_order_x_weight[birth_order_x_weight.birthord != 1].totalwgt_lb<br>
>Cohen's D<br>
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
>CohenEffectSize(first_babies, other_babies)<br>
>result: --0.08867236333202932<br>

