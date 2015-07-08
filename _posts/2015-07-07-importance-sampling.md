---
layout: post
title: A Review of Importance Sampling
tags:
- monte carlo
- probability
---

Importance sampling is a monte carlo method for estimating properties of a random variable. For example, in Bayesian inference, expectation an is important property to compute, but often, the expectation of a random variable doesn't have an analytical solution. Decades ago, these difficulties make Bayesian inference not practical in many cases. But with advance of computers and tools like importance sampling, Bayesian inference has become much more useful. <!--break-->

Let's take a look at computing expectation of a random in greater details. The expectation of a random variable is simply sum of all possible values weighted by their probability, $\Bbb {E}_p(g(\mathbf X)) = \sum_X g(\mathbf x)p(\mathbf x)$, or in continuous space $\Bbb {E}_p(g(\mathbf X)) = \int_X g(\mathbf x)p(\mathbf x)d\mathbf x$. From the equation, we can see that in discrete space, the expectation can be easily computed. In continuous space however, things can be difficult. When it's integral over a high dimension or the integrand is too complicated, the analytical solution might not exist. So alternative method is required. If sample from distribution $p(\mathbf x)$ can be drawn easily, then a straight-forward monte carlo simulation can be used, that is repeatedly draw samples from $p(\mathbf x)$ and average the samples. According to the law of large number, the result will converge to the expectation. But when drawing from $p(\mathbf x)$ is difficult or impossible, the importance sampling can be used.

The formula of expectation can be written as

$$
\int_X g(\mathbf x) \frac{p(\mathbf x)}{q(\mathbf x)} q(\mathbf x)d\mathbf x
$$

where $q(\mathbf x)$ is a distribution that can be easily drawn from. Let's denote $g(\mathbf x) \frac{p(\mathbf x)}{q(\mathbf x)}$ as $g(\mathbf x) w(\mathbf x)$, where importance weight $w(\mathbf x)$ is $\frac{p(\mathbf x)}{q(\mathbf x)}$. Now the interpretation of the formula can be changed to the expectation of $g(\mathbf x) w(\mathbf x)$ with respect to $q(\mathbf x)$, $\Bbb E_p(g(\mathbf X)) = \Bbb E_q(g(\mathbf X) w(\mathbf X))$.

Since $q(\mathbf x)$ is a distribution that can be easily drawn from, the simple mento carlo method in the second paragraph can be used to compute the expectation. One might ask how good is the estimation. With the law of large number and $q(\mathbf x)$ covers $g(\mathbf x)p(\mathbf x)$, one can shown that the estimated expectation will converge to the true expectation[1][2]. For the method to work well, meaning converging fast, some other conditions need to be satisfied[2].

Let's see an example how to apply importance sampling:

$$
\mathbf X \sim U(0,1) \\
g(x) = 8x
$$

$\mathbf X$ is an uniform distribution from 0 to 1, and $g(x)$ is a function. And we want to compute $\Bbb E(g(\mathbf X))$. In this example, $\Bbb E(g(\mathbf X))$ has an analytical solution, which will gives the answer 4. But, let's pretend that we can't solve it analytically, so we can use importance sampling to solve it instead. Let $q(\mathbf x)$ be the pdf of Normal distribution with parameters (0,10), which will be our importance proposal distribution. Then we will have the estimated expectation $\hat\mu_{g(\mathbf X)}$:

$$
\begin{equation}
\hat\mu_{g(\mathbf X)} = \frac{1}{N} \sum_{i=1}^N g(\mathbf x^{(i)}) w(\mathbf x^{(i)})
\end{equation}
$$

where $w(\mathbf x)$ is the importance weighting, $\mathbf x^{(i)}$ is a sample drawn from $q(\mathbf x)$ and N is the number of samples.

Here is a sample code written in Julia for computing $\hat\mu_{g(\mathbf X)}$:

{% highlight julia %}
using Distributions

q = Normal(0,10)      
u = Uniform(0,1)
g(x) = 8x                     
w(x) = pdf(u,x)/pdf(q,x)   #importance weight

N = 10000                  #number of samples
for i = 1:10
    println(string("(", i, ")", "u hat with ", N , " samples:",
                  foldr((x,r) -> r += g(x)*w(x), 0, rand(q, N))/N))
end
{% endhighlight %}

When the result is very close to 4, which is the true expectation, with an error about only $0.1\%$. If $N$ is increased, we will see that the estimation gets even better.

Note that, $g(x)$ can be any functions, which can be very useful. For example, if we choose $g(x)$ to be a indicator with some region to be $A$ to be 1 and 0 otherwise, $\Bbb 1_A$. Then, we can estimate the probability of a specific region in $A$, because $\int_{X} \Bbb 1_A(\mathbf x) p(\mathbf x) d\mathbf x = \Bbb P(\mathbf x \in A)$


Reference:<br>
<a href="http://www.cs.ubc.ca/~arnaud/andrieu_defreitas_doucet_jordan_intromontecarlomachinelearning.pdf" target="_blank">[1]</a> An Introduction to MCMC for Machine Learning.<i> Andrieu, Freitas, Doucet, and Jordan</i><br>
<a href="http://statweb.stanford.edu/~owen/mc/Ch-var-is.pdf" target="_blank">[2]</a> Importance sampling. <i>Art Owen</i><br>



