---
layout: post
title: Will Sun Rise Tomorrow? From Bayesian View
tags:
- bayesian
- probability
---

This question might seem silly, but it is a valid question to ask. In fact, famous mathematician <a href="https://en.wikipedia.org/wiki/Pierre-Simon_Laplace" target="_blank">Pierre Simon Laplace</a> studied it before. Most people think that sun will certainly rise tomorrow. But If you ask them why they will be so certain, they will have a hard time to come up with a reason.<!--break-->

we always make assumptions and we often do so without acknowledging. we have seen sun rises everyday and then assume that the sun will rise tomorrow. Past experience has shaped our belief about sun rising tomorrow. That's why we are so "certain". Now you might object and argue that because of science, you are certain. But science is made out of many models to explain different pieces of our world. Even successful models can have rooms for doubts, like Newton's laws. 

Let's show how a baysian will think about this problem. Let's model sun rises as bernoulli random variable. Since we don't know any better, we model and the probability of sun rises each day as variate $\pi$, with a uniform distribution from 0 to 1, $\pi \sim Beta(1,1)$. Then we will collect data $D$ about how many times sun rises in $m$ days. Let's say we get n days out of m days that sun rises. Now, we are in good shape for getting better informed idea about $\pi$, $p(\pi\|D)$.

$$
\begin{align*}
p(\pi|D) & = \frac {p(D|\pi)p(\pi)}{p(D)}
\\ & \propto p(D|\pi)p(\pi)
\\ & = \pi^n (1-\pi)^{m-n}
\end{align*}
$$

From the result, we can see that $p(\pi\|D)$ is also a beta function, $Beta(n+1,m-n+1)$. Since you can reach to my website and read until this point, I can safely say that you are old enough to see sun rise for the past 60 days. If not, believe me, for the past 60 days, sun have been there. I'm old enough. Then we can apply this formula to see what is the distribution of the probabilty that sun will rise tomorrow. Click <a href="http://www.wolframalpha.com/input/?i=beta+distribution%2861%2C1%29" target="_blank">here</a> to visualize the distribution.

