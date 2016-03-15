#0 - all files should be .tar.gz on a smapp file server. even small files. just tar them gz them, it makes them easier to manage.

`tar cvfz datafile.tar.gz data_file.bson folderofbsons/ data_file_2.bosn etc`

#1 - install and setup nginx

`sudo apt-get install nginx`

#2 - remove nginx default site

`sudo rm /etc/nginx/sites-enabled/default`

#3 - setup the spec for the fileserver

`nano /etc/nginx/sites-available/YOUR_FILESERVER_NAME`

```
server {
  listen 82;
  server_name DOMAIN_OR_IP_FOR_SITE;
  root /home/yvan/YOUR_FILESERVER_NAME;
  autoindex on;
  sendfile on;
  sendfile_max_chunk 1m;
  tcp_nopush on;
}
```

#4 - symlink this spec for it to be available

`sudo ln -s /etc/nginx/sites-available/YOUR_FILESERVER_NAME /etc/nginx/sites-enabled/`

#5 - test nginx and restart it

`sudo nginx -t`

`sudo service nginx restart`

#6 - grab a file

to get a file put `http://DOMAIN_OR_IP_FOR_SITE:82/NAME_OF_FILE.tar.gz`

#7 - to upload files

[use scp](http://linux.die.net/man/1/scp)


resources:

https://www.nginx.com/resources/admin-guide/serving-static-content/

http://nginx.org/en/docs/http/ngx_http_core_module.html

https://www.nginx.com/resources/admin-guide/serving-static-content/