---
layout: post
title: Faitson - a drone project (proof of concept)
tags: drone, electronics
---

### Intro
I like drones. They give the freedom that human being can't have physically. they are like wings, and with those wings, you can go everywhere, explore the earth. Drones are getting cheaper every day. Despite of my strong desire to buy one, I still don't have one - It's too expensive for me. Even though I couldn't afford to buy one, I already have an project in mind involving drones. This post is my attempt to present the project, at least concept-wise. I would call it Faitson (don't ask why the name :smile:).

### What is the Faitson?
The idea is utterly - A semi-autonomous system that explores the earth. The system can fly to many different places and collect data (All I can think of right now will be pictures). Drones have been able to do that, however they are not automated and they have any restrictions. My system is robust and awesome. It can fly to very far places, and take pictures(data) and then give them to you. Key functionalities that Faitson has to make it possible:

- No batteries change. That means it can operate as long as you want.
- Connected to the Internet. That means the system doesn't have to come back for you to get data it collects.
- It has a brain. The brain is the way to make it 'smart'. And with Internet, 'smart' can be programed remotely.
- It has 'eyes', meaning it can sense what's going on in the environment

### Architecture of Faitson?
There are serveral components in Faitson - power source module(PSM), control unit(CU), wireless module(WM), main body (BM).</br>
Let's first talk about PSM. The module should consist of a rechargable power supply, a solar panel and a small micro-controller. Solar panel is the mean to collect energy from the sun, and power supply is the medium to store energy. Then micro-controller will provide some 'smartness' to the module: 

- Provide signal of energy left. call it PWS_EL.
- Able to trigger ON and OFF. (start charging and stop charging)
- Provide channel to execute command from external signal to trigger ON and OFF.

Here is diagram of PSM:</br>
<img src="{{site.baseurl}}images/2014-08-04/psm.png" alt="PSM">
With this module, Faitson will be able to  fly for a long time without you to replace a power supply.</br>

Now, let's talk about wireless module(WM). WM, obviously, provides the Internet access. In order for Faitson to go anywhere and still be able to access the Internet, WM will be using GSM with a sim card. It can use very low level chips to like [GSM/GPRS M10](http://www.quectel.com/product/prodetail.aspx?id=14), for greater controll. Or It could use existing modules like [this](https://www.sparkfun.com/products/9533), for convenience, and save time, but higher price. Faitson would use 2nd approach (for simplicity).</br>

Then, there is the main body, which consists of a drone, various sensors and maybe a small chip. The main body will be responsible for moving(drone) and collecting data(sensors), which can be communicated via the small chip with the CU.</br>

Last but not least, there is the control unit(CU). CU is the "brain" of Faitson, where we program it to coordinate the whole system. PSM provide power source info to CU and give CU the controll over to CU. WM provides access to Internet for CU, so that CU can be communicated remotely. And CU can controll over the main body, so that Faitson can move.</br>

In this architecture, all modules can virtually talk to each other through CU, which provides huge flexibility for us to program. Below is a diagram to illustrate the architecture:
<img src="{{site.baseurl}}images/2014-08-04/architecture.png" alt="architecture">

### Basic algorithm for Faitson


### How to "manufacture" Faith

I put

### Side notes







