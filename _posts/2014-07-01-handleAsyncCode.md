---
layout: post
title: Ways to handle asynchronous code in Javascript
tags:
 - javascript
---
Yesterday, I came across function generators in Javascript, which is very similar to Python's function generator. The function generator is characterized by the keyword `yield`, which will suspend the function when it's called with `next()`. That's my simple understanding of function generator. I think it's trying to mimic lazy evaluation in languages like Haskell, and this makes infinite data structure easy to be expressed. <br>
Anyway, I found function generator was because I found [koa](https://github.com/koajs/koa) is using this new feature from Ecmascript 6 to construct async codes in a sync way. I didn't understand how koa can achieve it using `yield` at first (even though I understand function generator). But after I searched more info about it, I started to understand it. From what I understand, koa take all generator functions and call them behind the scene until no more yield. I think it's very neat solution to avoid callback hell and makes asynchronous code more readable if you want to make them execute in a synchronous way. Many solutions have been invented by very smart people in Javascript community, noticeably using promise. libraries like [Q](https://github.com/kriskowal/q) has been able to solve the same problem quite well. This is quite popular, I saw it many times. However, comparing function generator and promise, I think function generator is better to solve sync problems.<br>

<!--break-->

Reason 1: function generator is light weight and it's implemented in native code, as suppose to library. So I will assume it has better performance.<br>
Reason 2: control flow using function generator looks more imperative.

~~~javascript
//using co library
co(function* () {
  var text = yield readFile();
  var webpage = yield get('google.com');
  console.log(text);
  console.log(webpage);
})();

//above is not valid code, just use to illustrate concept.
~~~

whereas, you use promise it will look something like:

~~~javacript
//using library Q
Q.fcall(readFile)
.then(function (text) {
  console.log(text);
  return get('google.com');
}).then(....) 

//above is not valid code, just use to illustrate the concept
~~~

if a person who is not familiar with callback, he or she will be likely to understand first one. indeed, I think the first looks more natural. you just think of it execute step by step. yield will pause the function until async function is finished. Promise approach tries to use `then` sugar to make it appear more natural, but you still need to think about callback(maybe I'm wrong). Anyway, yield appears more natural.

------------------
haha, ecmascript 6 is comming up. lots of new things will be added to the language, like `let`, `for of`, some standard `collections` and more. Let's see how it's gonna be. looking forward to it. :smile:
