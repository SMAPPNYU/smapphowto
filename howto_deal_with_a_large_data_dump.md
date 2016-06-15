how to deal with a large data dump

so we've given you a large dataset and you need a place to keep it. here are your options (i would recommend a combination of the below as no single solution will insulate you from failure):

###1 - compress the data (if it isnt already)

if a file has any of these extensions it's already compressed:

.tar
.tar.gz
.zip
.bz2

this will save you space and can be used to put datasets with lots of files or folders into one portable file.

we recommend creating a default .tar.gz file like so:

```
tar -cvzf NAME_OF_NEW_COMPRESSED_FILE.tar.gz name_of_inputfile.json name_of_another_inputfile.csv name_of_input_folder/
```

input files can have any extension

list of complete archive formats:
https://en.wikipedia.org/wiki/List_of_archive_formats

###2 - put your data on space allocated for you on NYU HPC 

everyone with an nyu netid and nyu hpc access has 2 Terabytes of space in their archive

links to get nyu HPC access:
[https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account](https://wikis.nyu.edu/display/NYUHPC/Getting+or+renewing+an+HPC+account)

[https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ](https://wikis.nyu.edu/display/NYUHPC/Requesting+an+HPC+account+with+IIQ)

to navigate to your archive log into HPC and type:

`cd /archive/YOUR_NETID`

to see what files are in the archive type:

`ls /archive/YOUR_NETID`

you can use [scp](https://en.wikipedia.org/wiki/Secure_copy) (aka secure copy) to move you data from your computer to HPC:

`scp /path/to/file/on/your/computer YOUR_NETID@mercer.es.its.nyu.edu:/archive/YOUR_NETID/`

or if you are on HPC/mercer

`scp USERNAME_ON_YOUR_COMPUTER@mercer.es.its.nyu.edu:/archive/YOUR_NETID/`

to get `USERNAME_ON_YOUR_COMPUTER` type `whoami`

[usage examples for scp](http://www.hypexr.org/linux_scp_help.php)

if you have any questions contact the smapp_programmer-group@nyu.edu mailing list, identify yourself, and ask a question

###3 - put your data on space provided on google drive for you by nyu

everyone with an nyu netid has unlimited space with Google Drive.

you can access this google drive space by going to this link [http://drive.nyu.edu/](http://drive.nyu.edu/) and logging in with your netid and nyu password.

###4 - put your data on an external hard drive

ask your advisor for a hard drive. if you are unsure about some detail, send an email to smapp_programmer-group@nyu.edu to ask about getting a hard drive.

