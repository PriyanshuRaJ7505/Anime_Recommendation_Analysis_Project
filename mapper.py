#!/usr/bin/env python
import sys
for line in sys.stdin:
    if "userId" in line:
        continue
    try:
        data = line.strip().split(',')
        anime = data[2]
        rating = float(data[4])
        print("{}\t{}".format(anime, rating))
    except:
        pass

