#0 - export the crontab into a file

export a crontab: 
crontab -l > crontab.bak

[how to do this](http://stackoverflow.com/questions/15767834/how-to-export-crontab-to-a-file)

#1 - put the oauth folder, filter_criteria folder, and crontab file into a tar file 

```sh
tar cvfz collector_data.tar.gz crontab.bak oauth/ filter_criteria/ 
```

[tar tutorial] (https://blog.udemy.com/tar-command-in-linux/)

[tar ref](http://linuxcommand.org/man_pages/tar1.html)

#3 - scp that to the new collector machine

lg into the new collector box and run:
```sh
scp USER@SERVER:/path/to/file
```

#4 - untar the tar file

```sh
tar xvzf collector_data.tar.gz
```

#5 - move oauth and filter_critera to ~

```sh
mv collector_data/oauth ~/oauth
mv collector_data/filter_criteria ~/filter_criteria
```

#6 - import the crontab

```sh
crontab crontab.bak
```

#7 start a tunnel

use [hades_rotating_tunnel.sh](https://github.com/SMAPPNYU/smapputilities#hades_rotating_tunnelsh)
