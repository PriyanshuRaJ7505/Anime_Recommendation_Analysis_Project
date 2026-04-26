#!/usr/bin/env python
import sys
anime = None
total = 0
count = 0
for line in sys.stdin:
    try:
        a, r = line.strip().split('\t')
        r = float(r)
        if a == anime:
            total += r
            count += 1
        else:
            if anime:
                print("{}\t{:.2f}\t{}".format(anime, total/count, count))
            anime = a
            total = r
            count = 1
    except:
        pass
if anime:
    print("{}\t{:.2f}\t{}".format(anime, total/count, count))

