# Guide

1. [Setup Repository](#setup-repository)
2. [Setup Python](#setup-python)
3. [Run Baseline](#run-baseline)

## Setup Repository

1.1 Clone repository
```bash
git clone https://github.com/BaguetteJet/CS4928-Project
```

1.2 Clone submodule `baseline`
```bash
git submodule update --init --recursive
```

1.3 Extract `baseline/datasets.zip` into root directory `datasets/`
```bash
# Linux/MacOS
unzip -o baseline/datasets.zip

# Windows (PowerShell)
Expand-Archive -Path baseline\datasets.zip -DestinationPath . -Force
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

2.3 Install Git hooks
```bash
pip install pre-commit
pre-commit install --config .config/pre-commit.yaml
```

```bash
pre-commit run --all-files --config .config/pre-commit.yaml
```
## Run Baseline

Run the baseline notebook to answer [Research Question 1](/docs/Research_Questions.md#rq1)

[`baseline/RoBERTa_knn.ipynb`](baseline/RoBERTa_knn.ipynb)