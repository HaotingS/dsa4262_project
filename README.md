# DSA4262 Project
Project repository for DSA4262 Sense-making Case Analysis Health and Medicine. 

## Content
- [Introduction](#Introduction)
- [Getting started](#Getting-started)
- [Usage](#Usage)
- [Contributors](#Contributors)
- [Contributing](#Contributing)
- [License](#License)


## Introduction
This project aims to use machine learning to identify m6A RNA modifications from direct RNA-Seq data.


## Getting started
### Prerequisites
- Python 3.8

### Dataset and preparation
1. Download data files (`data.zip`, `data.info`) from [LumiNUS](https://luminus.nus.edu.sg).
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
unzip data.zip  # this will give you data.json
```
4. Run [`parse_data.ipynb`](notebooks/parse_data.ipynb) to parse `data.json` into `data.csv`.
 
### Configuration


## Usage
### Train
```
python train.py
```

### Evaluation
```
python test.py
```
- `some parameter` explaination bla bla bla

## Contributors


## Contributing
1. Fork it!
2. Create your own branch: `git checkout -b my-new-branch`.
3. Make your changes.
   - Comment out what changes are made: `// changed ArrayList to array`.
   - Comment out why are they made: `// saves memory`.
3. Commit your changes: `git commit -am 'added some feature'`.
4. Push to the branch: `git push origin my-new-branch`.
5. Submit a pull request. :smile:


## License
DSA4262 Project is licensed under the [MIT license](./LICENSE).