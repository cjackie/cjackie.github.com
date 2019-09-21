---
layout: post
title: Understands System Diagram
tags:
- software
- engineering
- architecture
---

Have you seen a complicated system diagram that describes a system architecture. If you like me, seeing a system diagram is intimidating, because such diagram might have dozens or more boxes in it, and boxes are interconnected by arrows. A box is easy to understand; it represents an entity/component/module that serves a specific focused and singular function or task. But what does an arrow mean? The arrow represents a box knows about another box. Say we have two boxes, box A and box B. An arrow is pointing from box A to box B. It means that box A *knows* box B. By knowing box B, box A can use functionalities provided by box B. However, box B does not know box A, so box B cannot use box A's functionalities [1].

To summarize, system diagram consists of boxes and arrows. A box represents a specific focused and singular function or task. An arrow from box A to box B, represents that A knows B, but not necessarily vice versa.


-------------------
[1] At least, box B cannot use box A directly. However let's say there is C which knows A, and B knows C, then B knows A in a indirect way. but as far as B is concern, B does not know A.






