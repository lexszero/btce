#!/usr/bin/python
import sys
import math
import btce
from time import strftime, localtime

nbuckets=20
norm=80

pair = sys.argv[1]
ticker = btce.ticker(pair)

print "Curency pair:", pair
for param in ['sell', 'buy', 'last', 'low', 'high']:
	print "\t", param, ticker[param]

depth = btce.depth(pair)

for type in ['bids', 'asks']:
	d = depth[type]
	rates = map(lambda x: x[0], d)
	rate_min = min(rates)
	rate_max = max(rates)
	rate_delta = rate_max - rate_min
	print type

	buckets = [0 for x in range(nbuckets)]
	for x in map(lambda x: [int((x[0] - rate_min) / rate_delta * (nbuckets - 1)), x[1]], d):
		buckets[x[0]] = buckets[x[0]] + x[1]
	bucket_max = max(buckets)
	buckets = map(lambda x: (x / bucket_max) * norm, buckets)
	
	print "min"
	for bucket_num in range(nbuckets):
		print "%10.3f %10.3f" % ((rate_min + (rate_delta / nbuckets) * bucket_num), buckets[bucket_num]), "*" * int(buckets[bucket_num])
	print rate_max
	print "max"
	print
