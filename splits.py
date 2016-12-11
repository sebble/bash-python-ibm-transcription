#!/usr/bin/env python

import sys
from math import ceil

h,m,s = sys.argv[1].split(':')
duration = ceil(float(s) + int(m)*60 + int(h)*3600)

length = int(sys.argv[2])
overlap = int(sys.argv[3])

start = 0

while start < duration:
    end = min(duration, start + length)
    print("%d %d" % (start, end))
    start = start + length - overlap

