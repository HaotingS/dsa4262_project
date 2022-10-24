import argparse
import pandas as pd
import json
import os

ap = argparse.ArgumentParser(description="Parse RNA Seq JSON data to CSV")
ap.add_argument("-f", "--file", type=str, help="path to JSON data", required=True)
ap.add_argument("-s", "--save_path", type=str, help="path to save CSV output")
args = ap.parse_args()

temp_lst = list()
with open(args.file, 'rb') as f:
    for line in f:
        temp1 = json.loads(line)
        for gene_id, reads in temp1.items():
            for read_pos, trans_vals in reads.items():
                for trans_id, vals in trans_vals.items():
                    for val in vals:
                        row1 = (gene_id, read_pos, trans_id, val)
                        temp_lst.append(row1)

df = pd.DataFrame(temp_lst, columns=['transcript_id', 'transcript_position', 'nucleotides', 'val'])
temp = pd.DataFrame(df.val.tolist(), index=df.index,  columns=['0', '1', '2', '3', '4', '5', '6', '7', '8'])

df = pd.concat([df, temp], axis=1)
df.drop(columns=['val'], inplace=True)

if args.save_path:
    df.to_csv(args.save_path, index=False)
else:
    df.to_csv(f"{os.path.splitext(args.file)[0]}.csv", index=False)