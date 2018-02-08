#!/bin/bash

csv_path="/scratch/jli458/BIGTENSORS/BreastCancer/"
#csv_path="/scratch/jli458/BIGTENSORS/FROSTT/tensor_parser/BreastCancer/csvs/"

../scripts/build_tensor.py ${csv_path}/merged3.csv.gz breastcancer.tns \
	-f "post_author_id" --type="post_author_id",int \
	-f "post_id" --type="post_id",int \
	-f "post_time" --type="post_time",float

# Failed for tar.gz now
# ../scripts/build_tensor.py csvs.tar.gz out.tns \
# 	-f "post_author_id" --type="post_author_id",int \
# 	-f "post_id" --type="post_id",int \
# 	-f "post_time" --type="post_time",float
