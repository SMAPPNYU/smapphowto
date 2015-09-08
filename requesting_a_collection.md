How to properly request a collection from a SMaPP programmer
===========================================================

##For us to start a collection we need two things:

###1. We need the terms you want collected from twitter.

Here's how the logic works for getting raw tweets from twitter, we can:

1 Get tweets containing "good" AND "world" by giving the streaming API an input like so "good world" -> spaces between words look for BOTH words in a tweet.

So if you wanted to look for the words "good" AND "world" in a tweet you could give us an input like so:

"good world" and it could give you a tweet like so:

"I am a very good person, I live in a wonderful world."

or a tweet like so:

"I love clouds; this is a good world." 

2 Get tweets containing "good" OR "world" by giving the streaming API an input like so "good, world" -> commas between words look for EITHER word in a tweet. This will return tweets with one of the terms or BOTH of the terms. It is a logical OR, not an exclusive XOR. 

So if you wanted to look for the words "good" OR "world" in a tweet you could give us an input like so:

"good,world" and it could give you a tweet like so:

"I am a very good person, I live in a wonderful world."

or a tweet like so:

"I love the world." 

or:

 "God is good." 


###2. We need a list of terms you want post filtered. 

Post filters are a way for you to enforce certiain rules onto a tweet.



