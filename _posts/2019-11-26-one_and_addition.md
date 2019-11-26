---
layout: post
title: One, and addition
tags:
- math
- recursion
---

Suppose all one knows is one (1) and addition (+).

$$
f(1) = 1, f(2) = 1+1, f(3) = 1+1+1, ...
$$

$$
f(n) = f(n-1)+1
$$

$$
g(1) = f(n), g(2) = f(n)+f(n), g(3) = f(n)+f(n)+f(n), ...
$$

$$
g(n) = g(n-1)+f(n)
$$

$$
h(1) = g(n), h(2) = g(n)+g(n), h(3) = g(n)+g(n)+g(n)
$$

examples

$$
f(2) = f(1)+1 = 1+1
$$

$$
g(2) = f(2)+f(2) = (1+1)+(1+1)
$$

$$
h(2) = g(2)+g(2) = ((1+1)+(1+1))+((1+1)+(1+1))
$$

let's then do this

$$
f_0 = f, f_1 = g, f_2=h, ...
$$

$$
\overline{f}(n) = f_n(n)
$$

$$
\overline{g}(n) = \overline{g}(n-1) + \overline{f}(n)
$$

$$
\overline{h}(n) = \overline{h}(n-1) + \overline{g}(n)
$$






