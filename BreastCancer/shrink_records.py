#!/usr/bin/python3

import gzip
from datetime import datetime

# in_gz_file = "../example_data/example_csvs/converted_1103.csv.gz"
# out_gz_file = "../example_data/example_csvs/shrinked_1103.csv.gz"
in_gz_file = "/scratch/jli458/BIGTENSORS/BreastCancer/converted/converted_merged4.csv.gz"
out_gz_file = "/scratch/jli458/BIGTENSORS/BreastCancer/converted/shrinked_merged4.csv.gz"

last_post_thread_id = 0
last_post_author_id = 0
last_post_id = 0
last_post_time = 0.0

with gzip.open(out_gz_file, 'wb') as fo:
	with gzip.open(in_gz_file, 'rb') as fi:
		for line in fi:
			# print(line.decode('utf8'))
			words = line.decode('utf8').split(",")
			if words[0] != "post_thread_id":
				# different words in the same post 
				if words[0] != last_post_thread_id or words[1] != last_post_author_id or words[2] != last_post_id or words[3] != last_post_time:
					last_post_thread_id = words[0]
					last_post_author_id = words[1]
					last_post_id = words[2]
					last_post_time = words[3]
					# Convert seconds to minutes
					# words[3] = str(int(float(words[3]) / 60.0))
					# Convert seconds to hours
					# words[3] = str(int(float(words[3]) / 60.0 / 60.0))
					# Convert seconds to days
					words[3] = str(int(float(words[3]) / 60.0 / 60.0 / 24.0))
					write_out = words[0]+','+words[1]+','+words[2]+','+words[3]+'\n'
					fo.write(write_out.encode('utf8'))
			else:
				write_out = words[0]+','+words[1]+','+words[2]+','+words[3]+'\n'
				fo.write(write_out.encode('utf8'))		
		