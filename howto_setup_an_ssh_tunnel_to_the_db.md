how to setup an ssh tunnel to the database

###1 - get an HPC account

links to get nyu HPC access:
[https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account](https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account)

[https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ](https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ)

###2 - get your HPC account approved for access to the hades database cluster

email the smapp_programmer-group@nyu.edu and clearly identify yourself by providing your nyu netid and position in the lab and request "hades database access"

we will send all requests for authorization in a timely manner to our peers at nyu hpc.

###3 - get the code

- clone the [smapputil](https://github.com/SMAPPNYU/smapputil) repository or just download it

- make sure you have python installed with the right dependencies

you can install anaconda python here:

http://repo.continuum.io/archive/Anaconda3-4.0.0-MacOSX-x86_64.pkg

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
python py/ssh_tunnel/ssh_tunnel.py -lo hpc.nyu.edu -u HPC_LOGIN_USERNAME -p HPC_LOGIN_PASSWORD -rh REMOTE_HOST -rp 27017 -lp 27017
```