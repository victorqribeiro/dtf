#!/usr/bin/env python -W ignore

import os
import glob
import argparse
import numpy as np
from PIL import Image


def distance(x1,x2):
  s = 0.0
  for i in range(len(x1)):
    s += np.sqrt((float(x1[i]) - float(x2[i])) ** 2)
  return s


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True, help="path to image folder")

args = vars(ap.parse_args())

types = ('*.pdf', '*.PDF')

paths = []

folder = args["folder"]

if not folder.endswith("/") :
	folder+="/"
	
for files in types :
	paths.extend(sorted(glob.glob(folder+files)))

tmpfolder = folder+"tmp/"
try :
	os.mkdir(tmpfolder)
except :
	pass

for f in paths :
	os.system( "convert -thumbnail x150 -background white -alpha remove "+f+" "+tmpfolder+f.split('/')[-1][:-4]+".png 2> /dev/null" )


paths = []	
paths.extend(sorted(glob.glob(tmpfolder+"*.png")))

img_addr = {}
for i in paths :
	img_addr[i] = np.array( Image.open(i) ).reshape(-1)

keys = img_addr.keys()

for i in range(0, len(keys) ):
	for j in range(i+1, len(keys) ):
		print( keys[i].split('/')[-1], keys[j].split('/')[-1], distance( img_addr[ keys[i] ], img_addr[ keys[j] ] ) )

os.system("rm -rfd "+	tmpfolder)
