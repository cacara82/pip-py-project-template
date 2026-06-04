# Python Scripting Project Template (Using Pip)
This repo contains a structured template to work on any Python scripting project, using Pip as its virtual environment manager. 

&nbsp;

<div align="center">
  <img alt="github-badge" src="https://img.shields.io/badge/github-template-blue?logo=github">
  <img alt="lang-badge" src="https://img.shields.io/badge/lang-en-green">
  <img alt="py-badge" src="https://img.shields.io/badge/python-3.12-blue?logo=python">
</div>

&nbsp;

## Project Structure
```
├── .env                    # (TO BE CREATED LOCALLY)  
├── .gitignore              #
├── LICENSE                 #
├── README.md               #
├── data/                   # (TO BE CREATED LOCALLY) Files processed in/out by the scripts
│   ├── input/              # (TO BE CREATED LOCALLY) Input data for scripting purposes, only if necessary
│   └── output/             # (TO BE CREATED LOCALLY) Output data from the scripts, only if necessary
├── requirements.txt        #
├── src/                    #
│   ├── main.py             #
│   └── project/            #
│       ├── __init__.py     #
│       ├── config.py       #
│       └── utils.py        #
└── tests/                  #
    └── test_main.py        #
```

## Requirements
WIP!
```
python -m venv .venv                   # crea entorno virtual
source .venv/bin/activate              # actívalo (Windows: .venv\Scripts\activate)
pip install -r requirements-dev.txt    # instala dependencias
```