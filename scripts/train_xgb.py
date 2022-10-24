import argparse
import json
import numpy as np
import pandas as pd
import os
from collections import Counter
from math import ceil
from sklearn import preprocessing
from xgboost import XGBClassifier 

ap = argparse.ArgumentParser(description="This script will use training data to learn a model. The model can be written to a file in any format.")
ap.add_argument("-d", "--data", type=str, help="direct RNA-Seq data, processed by m6Anet (.json)", required=True)
ap.add_argument("-l", "--labels", type=str, help="m6A labels (.csv)", required=True)
ap.add_argument("-s", "--save_path", type=str, help="path to save trained model (any format)", required=True)
args = ap.parse_args()


print("[INFO] Preprocessing data...")
temp_lst = list()
with open(args.data, 'rb') as f:
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
df = df.astype({'transcript_position': 'int'})
    
# merge with labels
df_info = pd.read_csv(args.labels)
df = df.merge(df_info, how='left', on=['transcript_id', 'transcript_position'])

# drop duplicates
df.drop_duplicates(keep='first', inplace=True, ignore_index=True)

# groupby and agg using mean 
df = df.groupby(by=['transcript_id', 'transcript_position', 'nucleotides']).mean(numeric_only=True)
df.reset_index(inplace=True)

# scale numerical variables
num_var = df.select_dtypes(include=np.number).columns
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
df[num_var]= scaler.fit_transform(df[num_var])

# seperate `nucleotides`
tmp = df['nucleotides'].str.split(pat="", expand=True)
tmp.drop(columns=[tmp.columns[0], tmp.columns[-1]], inplace=True)
tmp = tmp.add_prefix("p")
tmp = pd.get_dummies(tmp)
df = pd.concat([df, tmp], axis=1)

# prepare features
Xtr = df[['transcript_position', '0', '1', '2', '3', '4', '5', '6', '7', '8'] + list(tmp.columns)]
ytr = df['label']

print("[INFO] Initializing model...")
# XGBoost
# count examples in each class
count_label = Counter(ytr)

# estimate scale_pos_weight value
estimate = count_label[0] / count_label[1]

# define model
model = XGBClassifier(
    objective='binary:logistic',
    scale_pos_weight = ceil(estimate),
    max_delta_step=1,
    seed=42,
    verbosity=1
)

print("[INFO] Fitting model...")
model.fit(Xtr, ytr)

print("[INFO] Saving model...")
# save model
if args.save_path:
    model.save_model(args.save_path)
else:
    model.save_model(os.path.join(f"{os.path.splitext(args.data)[0]}.model"))
    
print("[INFO] Done.")