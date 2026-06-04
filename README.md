# Python Scripting Project Template (Using Pip)
This repo contains a structured template to work on any Python scripting project, using Pip as its virtual environment manager. 

&nbsp;

<div align="center">
  <img alt="github-badge" src="https://img.shields.io/badge/github-template-blue?logo=github">
  <img alt="lang-badge" src="https://img.shields.io/badge/lang-en-green">
  <img alt="license-badge" src="https://img.shields.io/badge/license-MIT-yellow">
  <img alt="py-badge" src="https://img.shields.io/badge/python-3.12-blue?logo=python">
</div>

&nbsp;

## Project _Intended_ Structure
```
├── .env                    # (TO BE CREATED LOCALLY) Environment secret attributes, NEVER PUSH TO GIT
├── .gitignore              # Ignored files not to be tracked by Git, .env as an example
├── LICENSE                 # License file, MIT by default- change as needed
├── README.md               # You are here!
├── data/                   # (TO BE CREATED LOCALLY) Files processed in/out by the scripts
│   ├── input/              # (TO BE CREATED LOCALLY) Input data for scripting purposes, if applicable
│   └── output/             # (TO BE CREATED LOCALLY) Output data from the scripts, if applicable
├── requirements.txt        # Pip requirements
├── src/                    # All source code, containing the scripts
│   ├── main.py             # Main script to be executed
│   └── project/            # Local package relevant to your project
│       ├── __init__.py     # Importable package indicator
│       ├── config.py       # File that imports the .env attributes into a Python environment
│       └── utils.py        # File containing main classes and/or functions
└── tests/                  # Tests of the different classes, if applicable
    └── test_main.py        # Test of the main class. Only this one is created by default
```

Note that this is the **intended** default structure. Subject to local changes as needed.

## Setup & Usage
 
### 1 — Create and configure the virtual environment
 
```bash
python -m venv <ENV_NAME>                      # Create the virtual environment
source <ENV_NAME>/bin/activate                 # Activate — Linux / WSL (Bash)
<ENV_NAME>\Scripts\activate                    # Activate — Windows (CMD / PowerShell)
 
pip install -r requirements.txt               # Install dependencies
pip freeze > requirements.txt                 # Save current dependencies to requirements file
```
 
### 2 — Run the main script
 
```bash
python3 src/main.py                            # Run from the project root
```
 
> Expected output: `Hello! Today is <DATE> and you are working on the root of <FOLDER>.`
 
### 3 — Make it yours
 
Delete and reconfigure the template files and metadata as needed, and start building your project!
 
---


## Disclaimer

**This README is part of the template and should be replaced. Rewrite it with the context, setup instructions, and details specific to your own project.**