#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import argparse
import logging
from datetime import datetime

import schedule

from notifier import Notifier

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_current_time():
    return str(datetime.now())

def do_notify(work=45, rest=5):
    Notifier.notify("You've been working " + str(work) + " minutes! Now take a " + str(rest) + " minutes rest.", "Take a rest!")
    logger.info("Rest: " + get_current_time())
    time.sleep(rest * 60)
    Notifier.notify("Rest is over. Time to work!")
    logger.info("Back: " + get_current_time())
    
def main():
     parser = argparse.ArgumentParser(description='A tiny reminder that will notify you when you need a rest')
     parser.add_argument('-v', '--version', action='version', version='1.0')
     parser.add_argument('-w', '--work', type=int, help='working duration(in minutes)', default=45)
     parser.add_argument('-r', '--rest', type=int, help='rest interval(in minutes)', default=5)
     args = parser.parse_args()
     work = args.work
     rest = args.rest
     schedule.every(work).minutes.do(do_notify, work=work, rest=rest)
     
     logger.info("Start: " + get_current_time())
     while True:
         schedule.run_pending()
         time.sleep(1)
         
if __name__ == '__main__':
    main()
