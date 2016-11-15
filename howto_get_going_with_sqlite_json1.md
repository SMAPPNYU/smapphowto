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

mac osx: `gcc -g -fPIC -dynamiclib sqlite-src-3140100/ext/misc/json1.c -o json1`

windows: `cl YourCode.c -link -dll -out:YourCode.dll`

*nix (linux, BSD, etc): `gcc -g -fPIC -shared YourCode.c -o YourCode.so`

note: if you are trying to use json1 on hpc, and successfully manage to compile json1 there please let me know. we've had trouble with it.

3 - load the extension using this example:

http://stackoverflow.com/questions/39319280/python-sqlite-json1-load-extension. 

for sqlite command line shell use '.load json1’

to access library methods documented here: https://www.sqlite.org/json1.html

heres an example of how to search json entries by a field's value: http://stackoverflow.com/questions/27497850/postgres-equivalient-in-sqlite-to-search-json-object with a json field called 'value'

if you could search json field on a table like so:

```
.load json1
CREATE TABLE testtable (id INTEGER, json_field JSON);
# insert data into test table
insert into test_table (id, test_field) values (1, json('{"name":"yvan"}'));
insert into test_table (id, test_field) values (2, json('{"name":"sara"}'));
#select json objects from the json column
select * from testtable where json_extract("json_field", '$.name') is not null;
1|{"name":"yvan"}
2|{"name":"sara"}
3|{"name":"yvan"}
4|{"name:"katherine"}
5|{"name":"thingol"}
6|{"name":"anarion"}
7|{"name":"earendil"}
8|{"name":"metalhead"}
9|{"name":"greenthumb"}
10|{"name":"cactushead"}
11|{"name":"blah"}
# or
select * from testtable where json_extract("json_field", '$.name') = 'yvan';
1|{"name":"yvan"}
3|{"name":"yvan"}
```

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