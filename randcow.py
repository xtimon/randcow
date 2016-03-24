#!/usr/bin/env python3
# coding:utf-8

import os
import random
import subprocess
import feedparser

cows_path = '/usr/share/cowsay/cows/'
rss_feed = 'http://bash.im/rss/'

cows_list = os.listdir(cows_path)
feed = feedparser.parse(rss_feed)
cow = random.choice(cows_list)
msg = random.choice(feed.entries).description
subprocess.call("cowsay -f {0} \"{1}\"".format(cow, msg), shell=True)
