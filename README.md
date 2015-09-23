#Trading Bot

I created this repository to test an idea, probably this will be my final project for the algotrading class.

The main idea I want to test is to use Bayesian networks to evaluate if it's worth to buy stocks of a company given a set of prices on a time interval.
Consider n economic Indicators, from I1 to In and Rho being the profit in terms of percentage, the probability of having a profit Rho is given by<br/><img src="http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20p%28Rho%7CI_i%29%7D%7Bn%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\frac{\sum_{i=1}^{n} p(Rho|I_i)}{n}" width="118" height="47" />

<!--\frac{\sum_{i=1}^{n} p(Rho|I_i)}{n}-->
