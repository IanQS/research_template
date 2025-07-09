"""
Single config file for all the paths
"""

from pathlib import Path


# --- Base Directories ---
# Assumes the script is run from the project root or the paths are adjusted accordingly.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Resolves to whatever the name of the project is/
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
PLOTS_DIR = PROJECT_ROOT / "plots"
