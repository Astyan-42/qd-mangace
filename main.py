#!/bin/python2.7
# -*- coding: utf-8 -*-

import sys

from classes.chapterstobook import chapterstobook
from classes.resize import resize
from classes.zipmobi import zipmobi

if __name__ == '__main__':
    
    if "c" in sys.argv:
        c = chapterstobook()
        c.correctbadnames()
        c.makeallbook()
    
    if "r" in sys.argv:
        r = resize()
        r.allscale()
    
    if "z" in sys.argv:
        z = zipmobi()
        z.zipall()
    
    if len(sys.argv) == 1:
        print "usage python main.py c r z"
        print "c = correct name and create book"
        print "r = resize pages"
        print "z = create the archives for the device"
