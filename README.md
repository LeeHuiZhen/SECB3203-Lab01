# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: Lee Hui Zhen, A24CS0259

## Setup

### Windows (Command Prompt):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
pip freeze > requirements-frozen.txt
```

### Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pip freeze > requirements-frozen.txt
```

## Run

Run tests: 
```bash
python -m pytest
```

Run code style check: 
```bash
ruff check src tests
```

Generate environment report: 
```bash
python src/env_check.py > results/environment_report.txt
```

## What is in this repository

- `src/`: Source code directory containing modular Python programs.

- `tests/`: Automated testing directory containing visible and custom test suites.

- `data/`: Read-only directory containing synthetic laboratory datasets.

- `results/`: Output directory for generated artifacts and reports.

- `src/env_check.py`: Module inspecting Python runtime, OS metadata, and installed package versions.

- `src/basics.py`: Module implementing GC percentage calculations, report string formatting, and base count parsing.

- `tests/test_visible.py`: Provided unit tests checking baseline function contracts.

- `tests/test_lab01_own.py`: Custom unit tests covering boundary conditions, zero totals, and invalid inputs.

- `data/qc_records.csv`: Read-only synthetic laboratory quality control records.

- `results/environment_report.txt`: Generated text file recording verified runtime environment versions.

- `requirements.txt`: Specified list of required project dependencies.

- `requirements-frozen.txt`: Pinned snapshot of exact package versions installed in the virtual environment.

- `pytest.ini`: Test runner configuration setting discovery paths and pythonpath.

- `.gitignore`: Rules excluding virtual environments, caches, and generated artifacts from Git.

- `AI_USE_LOG.md`: Interaction log documenting generative AI usage and verification under course policy.

- `README.md`: Project documentation detailing setup, run commands, layout, and ignored files.

## What is not committed, and why

The `.venv/` and `results/` folders are ignored by Git via `.gitignore`. Committing `.venv/` would push platform-specific binaries that break on other machines, while committing `results/` would clutter version history with generated artefacts that should always be reproduced from source code.
