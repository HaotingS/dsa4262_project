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
unzip data.zip  # outputs data.json
```

### Preprocess dataset (optional)
1. Run [`parse_data.py`](scripts/parse_data.py) to parse `data.json` into `data.csv`. `data.csv` is used in some of the notebooks for analysis and modeling.
```bash
python3 scripts/parse_data.py -f data/data.json -s data/data.csv
```


## Usage
### Train
```
python train.py
```

### Predict
```
python test.py
```
- `some parameter` explaination bla bla bla


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
