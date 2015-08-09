---
layout: post
title: Mathematical Explanations to Laws in the Book, <i>Capital in the Twenty-First Century</i>
tags:
 - books
 - economics
---

Simplicity is the best. When a theory or mathematical model gets too complex, on one hand, It becomes hard to reason about it, on the other hand, sometimes the theory is only tuned for a special case, which sacrifices generality. Laws of capitalism in the book, <i>Capital in the Twenty-First Century</i>, are good examples of simplicity. They are simple yet powerful. They can be the basic building blocks to think about macroeconomics.<!--break-->

First law links the capital stock to the flow of income from capital (p. 52)

$$
\begin{equation}
\alpha = \gamma \times \beta
\end{equation}
$$

Where $\alpha$ is the capital's share in the national income, $\gamma$ is the rate of return on the capital, and $\beta$ is capital/income ratio.

(1) is easy to derive. It follows immediately from the definition of each terms. Let $c$ denote capital, and $i$ denote national income, then

$$
\begin{align*}
\gamma \times \beta &= \gamma \times \frac{c}{i} \\
&= \frac{\gamma \times c}{i} \\
&= \alpha
\end{align*}
$$

The second law relates the capital/income ratio $\beta$ to saving rate and growth rate (p. 166)

$$
\begin{equation}
\beta = \frac{s}{g}
\end{equation}
$$

where $s$ is saving rate and $g$ is growth rate of the national income.

(2) is says that in long run, capital/income will be equal to saving rate divided by growth of nation income. The derivation of (2) is less straight forward than that of (1). To derive it, let's imagine there is a initial capital at a year $t_0$, which is denoted by $c_0$. Let $i_t$ denote national income after $t$ years starting from $t_0$. Then after $n$ years, the capital/income will be

$$

\begin{align}
\beta(n) &= \frac{c_0+i_0s+i_1s+\cdots+i_ns}{i_0(1+g)^n} \nonumber \\
         &= \frac{c_0+i_0s+i_0(1+g)^1s+\cdots+i_0(1+g)^ns}{i_0(1+g)^n} \nonumber \\
	 &= \frac{c_0}{i_0(1+g)^n} + s(1+\frac{1}{1+g}+\frac{1}{(1+g)^2}+\cdots+\frac{1}{(1+g)^n})
\end{align}
$$

In long run, $\beta$ will approach $s/g$. Formally, by Taylor series

$$
\begin{align*}
\lim_{n \to \infty} \beta(n) &= \cancelto{0}{\frac{c_0}{i_0(1+g)^n}} + s\cancelto{\frac{1}{g}}{(1+\frac{1}{1+g}+\frac{1}{(1+g)^2}+\cdots+\frac{1}{(1+g)^n}) }\require{cancel}\\
                             &= \frac{s}{g}
\end{align*}
$$

From the derivation, we can see there are many implicit assumptions for the second law. For example, mathematically $g$ must be greater than 0. There are also economical assumptions, such as $g$ and $s$ is fixed over time, and past capital won't grow itself. However, if this equation is for analyzing past period, these assumptions are okay to assume. You can think of $g$ and $s$ as the "average" of the past, and they can convey something about the reality. Refer to the book for more details discuss about the law and the reality.
