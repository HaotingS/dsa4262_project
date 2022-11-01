# DSA4262 Project
Project repository for DSA4262 Sense-making Case Analysis Health and Medicine. 

## Content
- [Introduction](#Introduction)
- [Getting started](#Getting-started)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [Authors](#Authors)
- [License](#License)


## Introduction
This project aims to use machine learning to identify m6A RNA modifications from direct RNA-Seq data.


## Getting started

### Prerequisites
- Python 3.8

Tested on Ubuntu 20.04.

### Configuration
1. Install Python packages
```bash
pip install -r requirements.txt
```

### Get dataset
1. Download data files from [LumiNUS](https://luminus.nus.edu.sg) for DSA4262, AY2022/2023, Semester 1.
  * `data.zip`
  * `data.info`
  * `dataset1.json`
  * `dataset2.json`
  * `dataset3.json`
2. Clone the repository.
```bash
git clone https://github.com/HaotingS/dsa4262_project.git
cd dsa4262_project
```
3. Make a folder `data` to store data files needed for the project.
```bash
mkdir data
mv <path-to-data.zip> data/data.zip
mv <path-to-data.info> data/data.info
mv <path-to-dataset1.json> data/dataset1.json
mv <path-to-dataset2.json> data/dataset2.json
mv <path-to-dataset3.json> data/dataset3.json
unzip data.zip  # outputs data.json
```
4. Make a folder `outputs` to store training and prediction outputs.
```bash
mkdir outputs
```

### Preprocess dataset (optional)
1. Run [`parse_data.py`](scripts/parse_data.py) to parse `data.json` into `data.csv`. `data.csv` is used in some of the notebooks for analysis and modeling.
```bash
python3 scripts/parse_data.py -f data/data.json -s data/data.csv
```


## Usage
The scripts below trains and predicts on the original datasets. They might take a longer time to run. We have provided a sample data `sample_data.json` at the root of the project directory for you to test run first before running on the full dataset.

### Train
```bash
python3 scripts/train_xgb.py -d data/data.json -l data/data.info -s outputs/xgb.model
```
* `-d data/data.json` specifies the RNA-Seq data.
* `-l data/data.info` specifies the labels.
* `-s outputs/xgb.model` specifies the model output.

### Predict
* Predict on `dataset1.json`, `dataset2.json`, `dataset3.json`
```bash
python3 scripts/predict_xgb.py -d data/dataset1.json -m outputs/xgb.model -s outputs/teamgenono_dataset1.csv
python3 scripts/predict_xgb.py -d data/dataset2.json -m outputs/xgb.model -s outputs/teamgenono_dataset2.csv
python3 scripts/predict_xgb.py -d data/dataset3.json -m outputs/xgb.model -s outputs/teamgenono_dataset3.csv
```
* `-d data/dataset<n>.json` specifies the n-th test dataset.
* `-m outputs/xgb.model` specifies the model to use for prediction.
* `-s outputs/teamgenono_dataset<n>` specifies the n-th prediction output.



## Contributing
1. Fork it!
2. Create your own branch: `git checkout -b my-new-branch`.
3. Make your changes.
   - Comment out what changes are made: `// changed ArrayList to array`.
   - Comment out why are they made: `// saves memory`.
3. Commit your changes: `git commit -am 'added some feature'`.
4. Push to the branch: `git push origin my-new-branch`.
5. Submit a pull request. :smile:


## Authors


## License
DSA4262 Project is licensed under the [MIT license](./LICENSE).
