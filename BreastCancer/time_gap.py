#!/usr/bin/python3

import gzip
import sys

# in_gz_file = "../example_data/example_csvs/shrinked_1103.csv.gz"
in_gz_file = "/scratch/jli458/BIGTENSORS/BreastCancer/converted/shrinked.csv.gz"

min_time = sys.maxsize
max_time = 0

with gzip.open(in_gz_file, 'rb') as fi:
	for line in fi:
		words = line.decode('utf8').split(",")
		if words[0] != "post_thread_id":
			post_time = int(words[3])
			if min_time > post_time:
				min_time = post_time
			if max_time < post_time:
				max_time = post_time

time_period = max_time - min_time
print('min time (min): '+str(min_time))	
print('max time (min): '+str(max_time))
print('time period (min): '+str(time_period))