# browser-resolution-collector
To collect most common browser size for most computer. 
Since we won't work on so much time of solving problems for different resolution of browser, 
we will collect the most common browser's resolution by using this.

## How to deploy
1. You should have a python 2 environment, I developed it with python 2.7.14
2. You should have these libraries: sqlite3, flask, Tornado. sqlite3 should be in python standard library,
which means you are most likely already having it, flask and Tornado can be installed via pip.
`pip install flask`+`pip install Tornado`
3. Create a database (.db file) in src, following the code in data.sql.
4. Open the "main.py", change the port you want in the last few lines of codes here
`http_server.listen(5000)`
5. Run main.py
