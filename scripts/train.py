import os
import argparse
from collections import Counter
from math import ceil
from xgboost import XGBClassifier
from utils import *

ap = argparse.ArgumentParser(description="This script will use training data to learn a model. The model can be written to a file in any format.")
ap.add_argument("-d", "--data", type=str, help="direct RNA-Seq data, processed by m6Anet (.json)", required=True)
ap.add_argument("-l", "--labels", type=str, help="m6A labels (.csv)", required=True)
ap.add_argument("-s", "--save_path", type=str, help="path to save trained model (any format)", required=True)
args = ap.parse_args()

# Read in data json and convert it into a dataframe
df = get_data_dataframe(args.data)

# Process the dataframe to generate new features
df, features = process_data_dataframe(df)

# Merge with labels
df_info = pd.read_csv(args.labels)
df = df.merge(df_info, how="left", on=["transcript_id", "transcript_position"])

# Select training features and labels
Xtr = df[features]
ytr = df["label"]

print("[INFO] Initializing model...")
# XGBoost
# Count examples in each class
count_label = Counter(ytr)

# Estimate scale_pos_weight value
# If the dataset is missing any classes, we use the label ratio from data.json as the default value
class_ratio = count_label[0] / count_label[1] if len(count_label) == 2 else 21.25351598173516

# Define model
model = XGBClassifier(
    objective="binary:logistic",
    scale_pos_weight = ceil(class_ratio),
    max_delta_step=1,
    seed=42
)

print("[INFO] Fitting model...")
model.fit(Xtr, ytr)

save_path = args.save_path if args.save_path else os.path.join(f"{os.path.splitext(args.data)[0]}.model")

print(f"[INFO] Saving model at {save_path}...")
model.save_model(save_path)

print("[INFO] Done.")
