import os
import csv
import smart_open
from pathlib import Path
from itertools import islice
from s3_sample.utils import generate_outpath

def sample_csv_head(in_path, out_path,n=10):
    with smart_open.open(in_path) as f:
        reader = csv.reader(f)
        with open(file_out, 'w') as outfile:
            writer = csv.writer(outfile)
            for row in islice(reader, 10):
                writer.writerow(row)
    return None