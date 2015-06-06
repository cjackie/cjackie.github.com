---
layout: post
title: Probability Estimation From Insurance Rate
tags:
- analysis
---

<p>
Few days ago, one of my friend told me about a life insurance that his relative was about to get. He told me roughly how it works, and I immediately sensed that given those information, one should be able to estimate what is the probabity underlying to determine the rate. Let me explain how this life insurance works. I will abstract away real numbers to protect his privacy. The life insurance is "protecting" one from sudden death for $t$ years. and the insuree will pay $m$ amount of money every year until he passes away or $t$ year reaches. If $t$ years passes, and the insuree is still alive, all money he pays will go waste, However if he dies before that, his family will get $D$ amount of money.
</p>
<p>
Given these number, one should be able to estimate probability of death for each year, because the probability is what eventually how the insurance fee is derived. So with that in mind, I want to do the estimations. To do that, one principle is used: the insurance company will do its best to make profits[1]. Let's define two random variables: $X_g$ and $X_l$. $X_g$ denotes the random variable that the amount of money the insurance company will gain from the insuree. $X_l$ denotes the random variable that the company will lose to the insuree. Here I need to make a simple assumption in order to get $X_l$ and $X_g$: event of the insuree pass away ocurrance is a bernoulli process with probability $\rho$, and will be terminated until the event happens. In other words, each year the insuree will have a probability of $\rho$ pass away. In this simple model, one can easily assign probilities to interest events, namely the insure dies on first year, second years, e.t.c. From these events, one can easily derive the distribution of $X_g$ and $X_l$. Specifically,
$$X_g \sim Categorical(1-\rho,\rho(1-\rho),\rho^2(1-\rho),\dots,  \rho^{t-1}(1-\rho), 1-\sum_{i=1}^{t} \rho^{i-1}(1-\rho))$$
$$X_l \sim Catergorical(\sum_{i=1}^{t} \rho^{i-1}(1-\rho), 1-\sum_{i=1}^{t} \rho^{i-1}(1-\rho))$$
Now, use principle presented at[1], and assume that it's a competitive market where the insurance company can hardly make profit, so we have $E[X_g]=E[X_l]$. One equation, one unknown, we can solve for $\rho$. Specifically, the equation for $E[X_g]$ and $E[X_l]$ will be 
$$E[X_g]=\sum_{i=1}^{t} mi\rho^{i-1}(1-\rho)+tm(1-\sum_{i=1}^{t} \rho^{i-1}(1-\rho))$$
$$E[X_l]=D(1-\sum_{i=1}^{t} \rho^{i-1}(1-\rho))$$
</p>

