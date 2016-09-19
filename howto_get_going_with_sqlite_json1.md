how to get going with sqlite and json1
=========================================

1 - install standard sqlite, make sure your sqlite is at least version 3.9.0:

docs on loading ext:http://sqlite.org/loadext.html
example of compiling loadable fts5: http://charlesleifer.com/blog/building-the-sqlite-fts5-search-extension/

2 - compile your own json1 library or download/use smapp’s json1 library

go to download page:http://sqlite.org/download.html:

```sh
curl -O http://sqlite.org/2016/sqlite-src-3140100.zip 
# (swap '3140100' with latest version from downloads page)

unzip sqlite-src-3140100.zip
```

mac osx: gcc -g -fPIC -dynamiclib sqlite-src-3140100/ext/misc/json1.c -o json1

windows: cl YourCode.c -link -dll -out:YourCode.dll

*nix (linux, BSD, etc): gcc -g -fPIC -shared YourCode.c -o YourCode.so

note if you are trying to use json1 on hpc, you will need to download or obtain a linx *nix smapp library from a programmer. or ask them to compile one for you.

3 - load the extension using this example:

http://stackoverflow.com/questions/39319280/python-sqlite-json1-load-extension. 

(for sqlite command line shell use '.load json1’) to access library methods documented here: https://www.sqlite.org/json1.html

```python
import sqlite3
conn = sqlite3.connect('testingjson.db')

#load precompiled json1 extension
conn.enable_load_extension(True)
conn.load_extension("./json1")

# create a cursor
c = conn.cursor()

# make a table
# create table NAME_OF_TABLE (NAME_OF_FIELD TYPE_OF_FIELD);
c.execute('create table testtabledos (testfield JSON);')

# Insert a row of data into a table
c.execute("insert into testtabledos (testfield) values (json('{\"json1\": \"works\"}'));")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```