# Python Scripting Project Template (Using Pip)
This repo contains a structured template to work on any Python scripting project, using Pip as its virtual environment manager. 

&nbsp;

<div align="center">
  <img alt="github-badge" src="https://img.shields.io/badge/github-template-blue?logo=github">
  <img alt="lang-badge" src="https://img.shields.io/badge/lang-en-green">
  <img alt="py-badge" src="https://img.shields.io/badge/python-3.12-blue?logo=python">
</div>

&nbsp;

## Project _Intended_ Structure
```
├── .env                    # (TO BE CREATED LOCALLY) Environment secret attributes, NEVER PUSH TO GIT
├── .gitignore              # Ignored files to not be tracked by Git, .env as an example
├── LICENSE                 # License file, MIT by default- change as needed
├── README.md               # Description and/or info about the repo
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

&nbsp;

## Requirements

As this is a Pip template, the workflow to follow will use:

1. Create and configure the virtual environment:

```
python -m venv <NAME_OF_ENVIRONMENT>          # create virtual environment
source <NAME_OF_ENVIRONMENT>/bin/activate     # activate the environment (Linux/WSL - Bash)
<NAME_OF_ENVIRONMENT>\Scripts\activate        # activate the environment (Windows - CMD/Shell)
pip install -r requirements.txt               # install dependencies
pip freeze > requirements.txt                 # 'freeze' your current dependencies into the requirements file
```

2. Run 'main.py':

```
python3 src/main.py                           # If working from root

### if the output is something similar to 'Hello! Today is <DATE> and you are working on the root of <FOLDER>.', it is working as intended.
```

3. Delete and re-configure the files/metadata needed and start working in your project!

&nbsp;

## Disclaimer

**This README serves purpose only as an example of how the template works. It SHOULD be replaced and or re-written specifically with the context of your own project.**