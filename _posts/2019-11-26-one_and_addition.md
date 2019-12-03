---
layout: post
title: One, and addition
tags:
- math
- recursion
---

Last updated: 2019/12/01

Suppose all one knows is one (1) and addition (+).

$$
f(1) = 1, f(2) = 1+1, f(3) = 1+1+1, ...
$$

$$
f(n) = \underbrace{1+1+...+1}_n
$$

$$
g(1) = f(n), g(2) = f(n)+f(n), g(3) = f(n)+f(n)+f(n), ...
$$

$$
g(n) = \underbrace{f(n)+...+f(n)}_n
$$

$$
h(1) = g(n), h(2) = g(n)+g(n), h(3) = g(n)+g(n)+g(n)
$$

$$
h(n) = \underbrace{g(n)+...+g(n)}_n
$$

examples

$$
h(2) = g(2) + g(2)
$$

$$
g(2) = f(2) + f(2)
$$

$$
f(2) = 1+1
$$

$$
g(2) = (1+1)+(1+1)
$$

$$
h(2) = ((1+1)+(1+1))+((1+1)+(1+1))
$$

$$
g(2) = f(2)+f(2) = (1+1)+(1+1)
$$

$$
h(2) = g(2)+g(2) = ((1+1)+(1+1))+((1+1)+(1+1))
$$

To express $f,g,h$ in recursion, we need to introduce 0

$$
f(n) = f(n-1) + 1, f(0) = 0
$$

$$
g(n) = g(n-1) + f(n), g(0) = 0
$$

$$
h(n) = h(n-1) + g(n), h(0) = 0
$$

Now, let's then do this

$$
f_1 = f, f_2 = g, f_3 = h, ...
$$

that is

$$
f_n(k) = \underbrace{f_{n-1}(k) + f_{n-1}(k) ... + f_{n-1}(k)}_k
$$

$$
f_1(k) = f(k)
$$

With zero, we can express $f_n(k)$ as

$$
f_n(k) = f_{n-1}(k) + f_n(k-1)
$$

$$
f_n(0) = 0, \forall n
$$

$$
f_1(n) = f(n)
$$

Let's diagonize

$$
\overline{f}(n) = f_n(n)
$$

$$
\overline{g}(n) = \underbrace{\overline{f}(n) + \overline{f}(n)... + \overline{f}(n)}_n
$$

$$
\overline{h}(n) = \underbrace{\overline{g}(n) + \overline{g}(n)... + \overline{g}(n)}_n
$$

examples

$$
\overline{h}(2) = \overline{g}(2) + \overline{g}(2)
$$

$$
\overline{g}(2) = \overline{f}(2) + \overline{f}(2)
$$

$$
\overline{f}(2) = f_2(2) = g(2) = (1+1)+(1+1)
$$

$$
\overline{g}(2) = ((1+1)+(1+1))+((1+1)+(1+1))
$$

$$
\overline{h}(2) = (((1+1)+(1+1))+((1+1)+(1+1)))+(((1+1)+(1+1))+((1+1)+(1+1)))
$$

Let's do this

$$
\overline{f}_1 = \overline{h}, \overline{f}_2 = \overline{g}, \overline{f}_3 = \overline{h}
$$

$$
\overline{f}_n(k) = \underbrace{\overline{f}_{n-1} + \overline{f}_{n-1} + ... + \overline{f}_{n-1}}_k
$$

$$
\overline{f}_1(k) = \overline{h} = 
$$

With 0, we can express $\overline{f}, \overline{g}, \overline{h}$ in recursion

....








