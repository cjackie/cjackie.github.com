---
layout: post
title: Challenges of Distributed Computing
tags:
- distributed
- computing
- network
- software
---

distributed computing is a computation task done in several computers over network. Compared to a computing done in a single computer, distributing computing has more challenges. A simple distributed computation involves two servers server A, and server B. Server A is connected to server B via network. Server A calls server B synchronously for a computation.

<img style="margin:auto" src="/images/blog/challenges_of_distributed_computing1.png">

Things can go wrong in this picture,
- A calls B, but B does not receives the call
- A calls B, but A ignores/cancels B response before B returns
- B returns, but A does not receive the response

In a computation done in single machine, where a function A calls another function B. the problems above will not happen. When function A calls function B, we know B is going to receive the request and returns at some point in time, as long as we assume the machine does not halt. However in distributed computing, these problems can happen due to
- Servers are connected over the network.
- Network can be down and unstable
- Servers execute and fail independently

These problems are entirely not new. They are studied in computer network for problem of transmitting a package from computer A to computer B. The solution from the computer network can be applied to solve the problem of not receiving a request or response from a server in distributed computing. Although the problem of receiving a request or response in distributed computing can be hidden from the software developers by a framework/protocol that hides the details of receiving a request/response, the problem of cancelling a call cannot be hidden. The framework can guarantee that when server A cancels B, that B will eventually receive the cancel signal. But as to how B handle the cancel signal, it depends on the nature of the application. For example, if server B behavors as a pure function like computing whether or not a given number is prime, B can ignore the cancel signal. On the other hand, if B is a server that updates bank account balanace, B must handle the cancel signal when it receives the cancel signal from the framework after updating the bank account balance.


