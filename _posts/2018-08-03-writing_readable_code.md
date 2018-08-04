---
layout: post
title: Write Readable Code
tags:
- software
---

Code is a text that expresses actions. Actions are movement/transformation of data. 
It is very important to write it in such way that developers can understand. 
Code is a reference to actions it expresses. Readable code is such that
 developers look at it and quickly understand what it does. Readable code is very important to
 both author and readers who will build/use the code. Unreadable code is impossible to maintain, and
 develop incremently, because the burden of understanding takes too much energy away from developers.
 Make readable code is a must path to software developers.
 
The first principle to write readable code is <b>consistent way of coding</b>. 
Consistent way of coding expresses intentions, and easier to understand. What do i mean by it? 
Let me give an example, lets say we have a class that is responsible for interact with a table in
 SQL database. The table stores information about our users. One consistency strategy is for
 every class for interacting with database, we name it such that `service` is appended at the end
```java
public class UserService { }
```
`UserService` class contains methods to retrieve data. A terrible way to naming such methods is to start
with `get`, because it confuses with Java naming convention for getters. Instead, we give it a different 
prefix, such as `find`
```java
public class UserService {
    public User findUsers(long userId) { return null; }
}
```

The second principle is <strong>doing one thing well</strong>. This is equivalent to 
<strong>separation of concerns</strong>. As an example, I want to write a class for handling payment.
The class communicate with third party vendor to do payment transaction,
and keep a record in our database.
```java
public class PaymentProcessor { }
``` 
With the principle in mind, One class is wrong way to do things. We separate the class into 
three classes. One class handles interaction with third party, while the second class handles interaction
with the database. The last one class is functional equivalent to `PaymentProcessor`, but uses previous
two class.
```java
class PaymentVendorProxy {}
class PaymentService {}
public class PaymentProcessor {} 
```
Each classes has well define role to play, and they are easy to unit test.

The third principle is <b>deferring implementation</b>. This principle is equivalent to <b>dependency injection</b> 
This is more of developing software rule, and it is closely related to the second principle. 
As an example, we have a requirement to implement something that will process a file from a third party,
 and we know the format but don't know the way of file transfer. We deter the implementation of retrieving files.
```java
public interface FileRetriever {
    File retrieveFormattedFile();
}
```
Then we can start implementing the processing file without yet knowing how to get the file
```java
public class FileProcessor {
    private FileRetriever retriever;
    
    public FileProcessor(FileRetriever retriever) {
        this.retriever = retriever;
    }
    
    public void process() {
        File file = this.retriever.retrieveFormattedFile();
        // do the processing
    }
}
```

