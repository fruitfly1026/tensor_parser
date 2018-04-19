#!/bin/bash

csv_path="/scratch/jli458/BIGTENSORS/BreastCancer/converted"
#csv_path="/scratch/jli458/BIGTENSORS/FROSTT/tensor_parser/BreastCancer/csvs/"

../scripts/build_tensor.py ${csv_path}/shrinked.csv.gz breastcancer.tns \
	-f "post_author_id" --type="post_author_id",int \
	-f "post_thread_id" --type="post_thread_id",int \
	-f "post_time" --type="post_time",int \
	--merge count

# -f "post_id" --type="post_id",int \

# Failed for tar.gz now
# ../scripts/build_tensor.py csvs.tar.gz out.tns \
# 	-f "post_author_id" --type="post_author_id",int \
# 	-f "post_id" --type="post_id",int \
# 	-f "post_time" --type="post_time",float
