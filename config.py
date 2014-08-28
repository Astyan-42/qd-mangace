#!/bin/python2.7
# -*- coding: utf-8 -*-

import os

""" directory where chapter are """
dirchapter = os.path.join("/","path","to","dirchapter")
""" directory where book are and should be create """
dirbook = os.path.join("/","path","to","dirbook")
""" directory where create the zip/mobi files"""
dirzip = os.path.join("/","path","to","dirzip")

""" width and hight of the device """
resebook = (600, 800)

""" type of images in book/chapter """
fileextentions = [".jpg",".JPG",".png",".jpeg"]

""" book to create (nameofbook,(numberofthirstchapter,numberoflastchapter)) """
tomes = [ (20,(171,179)), (21,(180,188)), 
(23,(198,206)), (26,(225,233)), (27,(234,240)) ]  

""" book in the book directory with page with interger name but where 
the display is bad (for exemple with 1.jpg ... 100.jpg and not 001.jpg ... 100.jpg) """
badnames = ["6","7","8","9","10","11","12","13","14","15","16",
"17","18","19"]
