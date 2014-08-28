#!/bin/python2.7
# -*- coding: utf-8 -*-

import os
import Image
import glob
import sys

sys.path[:0] = ['../'] 

import config

class resize:
    
    def init(self):
        pass
    
    def toscale(self, path):
        print "resize "+path
        scan = Image.open(path)
        (w,h) = scan.size
        if h > config.resebook[1]: # we use the height and not the width because of 2 pages scan
            rap = float(h)/float(config.resebook[1])
            h = config.resebook[1]
            w = int(w/rap)
            res = scan.resize((w,h),Image.BICUBIC)
            res.save(path)
        
    
    def dirscale(self, path):
        ls = glob.glob(os.path.join(path,"*"))
        for f in ls:
            if os.path.splitext(f)[1] in config.fileextentions:
                self.toscale(f)
        
    def allscale(self):
        ls = glob.glob(os.path.join(config.dirbook,"*"))
        for path in ls:
            if os.path.isdir(path):
                self.dirscale(path)

#~ 
#~ truc = resize()
#~ truc.test()

