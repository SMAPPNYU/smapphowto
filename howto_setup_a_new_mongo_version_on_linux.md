# how to setup a new version of mongo on linux

#1 go to this website: [digital ocean mongo tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-14-04)

#2 follow that tutorial.

or

#0 - get rid of old mongo

```sh
sudo apt-get purge mongodb mongodb-clients mongodb-server mongodb-dev
sudo apt-get purge mongodb-10gen
sudo apt-get autoremove
```

#1 - add key listing to apt-get

```sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
```

#2 - make a list file

```sh
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
```

#3 - update your package registry

```sh
sudo apt-get update
```

#4 - install new mongodb

```sh
sudo apt-get install -y mongodb-org
```