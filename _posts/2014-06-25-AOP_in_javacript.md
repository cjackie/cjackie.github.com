---
layout: post
title: Aspect-Oriented Programming in Javascript
tags: javascript, paradigm
---
##Aspect-Oriented Programming
It might sound complicated, but the idea is in fact very simple, which is adding new behavior to a function. This can be done using in object-oriented way, but for some problems, AOP is a better solution. Let's say you would like to print something before the call, and print something after that call for debugging purposes. Of course you can just make a subclass and add those functionality. However, it feels very unnatural. With AOP, it's straight forward: add one behavior before the call and another one after the call. The abstraction really free you from thinking details about class relationships, and other methods, and make you focus more on what the code does.<br>
  Let's give an example of AOP:
  
```javascript
function Person(name) { 
  this.name = name
}

Person.prototype.say = funciton() {
  console.log(this.name);
}
```

Now you make an 'instance' of it (in reality, better call it create a new an object)

```js
var jack = new Person('jack');
```

Then you change you mind and say, "you know what, let's say 'hello everyone' before say the name". You just want to change the `say` function, nothing else.

```js
var say = jack.say;
jack.say = function() {
  console.log('hello everyone');
  say.call(jack);
};
```

Thanks to closure, it works. That's it, 4 lines of codes. Now, whenever jack call `say` function, it will print out 'hello everyone', before whatever old method say does. Wow, this is neat. <br>
Let's break it down here. `var say = jack.say;` this is used to save the reference to original `say` function. then we redefine the `say` function for jack, `jack.say = function() {...};`. Inside the function, we will say hello to every, `console.log('hello everyone');`, then call the original function `say.call(jack);`. `say.call(jack);` is the way to invoke the old function, you might wonder why don't we just invoke the function like `say()`. This is because that `say` has different context, when it should be within the `jack` context. so we need to reinforce the context by using the method [call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
