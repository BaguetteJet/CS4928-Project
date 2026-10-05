# Guide

1. [Setup Repository](#setup-repository)
2. [Setup Python](#setup-python)
3. [Run Baseline](#run-baseline)

## Setup Repository

1.1 Clone repository
```bash
git clone https://github.com/BaguetteJet/CS4928-Project
```

1.2 Clone submodule
```bash
git submodule update --init --recursive
```

1.3 Extract `baseline/datasets.zip` into root directory `datasets/`
```bash
# Linux/MacOS
mkdir -p datasets
unzip -o baseline/datasets.zip -d datasets/

# Windows (PowerShell)
New-Item -ItemType Directory -Force datasets
Expand-Archive -Path baseline\datasets.zip -DestinationPath datasets -Force
```

## Setup Python

Requires Python 3.10+

2.1 Create virtual environment and activate
```bash
# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

2.2 Install requirements
```bash
pip install -r requirements.txt
```

## Run Baseline

Run the baseline notebook to answer [Research Question 1](/docs/Research_Questions.md#rq1)

[`baseline/RoBERTa_knn.ipynb`](baseline/RoBERTa_knn.ipynb)