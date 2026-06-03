# Python Scripting Project Template (Using Pip)
This repo contains a structured template to work on any Python scripting project, using Pip as its virtual environment manager. 

&nbsp;

<div align="center">
  <img alt="lang-badge" src="https://img.shields.io/badge/lang-en-blue">
  <img alt="py-badge" src="https://img.shields.io/badge/python-3.12-blue?logo=python">
</div>

&nbsp;

## Project Structure
```
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── data/
├── requirements.txt
├── src/
│   ├── main.py
│   └── project/
│       ├── __init__.py
│       ├── config.py
│       └── utils.py
└── tests/
    └── test_main.py
```

## Requirements
WIP!
```
python -m venv .venv                   # crea entorno virtual
source .venv/bin/activate              # actívalo (Windows: .venv\Scripts\activate)
pip install -r requirements-dev.txt    # instala dependencias
```