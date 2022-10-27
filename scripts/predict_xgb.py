import argparse
import json
import numpy as np
import pandas as pd
import os
from sklearn import preprocessing
from xgboost import XGBClassifier 


ap = argparse.ArgumentParser(description="This script will apply your model on new data and return the m6A predictions.")
ap.add_argument("-d", "--data", type=str, help="direct RNA-Seq data, processed by m6Anet (.json)", required=True)
ap.add_argument("-m", "--model", type=str, help="pre-trained model from training script", required=True)
ap.add_argument("-s", "--save_path", type=str, help="path to save predictions (.csv)", required=True)
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
    
# drop duplicates
df.drop_duplicates(keep='first', inplace=True, ignore_index=True)

# groupby and agg using mean 
df = df.groupby(by=['transcript_id', 'transcript_position', 'nucleotides']).mean(numeric_only=True)
df.reset_index(inplace=True)

# save original `transcript_position`
df['transcript_position0'] = df['transcript_position']
df = df.astype({'transcript_position0': 'str'})

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
Xte = df[['transcript_position', '0', '1', '2', '3', '4', '5', '6', '7', '8'] + list(tmp.columns)]

print("[INFO] Loading model...")
model = XGBClassifier()
model.load_model(args.model)

print("[INFO] Running inference...")
yhat_probs = model.predict_proba(Xte, iteration_range=(0, model.best_iteration + 1))
yhat = model.predict(Xte, iteration_range=(0, model.best_iteration + 1))
yhat1_probs = yhat_probs[:, 1]
df['score'] = yhat1_probs

print("[INFO] Saving predictions...")
df_res = df[['transcript_id', 'transcript_position0', 'score']].copy()
df_res.rename(columns={"transcript_position0": "transcript_position"}, inplace=True)
df_res.to_csv(args.save_path, index=False)

print("[INFO] Done.")
