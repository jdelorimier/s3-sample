import smart_open
from pathlib import Path
import os

def generate_outpath(in_path,out_path=None):
    stem = Path(in_path).stem
    ext = Path(in_path).suffix

    # make directory if does not exist
    directory_path = os.path.split(out_path)[0]
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    if out_path is None:
        return f"{stem}_sample{ext}"
    else: 
        return out_path