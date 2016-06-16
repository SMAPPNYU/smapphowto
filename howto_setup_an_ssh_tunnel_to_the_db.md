how to setup an ssh tunnel to the database

###1 - get an HPC account

links to get nyu HPC access:
[https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account](https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account)

[https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ](https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ)

###2 - get your HPC account approved for access to the hades database cluster

email the smapp_programmer-group@nyu.edu and clearly identify yourself by providing your nyu netid and position in the lab and request "hades database access"

we will send all requests for authorization in a timely manner to our peers at nyu hpc.

###3 - get the code

clone the [smapputil](https://github.com/SMAPPNYU/smapputil) repository or just download it by using `git clone https://github.com/SMAPPNYU/smapputil.git` or downloading by pressing the green `clone or donwload` button on the gethub pae at the top right.

make sure you have python 3.X installed with the right dependencies. you can install anaconda python here:

http://repo.continuum.io/archive/Anaconda3-4.0.0-MacOSX-x86_64.pkg

or [here if you dont have a mac](https://www.continuum.io/downloads)

then run these commands to install the dependencies:

```
pip install sshtunnel
pip install argparse
```

if you have issues check your installation by typing `which python` you should see something that has the word `anaconda` in it loke so `/Users/jack/anaconda/bin/python` if you dont see something like this you'll need to reinstall anaconda.

if you still have issues email smapp_programmer-group@nyu.edu

###4 - run the tunnel in a terminal window

you can use the smapputil code you just downoaded to run a tunnel. inside smapputil there is  a folder called `py` inside it there is ssh tunnel code

run it like so

```
python py/ssh_tunnel/ssh_tunnel.py -lo hpc.nyu.edu -u HPC_LOGIN_USERNAME -p HPC_LOGIN_PASSWORD -rh hades0.es.its.nyu.edu -rp 27017 -lp 49999
```

###5 - now use the tunnel

you can now access the database at localhost port 49999

using smappdragon this will look like this:
```
from smappdragon import MongoCollection

collection = MongoCollection('localhost', 49999, 'DB_USER_NAME', 'DB_PASSWORD', 'DB_NAME', 'COLLECTION_NAME')
```

using [pysmap smappcollection](https://github.com/SMAPPNYU/pysmap#smapp_collection) it looks like this:
```
from pysmap import SmappCollection

collection = SmappCollection('mongo', 'localhost', 49999, 'DB_USER_NAME', 'DB_PASSWORD', 'DB_NAME', 'COLLECTION_NAME')
```