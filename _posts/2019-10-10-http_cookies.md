---
layout: post
title: HTTP Cookies
tags:
- software
- engineering
- web
- website
- security
- technology
- brower
- protocol
---


HTTP is a stateless protocol, which means protocol does not have state. In other words, an HTTP request and response does not update some states which can be persisted in the subsequent requests and responses. For some feature of a website, there needs to have some ways to persist data between requests. For example, lets there is a user called Bob. He registered an account on a website with his email and password. Bob verifies himself with a credential such as email and password. When the website receives a request saying “I’m Bob, I have the credential email and password” [1]. If there isn’t a way to persist data, then Bob needs to verify again with the credential for every request. HTTP protocol does not have state, but browsers who implements the HTTP protocol adds a way to persist state. The state is called cookies. When the request is sent to a web server, and the web sends back with a response. In the response, an HTTP header Set-Cookie can be attached. The Set-Cookies is special HTTP header that tells the browser to remember the value of the Set-Cookie along with an expiration date [2]. The browsers attach the cookie (value of Set-Cookie)  in the subsequent requests. With the cookie, once someone with the credential has been verified, the web server sends back a cookie that presents that “someone with the credential has been verified”. The browser send the cookie “someone with the credential has been verified” to the web server in the subsequent HTTP requests.

THere are two types of cookies. One is the first party cookie, and the other one is the third party cookie. This distinction on the cookie is from the perspective of the web server. A cookie received by the website A, but set by the website B, is a third party cookie from the perspective of the website A. On the other hand, a cookie received by the website A and is set by the same website A, is a first party cookie from the perspective of website A. Third party cookies can be the cause of problems: security concerns, and privacy concern. Cross-Site Request Forgery (CSRF) is a problem by exploiting the cookie. CSRF is when a malicious website on user’s browser forges a request with a third party cookie from the malicious website’s perspective, and sends it to the web server being attacked who created the third party cookie. The web server being attacked sees the cookie and then thinks it is from the user, and executes the request.

CSRF works when
1. The malicious site obtains the third party cookie
2. The malicious site know what the third party cookie belongs to
3. The website server who created the cookie, allows cookie to be sent from a foreign website
4. The website server who created the cookie, accepts the cookie from other websites.

-----------------------------

reference:

[1] Note that it is not necessarily true that Bob who provides the credential. It might as well be that someone else has the credential.

[2] There are other metadata in the cookie such as Domain, Path, Secure and so on. Each metadata instructs the browser different behaviors with regard to the cookie.

