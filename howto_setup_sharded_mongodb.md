#How to setup a sharded mongodb.

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


##(0) Creating a security key so that servers run securely.

Run these commands in a directory where you want to store your mongodb server keys:

```sh
mkdir keyfiles

cd keyfiles

openssl rand -base64 741 > mongodb-keyfile

chmod 600 mongodb-keyfile
```

##(1) Setting up a replica set (repeat for the #ofshards/#ofreplicasets you will have.

See the docs here: <a href="http://docs.mongodb.org/master/tutorial/deploy-replica-set-for-testing/">http://docs.mongodb.org/master/tutorial/deploy-replica-set-for-testing/</a>

1 - Create data folders for each mongod instance that will run on a replica set.

Run this command to create three folder paths (-p creates missing folders).

```sh
mkdir -p srv/mongodb/rs0-0 srv/mongodb/rs0-1 srv/mongodb/rs0-2
```

2 - Start a TMUX session with:

```sh
tmux
```

3 - Then do ctrl+b then release keyboard then type ". Do this as many times as you need for each mongod instance in the replica set.

4 - Then use ctrl+b then release keyboard then type "o". this will let you jump between the windows in your tmux session.

5 - In each window of the tmux session start a mongod instance with the followin commands:

(first mongod in the replica set first window command)

```sh
mongod --dbpath srv/mongodb/rs0-0 --port 27018 --replSet rs0 --smallfiles --oplogSize 128 -—keyFile keyfiles/mongodb-keyfile
```

(second mongod in the replica set second window command)

```sh
mongod --dbpath srv/mongodb/rs0-1 --port 27019 --replSet rs0 --smallfiles --oplogSize 128 -—keyFile keyfiles/mongodb-keyfile
```

(third mongod in the replica set third window command)

```sh
mongod --dbpath srv/mongodb/rs0-2 --port 27020 --replSet rs0 --smallfiles --oplogSize 128 -—keyFile keyfiles/mongodb-keyfile
```

6 - Then use ctrl+b then release keyboard then type "d". This will detach your session and let it run on its own.

7 - Now log into mongod instance that you want to be the primary node.

```sh
mongo localhost:27018
```

8 - Create the replicaset on the primary node.

```sh
rs.initiate()
```

9 - Add the other two mongod instances running to the replicaset.

```sh
rs.add("localhost:27019")
```

```sh
rs.add("localhost:27020")
```

10 - Repeat 1 to 9 for however many replica sets you may have.

##(2) Setting up the three config servers.

See the docs here: <a href="http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/">http://docs.mongodb.org/master/tutorial/deploy-shard-cluster/</a>

1 - Create separate data folder paths for each config server.

```sh
mkdir -p configdata0/configdb configdata1/configdb configdata2/configdb
```

2 - Start a TMUX session and make three windows inside this session with ctrl+b and ".

```sh
tmux
```

3 - In each windown of the tmux session navigate using ctrl+b and "o" and run:

(first config server)

```sh
mongod --configsvr --dbpath configdata0/configdb/ --port 27024 -—keyFile keyfiles/mongodb-keyfile
```

(second config server)

```sh
mongod --configsvr --dbpath configdata1/configdb/ --port 27025 -—keyFile keyfiles/mongodb-keyfile
```

(third config server)

```sh
mongod --configsvr --dbpath configdata2/configdb/ --port 27026 -—keyFile keyfiles/mongodb-keyfile
```

4 - Then use ctrl+b then release keyboard then type "d". This will detach your session and let it run on its own.

##(3) Start up a mongos instance in a tmux session and make the shard.

1 - Run tmux.

```sh
tmux
```

2 - Start up a mongos instance inside that tmux session.

```sh
mongos —configdb localhost:27023,localhost:27024,localhost:27025 --port 27026
```

3 - Then use ctrl+b then release keyboard then type "d". This will detach your session and let it run on its own.

4 - Log into the mongos instance the way you would log into a mongod.

```sh
mongo localhost:27026
```

5 - Add each replica set as a shard.

```sh
sh.addShard("rs0/localhost:27017,localhost:27018,localhost:27019")
```

6 - Check the status of the sharded cluster to see if all replica sets are properly added as shards.

```sh
sh.addShard("rs0/localhost:27017,localhost:27018,localhost:27019")
```

##(4) Enable sharding on a database and shard a particular collection inside of that database.

1 - Create a collection on a database and enable sharding on the right database.

```sh
use DATABASENAME
db.createCollection("COLLECTIONNAME")
sh.enableSharding("DATABASENAME")
```

2 - Create a hashed index on the a field of your choosing (here I have chosen the "_id" field to make the hashed index).

```sh
db.COLLECTIONNAME.createIndex({_id:"hashed"})
```

3 - Shard the collection on that database.

```sh
sh.shardCollection("shardtest.shardedcollection", {_id: "hashed"})
```

###authors

written by <a href="https://github.com/yvan">Yvan Scher</a>
