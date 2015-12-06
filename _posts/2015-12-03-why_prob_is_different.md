---
layout: post
title: Probability
tags:
- probability
- math
---

For people who study probability for the first time in college, they will probably say it is a difficult subject. Probability is a type of mathematics, however students who excel at first year calculus class can still find probability difficult to grasp. But why? What makes it difficult and different? I have learned probability in three course: two of them were undergraduate courses, and the third one was graduate course. Right now, I still remember vaguely what is like not knowing probability. I should take the chance and write about what makes it different. <!--break-->

First of all, let see what is difference between calculus and probability in mathematics. I found two important difference. The first one is the representation. In basic math, we talk about single numbers only; whereas in probability, we think about it in tuples with 2 elements. Let us say we have a function

$$
y = g(x)
$$

$y$ is what we obtain when we apply the function $g(\bullet)$ on $x$. Once we have the answer $y$, most of us rarely think about the $x$. Even though, $g(\bullet)$ can be defined as a list of tuples, but most of us see it as whole. Another important concept in calculus is derivative, which can be denoted as,

$$
z = \frac{\partial g(x)}{\partial x}
$$

Once again, most of us think of derivative of something as a number, and ignore other aspects, such as underlying $x$ and $g(\bullet)$. It is reasonable, given that human can only think of one thing at a time. Holding multiple symbols together requires some trainings.

In probability, we are forced to think of it as a tuple. Let us say we have $(a,p)$, where $a$ is a number or an object, and $p$ is probability. It would not make sense if we only talk about either $a$ or $p$. For example, following sentence is a valid sentence about probability: "Rolling a die and getting a $6$ has a probability $\frac{1}{6}$". But the following two sentences do not: "Rolling a die and getting $6$. Probability is $\frac{1}{6}$". We see that $6$ and $\frac{1}{6}$ have to go together.

The second difficulty is many mathematical consequences in probability can be very counter-intuitive for beginners. In my opinion, the counter-intuition comes from not being able to see the whole picture. Probability is relative and intertwined; the probability of an event happening depends other events. Bayes rule can illuminate this property:

$$
P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum_{i} P(B|A_i)P(A_i)}
$$

Bayes rule is for doing inverse probability. That is when the probability relationship from $A_i$ to $B$ is obvious, but we want the inverse one, namely $B$ to $A_i$. Bayes rule tells us how to do it. It is likelihood $P(B\|A_i)$ multiply by prior $P(A_i)$, which shows the "inter-wined", then normalize it by $\sum_{i} P(B\|A_i)P(A_i)$, which shows the "relative". 

Without proper training, the intuitions from real world experience mixed with mathematics can be very confusion, especially for probability; some mathematical consequences can be counter-intuitive and some real world intuitions can be misleading. However, the mathematical intuitions can be improving by extensive training in mathematics.
