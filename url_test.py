#!/usr/bin/python3

import os
import sys
import time
import datetime
import requests
import urllib2


def status():
    """ Returns the progress of build url """
    tag = os.environ["TRAVIS_TAG"]
    date = datetime.datetime.now().strftime('%Y%m%d')
    url = "https://github.com/xeon-zolt/meilix/releases/download/"+tag+"/meilix-zesty-"+date+"-i386.iso"
    try:
        req = requests.head(url)
        if req.status_code == 200:
            return 200
        elif req.status_code == 404:
            return 404
        else:
            return 500
    except requests.ConnectionError:
        print('Failed To Connect')
    pass


def status_2():
    """ Returns the progress of build url """
    tag = os.environ["TRAVIS_TAG"]
    date = datetime.datetime.now().strftime('%Y%m%d')
    url = "https://github.com/xeon-zolt/meilix/releases/download/"+tag+"/meilix-zesty-"+date+"-i386.iso"
    try:
        conn = urllib2.urlopen(url)
        code = conn.getcode()
        conn.close()
        return code
    except urllib2.HTTPError as e:
        return e.getcode()
    pass
