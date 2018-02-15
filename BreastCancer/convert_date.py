#!/usr/bin/python3

import gzip
from datetime import datetime

# in_gz_file = "../example_csvs/test.csv.gz"
# out_gz_file = "../example_csvs/converted_test.csv.gz"
in_gz_file = "/scratch/jli458/BIGTENSORS/BreastCancer/merged3.csv.gz"
out_gz_file = "/scratch/jli458/BIGTENSORS/BreastCancer/converted_merged3.csv.gz"

with gzip.open(out_gz_file, 'wb') as fo:
	with gzip.open(in_gz_file, 'rb') as fi:
		for line in fi:
			# print(line.decode('utf8'))
			words = line.decode('utf8').split(",")
			if words[0] != "post_thread_id":
				try:
					tmp_time = datetime.strptime(words[3], "%Y-%m-%d %H:%M:%S")
					words[3] = str(tmp_time.timestamp())
					out_str = ",".join(words)
					print(line.decode('utf8'))
					fo.write(out_str.encode())
				except ValueError:
					fo.write(line)
					# print("float numbers for dates.")
			else:
				fo.write(line)			
		
