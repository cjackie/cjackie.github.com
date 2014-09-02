---
layout: post
title: Functional programming meets real world
tags:
 - programming
 - paradigm
---

### Haskell is useless
A few weeks ago, I came across a video called [Haskell is useless](https://www.youtube.com/watch?v=iSmkqocn0oQ) when I was learning haskell. I was intrigued by the title, because It was listed on the haskell website! The video itself is very informative. People in the video are the very people who design and maintain Haskell. </br>
In the video, Prof. Jones categorized programming languages according to two main characteristics: one is usefulness and the other is safety. Most noticeably, C would be very useful yet unsafe. on the other hand, Haskell is safe yet useless. Usefulness is achieved by allowing side effects, which is inherently unsafe, although the safety can be enhanced by good practice, like closure and objected oriented way. And then there is Haskell, representing the functional world where there is no or little side effects. Haskell is a pure functional programming language. which has no side effects, but 'useless'. And the recent trend is that both trying to achieve safety and usefulness. </br>

<!--break-->

Below is to illustrate the differenet languages' usefulness and safety.

```
         ^ 
useful   | C Java        SQL            'utopia' :)
         |                    
         |
         |
         |                    Lisp
         |                                Haskell
useless  |--------------------------------------->
          unsafe                             safe
```

### SQL and Haskell
In the video, Prof. Jones talked about SQL has borrowed many ideas from functional programming languages like Haskell in its design. At first I didn't understand why. But after learning about database from [a coursera class](https://www.coursera.org/course/datasci), I started to understand why.</br>
There are some similarities between two languages:

- Both are declarative languages, meaning we, as programmers, express our algorithm in the code as oppose to write out each steps one by one. Two advantages doing this: 1. increase productivity. 2. leave room for optimization by the compiler
- Both do things in the "functional way", meaning they achieve effects by transforming dataflow. This limits side effects on the data, and makes it more predictable, therefore improve safety.

### Database now
Nowadays, as data size increases exponentially and hardware gets cheaper every day, there is a trend for database go parallel. By moving from traditional databases provided by Oracle or IBM to parallel, companies can save tons amount of money. So recently, many database started to appear. Noticeably new kind of database has started to emerge - [NoSQL](http://en.wikipedia.org/wiki/NoSQL). NoSQL do things parallel. It's hard to programming in the parallel because of side effects(unsafe). Traditionally, we use some kind of lock to ensure data integrity. However, if we embrace functional programming way, it would be easier to work in parallel. I think NoSQL databases will have some flavors of functional programming in their implementation. 

### Haddoop and function programming
I know that Haddoop does things in functional way in order to do things in parallel easily. Haddoop is an implementation of a framework called MapReduce. The name tells us all how it is implemented - map and reduce. if you know a little bit about functional programming, you must have heard or used map and reduce. Map is a function applying to each one in a collection, and reduce use a function to compute a result of a collection. This basically how it works in Haddoop. in Haddoop you just need to write any combinations of map and reduce to achieve things, and it will make computation process in parallel. This framework is very powerful and become very popular to process terabytes or petabytes of data. wow, that's awesome.

### Reactive programming!?
What's reactive programming? At first, I was intrigued by the name. After I read [a gist](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754), I felt like it's just a special practice of functional programming, where everything is dataflow transformation like SQL. They claim that It's the future to solve ever increasing complexity of UI. It looks interesting, let's see if it will get traction.

### Summary
functional programming is becomming more and more important. Even though, functional programming languages themselves haven't gotten big traction, their influence is undeniable. mainstream programming languages and real world problem has taken ideas from functional programming languages to solve hard problems, and it works very well. :)





