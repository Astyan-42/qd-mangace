#!/bin/python2.7
# -*- coding: utf-8 -*-

import os
import shutil
import glob
import sys

sys.path[:0] = ['../'] 

import config

class chapterstobook:
    
    def init(self):
        pass
    
    def createbook(self, x):
        os.mkdir(os.path.join(config.dirbook, str(x)))
        
    def createname(self, x, ext):
        try :
            x = int(x)
        except :
            try :
                x = int(x.split("-")[0])
            except :
                x = int(x.split(" ")[0])
        y = str(x)
        if x < 10:
            name = "00"+y+ext
        elif x < 100:
            name = "0"+y+ext
        else:
            name = y+ext
        return name
    
    def copybook(self, bchapter, echapter, book):
        i = 0
        for j in range(bchapter,echapter+1):
            files = glob.glob(os.path.join(config.dirchapter,str(j),"*"))
            files.sort()
            for f in files:
                extention = os.path.splitext(f)[1]
                if os.path.splitext(f)[1] in config.fileextentions:
                    shutil.copyfile(f, os.path.join(config.dirbook,str(book),self.createname(i,extention)))
                    i = i + 1
    
    def correctbadnames(self):
        print "Correction of names"
        for book in config.badnames:
            files = glob.glob(os.path.join(config.dirbook,str(book),"*"))
            for f in files:
                (name, extention) = os.path.splitext(f)
                name = name.split("/")[-1]
                if extention in config.fileextentions:
                    newname = self.createname(name,extention)
                    os.rename(f, os.path.join(config.dirbook,str(book),newname))
    
    def makeallbook(self):
        for (i,(j,k)) in config.tomes:
            print "Creating the "+str(i)+"th book"
            try:
                self.createbook(i)
            except:
                pass
            try:
                self.copybook(j,k,i)
            except:
                pass
    

#~ truc = chapterstobook()
#~ truc.correctbadnames()
#~ truc.makeallbook()
#~ truc.copybook(171, 180, 20)


