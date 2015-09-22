---
layout: post
title: Basic Introduction to Julia
tags:
- programming
- julia
---

I think I should do an introduction to Julia, since I used it often in my website. Two fundamental elements are needed to know to get started with Julia: its <i>type system</i> and <i>function</i>. I hope by learning these two elements, you will appreciate how well-design is the language for scientific computing.<!--break-->

Let us talk about type system first. Julia has dynamic type system like other high-level languages. However, each variables has type associated with it, either by inference or explicitly specified by the programmers. for example,

{% highlight julia %}
n = 10                    #the type Int is inferred
m::Float64 = 10.3         #m is explicitly decleared as a float with 64 bits
{% endhighlight %}

The type is Julia is a place where data is stored. You can think of it as a object in object-oriented programming language like Java, without methods associated with it. But the type system does more just stores data; It provides several nice ways to organize data.

First of all, in Julia you can combine types together to form a new type, which is similar to struct in C language. In Julia, It is called a <i>composite type</i>. For example, we can define a type called Cat, with two data inside, 

{% highlight julia %}
type Cat
  name::ASCIIString      #the name of a cat
  cuteness::Int
end
{% endhighlight %}

To somehow organize different, Julia have something called <i>abstract type</i>. Abstract type is a type you can not assign concrete values to it. It is just a name tag without data inside, however you can make a subtype of it. This provides a way to declare hierarchical relationships among data types. For example,

{% highlight julia %}
abstract Animal           #we have a abstract type, called Animal
type Cat <: Animal        #<: is the syntax for declare "subtype of"
  name::ASCIIString
  cuteness::Int
end
type Dog <: Animal
  name::ASCIIString
  cuteness::Int
end
{% endhighlight %}

Another important type in Julia is <i>parametric types</i>. It is similar to the concept of templates in C language. It will gives us extra flexibility to express our type. For example, if we want a type call AnimalLover, we can express it by,

{% highlight julia %}
type AnimalLover{T<:Animal}    #the bracket means the things being parameterized
  owner::ASCIIString
  animal_name::T
end
{% endhighlight %}

There are several other features in Julia types system, like <i>type union.</i> and <i>immutable type</i>. They are all interesting. But the three I have introduced should be sufficient for starters.

If we have a type that we want to use for storing data, we can construct a variable with the type,

{% highlight julia %}
mydog = Dog("Argo",10)              #construct
howcute? = mydog.cuteness           #access to a field
{% endhighlight %}

So far we have talked about how Julia store and organize data. Next, we will talk about how it transforms or modifies it. To do that, we declare a function that operates on the data,

{% highlight julia %}
#last line will be the return value if return is not specified
function clone(d::Dog)
  Dog(d.name, d.cuteness)
end
#It is a Julia convention to make function that has side effects ends with !
function increase_cuteness!(d::Dog)
  d.cuteness = d.cuteness+1
end
{% endhighlight %}

The function name can be overload. The function will be invoked by signature of the function call, via <i>multiple dispatch</i>.

In OOP, functions and data are glued together in a class. It is a good abstraction in programming in general situation, where we constantly modify state by doing side effects. But, it is not suitable abstraction for doing scientific computing. The separation of function and data is the right one, because that is what being done in mathematics - the language of science and engineering. Types of math are all number-like types. They are standalone objects. But we can doing interesting things by applying functions to it. It is like transforming a number to another number. It will be absurd to have side effects in math. for example, if we apply $+$ on $1$ and $2$, we get back $3$, then $1$ changes to let's say $10$.

I hope this blog helps. If you want to know more details, you can read the Julia <a href="http://julia.readthedocs.org/en/latest/manual/">docs</a>
