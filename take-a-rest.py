#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import argparse
import schedule

from notifier import Notifier


def do_notify(work=45, rest=5):
    Notifier.notify("You've been working " + str(work) + " minutes! Now take a " + str(rest) + " minutes rest.", "Take a rest!")
    time.sleep(rest * 60)
    
def main():
     parser = argparse.ArgumentParser(description='A tiny reminder that will notify you when you need a rest')
     parser.add_argument('-v', '--version', action='version', version='1.0')
     parser.add_argument('-w', '--work', type=int, help='working duration(in minutes)', default=45)
     parser.add_argument('-r', '--rest', type=int, help='rest interval(in minutes)', default=5)
     args = parser.parse_args()
     work = args.work
     rest = args.rest
     schedule.every(work).minutes.do(do_notify, work=work, rest=rest)
     
     while True:
         schedule.run_pending()
         time.sleep(1)
         
if __name__ == '__main__':
    main()