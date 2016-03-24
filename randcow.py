#!/usr/bin/env python3
# coding:utf-8

import os
import random
import subprocess
import feedparser

# Specify here the directory of your cowfiles (This is default folder for Ubuntu)

cows_path = '/usr/share/cowsay/cows/'

# And here you can specify rss feed which cowsay tells you

rss_feed = 'http://bash.im/rss/'

cows_list = os.listdir(cows_path)
feed = feedparser.parse(rss_feed)
cow = random.choice(cows_list)
if feed.entries:
    msg = random.choice(feed.entries).description
    if msg[0] == '-':
        msg = ' ' + msg
    subprocess.call("cowsay -f {0} '{1}'".format(cow, msg), shell=True)
