#!/bin/python2.7
# -*- coding: utf-8 -*-

import os
import glob
import zipfile
import sys

sys.path[:0] = ['../'] 

import config

class zipcbz:
    
    def init(self):
        pass
    
    def zipdir(self, path, name):
        print "zip "+os.path.join(path,str(name))
        listoffiles = glob.glob(os.path.join(path,str(name),"*"))
        myzip = zipfile.ZipFile(os.path.join(config.dirzip,str(name)+".zip"), 'w')
        for f in listoffiles:
            fs = f.split("/")
            myzip.write(f, fs[-1])
        myzip.close()
    
    def zipall(self):
        listofbooks = glob.glob(os.path.join(config.dirbook,"*"))
        for book in listofbooks:
            if os.path.isdir(book):
                bk = book.split("/")
                self.zipdir(config.dirbook,bk[-1]) 
                
        
#~ truc = zipmobi()
#~ truc.zipall()
        
