import argparse
import os
from utils import *

ap = argparse.ArgumentParser(description="Parse RNA Seq JSON data to CSV")
ap.add_argument("-f", "--file", type=str, help="path to JSON data", required=True)
ap.add_argument("-s", "--save_path", type=str, help="path to save CSV output")
args = ap.parse_args()

df = get_data_dataframe(args.file)

print(f"[INFO] Saving data at {args.save_path}...")

if args.save_path:
    df.to_csv(args.save_path, index=False)
else:
    df.to_csv(f"{os.path.splitext(args.file)[0]}.csv", index=False)

print("[INFO] Done.")
