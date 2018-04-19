1. If too many files, first do `merge_csvs.py`
2. Use `convert_date.py` to unify time format to seconds
3. Use `shrink_records.py` to get rid of duplicated items because of many words in a single post
4. remove the first line of csv.gz files except the first one.
4. `cat xx >> shrinked.csv.gz`
5. Run `time_gap.py` to get the time period
6. Run `run_gz.sh` to generate a tensor and its mapping files


<!-- This data is only used for research purpose, with permission from Breastcancer.org. You can only download this data for your personal use and non-commercial purpose. Refer to [Breastcancer.org](http://www.breastcancer.org/about_us/bco_commitment/legal_terms) for redistribution policy. -->