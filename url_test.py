#!/usr/bin/python3

import os
import sys
import time
import datetime
import requests


def status():
    """ Returns the progress of build url """
    tag = os.environ["TRAVIS_TAG"]
    date = datetime.datetime.now().strftime('%Y%m%d')
    url = "https://github.com/xeon-zolt/meilix/releases/download/"+tag+"/meilix-zesty-"+date+"-i386.iso"
    f = open("log", "w+")
    try:
        req = requests.head(url)
        if req.status_code == 200:
            print('Sucess')
        elif req.status_code == 404:
            f.write('ISO is Building\n')
        else:
            print('Unable to reach to server')
    except requests.ConnectionError:
        print('Failed To Connect')
    f.close()


while True:
    status()
    time.sleep(10)
