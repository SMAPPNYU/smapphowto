Let's take a quick step back: Why do we shard in the first place?

Bascially sharding is a great way to do something called "horizontal scaling."" Without sharding i need to maintain a large number of servers and each collection is stored on one server. So if the Canada_Election collection would be stored on serverone, and I'd have to log into the mongod instance running on serverone and grab the collection from there. If another collection Canada_Geobox is stored on another server I have to go and track it down there.  This gets harder and harder as we increase the number of servers. If would be cool if we could just keep all the data on one server, but servers have capacity limits (if I have 100,000 databases I'm constantly writing to and reading from one server can't handle that so well) and space limits (server hard drive/disks fill up, self explanatory). So we want a way to treat all of our data as if it was one one server, but in reality we want to be able to have it on different servers so we can read/write it efficiently and so we can add extra servers when we need more space.

Enter sharded mongoDB databases.

A sharded database essentially aggregates multiple 'mongod' (mongo database) instances (multiple running databases) and makes them accessible via a single running instance called the 'mongos' (mongo shard) instance. A collection in mongos instance can be stored on ONE shared so 100% of the data in a collection can be located on shard1 (replica set1), this is effectively just like having a regular mongodb database and there's usually no reason for doing this. Conversely, a collections data can be spread out. 50% can go on shard1 (replica set1 or mongod1) and 50% can go on shard2 (replica set2 or mongod2). In otherwords a collection even though it is 100% queryable and visible on the mongos instance is actually stored across several different servers. 

Concepts you should be familiar with before tackling this guide:

Replica Sets: Essentially just mongod instances that clone each other's data. So a replica set with three mongod instances will have the same data on each instance. You can read about how to setup a basic replica set here:
<a href="http://docs.mongodb.org/master/tutorial/deploy-replica-set-for-testing/">
http://docs.mongodb.org/master/tutorial/deploy-replica-set-for-testing/
</a>

Config Servers: Servers that store metadata/organizational info for a sharded cluster. They help us deteremine which data in a collection is stored on which shard of our sharded database. You can read about how to setup basic config servers here:
<a href="http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/">
http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/
</a>

Shard: More of an abstract concept than anything. Shards are ways to split up any individual collection between "shards". Each shard is one replica set (group of servers/mongod instances that have the same data cloned across them) or it is a single mongod instance. You can learn about how to enable sharding on a database (within a running mongos isntance) and shard a collection. 
<a href="http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/">
http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/
</a>

Below is a list of steps to follow to get a test sharded database up and running on your machine:

