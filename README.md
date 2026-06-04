# Python Scripting Project Template (Pip)

> A structured, ready-to-use template for Python scripting projects — batteries included, clutter excluded.

<div align="center">

  ![GitHub Template](https://img.shields.io/badge/github-template-181717?logo=github&logoColor=white)
  ![Language](https://img.shields.io/badge/lang-en-4CAF50?logoColor=white)
  ![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
  ![License](https://img.shields.io/badge/license-MIT-yellow)

</div>

---

## Project Structure

```
├── .env                    # (LOCAL ONLY) Secret environment variables — NEVER push to Git
├── .gitignore              # Files ignored by Git tracking (.env included)
├── LICENSE                 # MIT license by default — change as needed
├── README.md               # You are here
│
├── data/                   # (LOCAL ONLY) Data files processed by scripts
│   ├── input/              # (LOCAL ONLY) Input data, if applicable
│   └── output/             # (LOCAL ONLY) Output data, if applicable
│
├── requirements.txt        # Pip dependencies
│
├── src/                    # All source code
│   ├── main.py             # Main entry point
│   └── project/            # Local project package
│       ├── __init__.py     # Makes this directory a Python package
│       ├── config.py       # Loads .env variables into the Python environment
│       └── utils.py        # Core classes and/or helper functions
│
└── tests/                  # Unit tests
    └── test_main.py        # Main test file (only one created by default)
```

> [!NOTE]
> This is the **intended** default structure. Modify locally as your project requires.

---

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

Delete and reconfigure the template files as needed, and start building your project!

---

## Disclaimer

**This README is part of the template and should be replaced.** Rewrite it with the context, setup instructions, and details specific to your own project.