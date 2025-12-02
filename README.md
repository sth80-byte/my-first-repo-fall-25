# My First Repo!

## Setup

Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line. Perhaps onto the Desktop folder.

```sh
cd ~/Desktop/local_repository/my-first-repo-fall-25
```

Crrate a virtual environment:

```sh
conda create -n my-first-env-fall-25 python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env-fall-25
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Example script:

```sh
python app/my_script.py
```

Game of rock, paper, scissors:

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```

Stocks Dashboard
```sh
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```
