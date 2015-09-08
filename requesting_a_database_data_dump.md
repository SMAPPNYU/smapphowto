How to properly request to a data dump
======================================

#Getting data from a database - For us to get data from a database we need a few things.

##1. We need the rough amount of data you are looking to get.

If size is no issue just say 'size is not an issue.'

Otherwise let us know the maximum data you can hadndle.

"I can only handle 5GB of data, no more than 5GB."

##2. We need the collection you want to get data from.

Tell us the collection you are trying to get the dump from.

The specific collection name is preferable.

For example:

"Hey could you guys dump me the data from the Argentia_Politicians collection."


##3. We need the terms, dates, and other filters you want applied to the data dump.

Tell us the filters you want applied to the data.

If you want tweets since (05, 05, 2014) (day, month, year) until (25, 05, 2014) you need to tell us that.

If you want tweets containing words you need to tell us " I need tweets containing these key words :"

'bieber', 'justin', 'drinking', 'concert', 'marriage'

If you want tweets in a certain language (algorithmically determined tweet language) you need to tell us so we can look up the language code.

If you only want tweets from a user with a certain stated language n their profile (self identified language) tell us that.

If you want the user_location to be from a certain place you need to tell us that. So like you would say something like "the user location should be 'new york' "

If you only want geo tagged tweets or non geo tagged tweets you should tell us that.

Anything I did not metion here should be documented in the smapp-toolkit (some things are definitely missing from the docs though so don't hesitate to ask):
<a href="https://github.com/SMAPPNYU/smapp-toolkit">https://github.com/SMAPPNYU/smapp-toolkit</a>