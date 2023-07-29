from pathlib import Path
import os


BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
DATA_DIR = Path(BASE_DIR, "data")
NOTEBOOK_DIR = Path(BASE_DIR, "notebooks")
ARTIFACTS_DIR = Path(BASE_DIR, "artifacts")
REPORTS_DIR = Path(BASE_DIR, "reports")
RAW_DATA_DIR = Path(DATA_DIR, "raw")

DATA_DIR.mkdir(parents=True, exist_ok=True)
NOTEBOOK_DIR.mkdir(parents=True, exist_ok=True)
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

print(os)