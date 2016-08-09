#1- logging in

you need to log into hpc to run programs there.

the easiest way is to run:

`ssh YOUR_NET_ID@hpc.nyu.edu` you should then see a banner warning message 'UNAUTHORIZED PERSONS ........ DO NOT PROCEED' and a prompt `[YOUR_NET_ID@hpc ~]$` at the prompt tell hpc that you want to go into mercer `ssh YOUR_NET_ID@mercer.es.its.nyu.edu`. your nyu password is used for both logins. once you are on mercer you are actually on hpc.

#2- installing software you need or code you need

check that python is installed `which python`

check that somewhere in the output of that command you see `miniconda` or `anaconda`

if not [install anaconda python: fro linux](https://docs.continuum.io/anaconda/install#linux-install): 
`curl -O http://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh`

`bash ~/Downloads/Anaconda3-4.0.0-Linux-x86_64.sh`

make sure to accept (type 'yes') the option to append anaconda to the path if you accidentally say no do after installation is over:

`export PATH="/home/YOUR_NET_ID/anaconda/bin:$PATH"`

to get the latest smapp tools / code use git and pip (if not installed do `sudo apt-get install git`):

`git clone https://github.com/SMAPPNYU/smapputil.git`

`pip install pysmap --upgrade`

`pip install smappdragon --upgrade`

if it's an individual script you need you'll need to use a program called 'scp' to copy it over.

on your computer locally create a tunnel definition: 

open `~/.ssh/config`
add this to the file:
```
Host hpctunnel
   HostName hpc.nyu.edu
   ForwardX11 yes
   LocalForward 8023 mercer.es.its.nyu.edu:22
   User YOUR_NET_ID

Host mercer
  HostName localhost
  Port 8023
  ForwardX11 yes
  User YOUR_NET_ID
```
open a new terminal tab locally (just open a tab make sure its not logged into hpc, just your regular computer's command prompt)
run `ssh hpctunnel` in the new tab, you may need to enter a password
download the file with hpc run this in et another terminal tab:

`scp mercer:/path/on/your/computer/where/the/file/is /path/on/mercer/where/you/want/the/file`

i.e. scp mercer:~/smapp_stuff/blabla.txt ~/smapp_stuff_local/

#3- running a 'job' 

a job is just a program, script, or process that you decide to run. its any program you submit to run qith qsub. on hpc you cant just run your program as this doesnt actually tap into hpc's vast resources. you need to run you program as a job so it can be sent to the hpc supercomputer to be run. everything should be run as a job.

to run a job you will need to use qsub:

the first way to run programs is whats called 'interactive mode' this is a script that when you run it will almost seamlessly replace your current terminal session on hpc with a new interactive session with access to hpc resources. in this new interactive session you can run jobs (programs, scripts, processes) at will, to run an interactive job session:

`qsub -I interactive.pbs` (if you need the interactive.pbs file email a programmer)

to run a job on hpcs cluster non interactively (to submit the job for hpc to run) you can use the simple_launch_n_jobs.py script:

`~/anaconda/bin/python ~/Sandbox/cluster/simple_launch_n_jobs.py -c '~/anaconda/bin/python ~/Projects/data-reports/2015_6_19-ArabEvents-ISIS/get_data_for_split.py -i /scratch/smapp/arab_events_all_6_19/ArabEvents___tweets_18.bson  -o /scratch/smapp/arabevents-isis-data-report'`

-c is the command to be executed, in this case a python script located on the hpc filesystem at the path `~/Projects/data-reports/2015_6_19-ArabEvents-ISIS/get_data_for_split.p` exectued by python located at path `~/anaconda/bin/python`
-i gives input file for this particular script (some commands would not have one, this particular python script takes in a bson file)
-o shows where to put the output file 

#4- dealing with data on hpc

to see the datasets that are archived run:

`ls -lah /archive/smapp/db_archives/`

to get a copy of the data unzipped directly into scratch of an archive run the 'tar' command as a job either interactively or submitted, unzipping can take a long time:

`tar -xzvf NAME_OF_DATASET.tar.gz -C /scratch/smapp/`

DO NOT RUN ANYTHING OTHER THAN THESE TWO COMMANDS ON THE DATA HERE:

`ls` command
`tar xzvf` 

if you think you need to do something else you must ask a programmer to help you, or to copy data to /scratch/smapp. this is a live archive and doing things in here as an inexperienced command line user can cause people's research data to be lost.

if there is an issue or error in copying, unzipping or any other operation, email a programmer immediately with the output of your command up to the point it failed.

#5- moving data to your computer

setup tunnel stuff as in section 2:

open `~/.ssh/config`
add this to the file:
```
Host hpctunnel
   HostName hpc.nyu.edu
   ForwardX11 yes
   LocalForward 8023 mercer.es.its.nyu.edu:22
   User YOUR_NET_ID

Host mercer
  HostName localhost
  Port 8023
  ForwardX11 yes
  User YOUR_NET_ID
```
open a new terminal tab locally (just open a tab make sure its not logged into hpc, just your regular computer's command prompt)
run `ssh hpctunnel` in the new tab, you may need to enter a password

`scp mercer:/path/on/mercer/where/the/file/is /path/on/your/computer/where/you/want/the/file`

i.e. scp mercer:~/smapp_stuff/blabla.txt ~/smapp_stuff_local/

resources:

[nyu hpc wiki](https://wikis.nyu.edu/display/NYUHPC/High+Performance+Computing+at+NYU)

[here another guide to working on hpc](https://github.com/SMAPPNYU/smapphowto/blob/master/howto_setup_cluster_software.md)
