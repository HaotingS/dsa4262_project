# DSA4262 Project
Project repository for DSA4262 Sense-making Case Analysis Health and Medicine. 

## Content
* [Introduction](#Introduction)
* [Getting started](#Getting-started)
* [Usage](#Usage)
* [Contributing](#Contributing)
* [Authors](#Authors)
* [License](#License)

## Introduction
This project aims to use machine learning to identify m6A RNA modifications from direct RNA-Seq data.

## Getting started
### Prerequisites
* Python 3.8.10
* For Amazon EC2, use instance type **t3.xlarge** & above

Tested on Ubuntu 20.04.

### Configuration
1. Clone the repository.
```bash
git clone https://github.com/HaotingS/dsa4262_project.git
cd dsa4262_project
```
2. Make sure you are on the right branch, `demo`.
```bash
git checkout demo
```
3. Create a folder for storing outputs.
```bash
mkdir outputs
```
4. Install Python packages.
```bash
sudo apt install -y python3-pip
sudo pip install -r requirements.txt
```

### Get dataset
1. Download data.
```bash
wget -O data.tgz https://www.dropbox.com/s/j24g0e4fg7kqj43/data.tgz?dl=1
```
2. Unzip data and remove compressed files.
```bash
tar -xzvf data.tgz data && rm data.tgz
```

## Usage
The scripts below parse, train and predict on the original datasets. They might take a longer time to run. We have provided a sample data `sample_data.json` at the root of the project directory for you to test run first before running on the full dataset.

### Preprocess dataset (optional)
Parse `data.json` into `data.csv`.
```bash
python3 scripts/parse_data.py -f data/data.json -s data/data.csv
```
* `-f data/data.json` specifies the RNA-Seq data.
* `-s data/data.csv` specifies the resulting csv file.

### Train
Train model using `data.json` and `data.info`.
```bash
python3 scripts/train.py -d data/data.json -l data/data.info -s outputs/xgb.model
```
* `-d data/data.json` specifies the RNA-Seq data.
* `-l data/data.info` specifies the labels.
* `-s outputs/xgb.model` specifies the resulting model.

### Predict
Use trained model to predict on `dataset1.json`, `dataset2.json`, `dataset3.json`.
```bash
python3 scripts/predict.py -d data/dataset1.json -m outputs/xgb.model -s outputs/teamgenono_dataset1.csv
python3 scripts/predict.py -d data/dataset2.json -m outputs/xgb.model -s outputs/teamgenono_dataset2.csv
python3 scripts/predict.py -d data/dataset3.json -m outputs/xgb.model -s outputs/teamgenono_dataset3.csv
```
* `-d data/dataset<n>.json` specifies the n-th test dataset.
* `-m outputs/xgb.model` specifies the model to use for prediction.
* `-s outputs/teamgenono_dataset<n>` specifies the n-th prediction output.

## Contributing
1. Fork it!
2. Create your own branch: `git checkout -b my-new-branch`.
3. Make your changes.
   - Comment out what changes are made: `// Changed ArrayList to Array`.
   - Comment out why are they made: `// Saves memory`.
3. Commit your changes: `git commit -am 'added some feature'`.
4. Push to the branch: `git push origin my-new-branch`.
5. Submit a pull request. :smile:

## Authors
* [:octocat: @samtjong23](https://github.com/samtjong23)
* [:octocat: @y33-j3T](https://github.com/y33-j3T)
* [:octocat: @snah321](https://github.com/snah321)
* [:octocat: @HaotingS](https://github.com/HaotingS)
* [:octocat: @kaychiiiii](https://github.com/kaychiiiii)

## License
DSA4262 Project is licensed under the [MIT license](./LICENSE).
