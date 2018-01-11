#!/bin/bash

../scripts/build_tensor.py csvs/1102.csv.gz csvs/1103.csv.gz out.tns \
	-f "post_author_id" --type="post_author_id",int \
	-f "post_id" --type="post_id",int \
	-f "post_time" --type="post_time",float