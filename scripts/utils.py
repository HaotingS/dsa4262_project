import json
import numpy as np
import pandas as pd
from sklearn import preprocessing
from tqdm import tqdm

def get_data_dataframe(path):
    instance_lists = []
    num_lines = sum(1 for line in open(path))

    with open(path) as f, tqdm(total=num_lines, desc=f"[INFO] Reading in lines from {path}") as progress_bar:
        for transcript_json in f:
            transcript_dict = json.loads(transcript_json)
            for transcript_id, transcript_pos_dict in transcript_dict.items():
                for transcript_pos, nucleotides_dict in transcript_pos_dict.items():
                    for nucleotides, data in nucleotides_dict.items():
                        for row in data:
                            instance_lists.append([transcript_id, transcript_pos, nucleotides] + row)
            progress_bar.update(1)

    print("[INFO] Converting lines into a dataframe...")

    df = pd.DataFrame(instance_lists, columns=["transcript_id", "transcript_position", "nucleotides", "0", "1", "2", "3", "4", "5", "6", "7", "8"])
    df = df.astype({"transcript_position": "int"})

    return df

def process_data_dataframe(df):
    print("[INFO] Preparing features...")

    # Group by and find mean for each group
    df = df.groupby(by=["transcript_id", "str_transcript_position" if "str_transcript_position" in df.columns else "transcript_position", "nucleotides"]).mean(numeric_only=True)
    df.reset_index(inplace=True)

    # Scale numerical variables
    num_vars = df.select_dtypes(include=np.number).columns
    scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    df[num_vars]= scaler.fit_transform(df[num_vars])

    # Split `nucleotides` into characters and make it into indicator variables
    nucleotides_df = df["nucleotides"].str.split(pat="", expand=True)
    nucleotides_df.drop(columns=[nucleotides_df.columns[0], nucleotides_df.columns[-1]], inplace=True)
    nucleotides_df = nucleotides_df.add_prefix("p")
    nucleotides_df = pd.get_dummies(nucleotides_df)
    df = pd.concat([df, nucleotides_df], axis=1)

    return df, nucleotides_df.columns
