# Mighty cowsay tells news

Everybody know cowsay. Great tool, made on Perl. I decided to enlarge it's functionality with rss feed, so you can never be bored openning terminal on local desktop or remote server.

### Installation

Please verify that you have python version 3. If you don't have it, please install firstly.

```sh
$ python3 --version
Python 3.4.3
```
Installation is simple:
```sh
$ git clone https://github.com/xtimon/randcow.git {destination_folder}
$ chmod +x {destination_folder}/randcow.py
```
Then add script in bashrc, so it will be executed everytime you call terminal:
```sh
$ echo "~/{destination_folder}/randcow.py" >> ~/.bashrc
```
### Things you should change
There are two variables you will probably want to change. 
* Default cows_path directory:
```
cows_path = '/usr/share/cowsay/cows/' 
```
* RSS feed link: 
```
rss_feed = 'http://bash.im/rss/'
```
