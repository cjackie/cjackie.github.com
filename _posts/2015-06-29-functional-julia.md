---
layout: post
title: Glimpse of Functional Programming Paradigm in Julia
tags:
 - julia
 - programming
---

Julia language is not a pure functional programming language, but It does have supports for doing funcitonal programming. In this post, I illutrate how functional programming paradigm can be used in Julia. This post doesn't assume prior knowledge about functional programming. But basic programming experience is assumed. That is, you should know variable, for loop, array, and function. <!--break--> I think Julia is pretty easy to understand, so it shouldn't be a problem to understand code example snippets. When in doubt though, the <a href="http://docs.julialang.org/en/latest/" target="_blank">doc</a> for Julia is great place to start.

In C, Java, a function(method) is a block of code that takes input arguments and return a value. It's not a function in a sense that a mathmatician will think of, because functions can be used to alter the value of the inputs(In math, if you compute 1+1, you don't want 1 becomes 5 after you get the answer 2). Altering inputs is common in programming languages, which is called programming with side effect. In functional programming however, function has no side effect: the return value is the only window for achieving what you want.

Now I should introduce a notation for describing functions, which is called function signature. A function has two components: inputs and outputs. To showing this two components, we align both together in a line, and they are separeted by -> with last one being output. If a function contains a function, the inner function is enclosed in a parentheses. for example:(a -> b) -> [a] -> [c]. This function signature means that the function takes two arguments. First argument is a function that takes type a returns type b. Second argument is an array of type a. Then the return value will be an array of type c. 

There are some standard functions in functional programming. And functions are called higher-order functions[1]. Among them, filter, foldr, map, zip, unzip are the functions that deal with arrays. These functions are basic yet powerful. Many variance of these functions exist, however those are fairly easy to understand once you know basic ones.

The function signature for map is: (a -> b) -> [a] -> [b]. map is the simplest one in my opinion. It applies the first argument to each elements in an array, then return the resulting array. Example:

{% highlight julia %}
#an array with elements 1, 2 and 3
x = [1 2 3]
#add each element by 2
x2 = map((x) -> x+2, x)
#the result will be [3 4 5]
{% endhighlight %}

The function signature for filter is:  (a -> bool) -> [a] -> [a]. filter walks through every element of an array but apply first argument. If argument function is evaluated and true returns, then that element will be added to the returning array. Example:

{% highlight julia %}
#an array of integer from 1 to 10
x = [1:10]
#filter out non-even elements
x_even = filter((x) -> x % 2 == 0, x)
#the result will be [2 4 6 8 10]
{% endhighlight %}

The function signature for foldr is: (a -> b -> b) -> b -> [a] -> b. This is a function that will apply the first argument, which is a function, to each element in an array and the previous return value from the first argument. It starts from the right to left when iterate through the array. Since foldr needs a previous return value, so it needs a initial value to start with, which is the second argument. The third argument is the array. Intuitively, you can think of it as folding the array down to a single value. Example:

{% highlight julia %}
#array [1 3 5 7 9]
a = [1:2:9]
#add every element together, starting with 0
val = foldr(+, 0, a)
#the result will be 25
{% endhighlight %}

With map, filter and reduce, one can already write very concise code that does complex task by combinating them together. One example is mapreduce framework for prallel data processing[2]. In addition to these three functions, zip and unzip are also useful high-order functions. zip will merge two arrays together and produce an array of tuples. unzip is the opposite. For julia 0.3 version, to make zip to take effect, meaning return a array of tuples. We need to call the function collect on zip.

Now let's show an example of how to composite these functions to do task. I think it's elegent. Let's say we are given dataset of age and income in foreign currency, and we want to compute the average income of young people who are under 30. Foreign currency is hard to value, so we convert it to dollars. Here is the code for achieving that:

{% highlight julia %}
#there are two arrays with the same size: ages, incomes

todollars(x) = 1.4x
#sum of all incomes of people under 30 in dollars
s = foldr(+,
          0,
          filter((x) -> x < 30,
                 map(todollars,
                     collect(zip(ages, incomes))
                     )
                 )
          )
	  
#number of people under 30
len = foldr((x,r) -> r+1,
            0,
            filter((x) -> x < 30,
                   map(todollars,
                       collect(zip(ages, incomes))
                       )
                   )
            )

#average income
agv_income = s/len
{% endhighlight %}

I think functional programming is interesting. For those of you who are interested, I recommend learning <a href="https://www.haskell.org/" target="_blank">Haskell</a>. It will give you a new perspective on writing programs.

Reference:<br>
<a href="http://people.cs.aau.dk/~normark/prog3-03/html/notes/higher-order-fu_themes-intr-section.html" target="_blank">[1]</a> Introduction to higher-order functions<br>
<a href="http://hci.stanford.edu/courses/cs448g/a2/files/map_reduce_tutorial.pdf" target="_blank">[2]</a> A Very Brief Introduction to MapReduce, Diana MacLean 
