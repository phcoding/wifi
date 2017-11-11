# school wifi login tool
+ describ
```
wifi is a simple tool for login/logout school wifi of Hunan University. This tool
 is only surpport the latest wifi login web protocol. The only thing you need to 
do is to input your username and password or set your login word to default for 
simple login.
```
+ usage
```
usage: wifi [-h] [-a ACTION] [-u USERNAME] [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -a ACTION, --action ACTION
                        action to login or logout.
  -u USERNAME, --username USERNAME
                        username to login wifi.
  -p PASSWORD, --password PASSWORD
                        password to login wifi.
```
+ demo
    1. login: `py -3 wifi -a login -u [username] -p [password]`
    2. logout: `py -3 wifi -a logout -u [username] -p [password]`
    3. if you set your username and password to default, you only need to: 
    `py -3 wifi` or `py -3 wifi -a logout`