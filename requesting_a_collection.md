How to properly request to start collection 
===========================================================

#Collecting Terms in Tweets (track) - For us to start a collection we need two things to collect TERMS in tweets:

##1. We need the terms you want collected from twitter.

Here's how the logic works for getting raw tweets from twitter, we can:

###1 - Get tweets containing "good" AND "world" by giving the streaming API an input like so "good world" -> spaces between words look for BOTH words in a tweet.

So if you wanted to look for the words "good" AND "world" in a tweet you could give us an input like so:

"good world" and it could give you a tweet like so:

"I am a very good person, I live in a wonderful world."

or a tweet like so:

"I love clouds; this is a good world." 

###2 - Get tweets containing "good" OR "world" by giving the streaming API an input like so "good, world" -> commas between words look for EITHER word in a tweet. This will return tweets with one of the terms or BOTH of the terms. It is a logical OR, not an exclusive XOR. 

So if you wanted to look for the words "good" OR "world" in a tweet you could give us an input like so:

"good,world" and it could give you a tweet like so:

"I am a very good person, I live in a wonderful world."

or a tweet like so:

"I love the world." 

or:

"God is good."


###2. We need a list of terms you want post filtered. 

Post filters are a way for you to enforce certiain rules onto a tweet that you couldn't enforce with the above basic track inputs to the twitter streaming API.

### `field_contains` post filter: 

One way to use this is to enter keywords/phrases you want matched like so:

field_contains(tweet, 'NYC', 'good society') - (checks tweet['text']) would match the word NYC and the phrase NYC on the post filter.

You can also use it to match fields on the twitter object like the screen name or userid:

field_contains(tweet, 'user.screen_name', 'bob', 'alice') - (checks tweet['user']['screen_name'])

Would setup a post filter to match screen_names (twitter handles) that had the string "bob" or "alice" inside of them:

so "@bob_123" or "@alice" or "@alicezzzzzz" would all match.

So to request this post filter you would say something like in an email:

" For the field_contains post filter get me these terms: 'NYC', 'good society' "

### `field_contains_case_sensitive` post filter:

This post filter is the same as above but it is case insensitive.

So to request this post filter you would say something like in an email:

Same as above.

### `place_name_contains` post filter (checks tweet['place']['full_name']):

This post filter will only keep tweets where the `place` field of a twitter object.

place_name_contains(tweet, 'Kiev') would get place fields that contained 'Kiev'.

place_name_contains(tweet, 'Kiev', 'Paris') would get a field that contained 'Kiev' or 'Paris'.

So to request this post filter you would say something like in an email:

" For the place_name_contains post filder get me these terms: 'Kiev', 'Paris', 'Berlin' "

### `user_description_contains` post filter (checks tweet['user']['description']):

This post filter is for matching words or phrases to the text inside a user's description field.

user_descriptions_contains(tweet, 'Cow', 'moon dance') would match user descriptions with the words 'Cow' and the phrase 'moon dance' like so:

"I am a cow and I do a little moon dance." or "I am a cow."" or "I do a little moon dance."

So to request this post filter you would say something like in an email:

" For the user_description post filter get me these terms: 'Cow', 'moon dance' "

### `user_location_contains` post filter (checks tweet['user']['location']):

This post filter is for matching words or phrases to the text inside a user's location field.

user_location_contains(tweet, 'The surface of the sun', 'San Francisco') would match user stated locations like so:

"I live on the surface of the sun AKA San Francisco" 

or

"San Francisco"

or

"The surface of the sun"

So to request this post filter you would say something like in an email:

" For the user_location_contains post filter get me these terms: 'San Francisco', 'The surface of the sun' "

### `within_geobox` post filter (checks to see if a tweet is geotagged and within the give box):

within_geobox(tweet, -75.280303, 39.8670041, -74.9557629, 40.1379919) would match geotagged tweets within the box given by those four coordinates.

So to request this post filter you would say something like in an email:

" For the within_geobox post filter get me geotagges tweets within this box: [-75.280303, 39.8670041, -74.9557629, 40.1379919]"

##Collecting Tweets from Specific Users (follow) - For us to start collection we need one thing:

#1. We need a list of user ids you would like to follow.


##Collecting Tweets from a specific Geobox (geo) - For us to start a collection we need one thing:

#1. We need the geobox in terms of geographic coordinates you would like the tweets collected in.






