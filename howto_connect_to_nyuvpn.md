How to connect to nyu's vpn (vpn.nyu.edu) from the command line in linux or OSX.

On OSX Yosemite 10.5.5 and Ubuntu 14.04.3


Install vpnc and openconnect
===========================

OSX: 

Get homebrew by visting [http://brew.sh](http://brew.sh)

and running

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


```bash
brew install vpnc
```

you may be prompted to run this command when installing vpnc on OSX Yosemite and later, do it then install vpnc via the command above.

```bash
brew install Caskroom/cask/tuntap
```

then run:

```bash
brew install openconnect
```

Linux:

```bash
sudo apt-get install openconnect vpnc
```


Use them to connect
====================

```bash
echo “NYUPWD” | sudo openconnect -u NETID --passwd-on-stdin --authgroup nyu-vpn vpn.nyu.edu
```

OR 
```bash
sudo openconnect --authgroup nyu-vpn vpn.nyu.edu
```

and enter your password and username on the command line.

Note: if you have problems on Linux try running the command with the 
--no-xmlpost flag like so:

```bash
sudo openconnect --no-xmlpost --authgroup nyu-vpn vpn.nyu.edu
```


You can also find instructions at these resources/tutorials:

[http://www.infradead.org/openconnect/manual.html](http://www.infradead.org/openconnect/manual.html)
[https://wiki.archlinux.org/index.php/OpenConnect](https://wiki.archlinux.org/index.php/OpenConnect)
[http://crashcourse.housegordon.org/OpenConnect.html](http://crashcourse.housegordon.org/OpenConnect.html)
[http://askubuntu.com/questions/523407/ubuntu-equivalent-of-the-cisco-anyconnect-vpn-client](http://askubuntu.com/questions/523407/ubuntu-equivalent-of-the-cisco-anyconnect-vpn-client)

authors
=======
[yvan](https://github.com/yvan)


contributor
===========
guiseppe-antonio