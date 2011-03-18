#! /usr/bin/python

import os
import time
import sys

def sort_filename(a, b):
    try:
        a_num = int(a.split('.')[0].split('-')[-1])
    except:
        return -1
    try:
        b_num = int(b.split('.')[0].split('-')[-1])
    except:
        return 1

    if a_num == b_num:
        return 0
    elif a_num < b_num:
        return -1
    else:
        return 1
try:
    directory = sys.argv[1]
except:
    print 'Please specify a directory for this capture session'
    exit()

# Find latest image number
files = os.listdir(directory)

if len(files) == 0:
    count = 1
else:
    files.sort(sort_filename)
    count = files[-1].split('.')[0].split('-')[-1]
    if count == '':
        count = 1
    else:
        count = int(count) + 1

print "Starting image capture from #%d" % count

name = 'screenshot'
delay = 5

while True:
    
    filename = "images/%s-%i.png" % (name, count)
    
    os.system("screencapture -x %s" % filename)
    
    print "Captured screenshot #%i" % count

    count = count + 1

    time.sleep(delay)