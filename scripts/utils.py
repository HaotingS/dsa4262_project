import json
import pandas as pd
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

    mean_df = df.groupby(by=['transcript_id', 'transcript_position', 'nucleotides']).mean().reset_index()

    min_df = df.groupby(by=['transcript_id', 'transcript_position', 'nucleotides']).min().reset_index()
    min_df.columns = ['transcript_id', 'transcript_position', 'nucleotides', '9', '10', '11', '12', '13', '14', '15', '16', '17']

    max_df = df.groupby(by=['transcript_id', 'transcript_position', 'nucleotides']).max().reset_index()
    max_df.columns = ['transcript_id', 'transcript_position', 'nucleotides', '18', '19', '20', '21', '22', '23', '24', '25', '26']

    complete_df = mean_df.merge(min_df).merge(max_df)
    complete_df = complete_df.astype({"transcript_position": "int"})

    feature_names = [str(feature) for feature in range(27)]

    return complete_df, feature_names
