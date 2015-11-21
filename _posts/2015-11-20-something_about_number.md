---
layout: post
title: Sense of Number
tags:
- math
---

Number is something very interesting. It is abstract, yet it feels so concrete and real. The concreteness comes from our daily usage of numbers, which can be helpful ,and illusional well. <!--break-->

For a computer science, computer engineering or related majors, there are some numbers that we are quite familiar. For example, power of base two numbers: $2^1, 2^2, 2^3, ..., 2^{10}$. Important units like KB,MB,GB coming from these number - $KB = 2^{10}B$, $MB = 2^{20}B$ and $GB = 2^{30}B$. These number is very helpful to keep in mind; when we reason about something that is quantitative, these number can be used as a benchmark for comparing. For example, in computer science, complexity is an important metrics, which could be time complexity or memory complexity. Let say we have an algorithm that has $O(n)$ complexity, which is pretty good. But how good is it in practice? To answer this question, we need to know what is $n$ roughly for a given problem. If n is in the order of $9$, which is roughly $2^{30}$, then the algorithm will take in order of seconds. This is because clock speed of modern computer is in the order of 9 since it is few GHz speed. Once our complexity tells us our program takes in the order of seconds, the constant part of $O(n)$ becomes important. For example $10000n$ is also $O(n)$, which in practice will result in significant different; the coefficient will slow down the program a lot.

Another example of the helpfulness of power of base two numbers is memory usage. Nowadays, we have way more data than ever, but our computer RAM is finite. There are many algorithms consumes large amount of data, so the ability to estimate in magnitude how much data we can fit into our computer can be very helpful. In last kaggle competition, I was given 2 GB of data, once it was read, it quickly exceeded the amount of memory I had in the computer. If I had estimated the memory usage, I could have been more cautious about memory usage when I implemented my algorithm, which could save time.

The number can be illusional sometimes. When we see something, our brain will search in our memory for similar things to get sense of what that "something" is. So when we encounter a number, we might have a different impression about what that number implies based our memory. I have experienced first hand. Chinese has names for every order of increase in number, like a thousand, we call it 千(qian), and a 10 thousand, we call it 万(wan). Once, I read something in Chinese about a number that ends in <i>wan</i>, I felt it was a large number, then I read the same thing again in English, which presented it in 10 thousand, and I felt it was not that large anymore. It was because, when I read it in Chinese, it triggered the memory of <i>wan</i>, which gave me the illusion of big, while in English I didn't have pass memory that told me it was big.

The property of illusion of numbers have been exploited a lot in different contexts. For example, if one wants to persuade people that a new disease is lethal and needed immediate attentions. If the death rate is only 0.1 percent, one can put it differently to boost its severity; One can put it one thousand out of 1 million people who contracted the disease died. The thousand and million will trigger a sense of big for us.

There are other interesting things about number, like infinity, $\pi$. They need another standalone blog.



