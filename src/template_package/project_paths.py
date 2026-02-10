"""
Single config file for all the paths

Path resolution for src/ layout:
- This file: src/{project_name}/project_paths.py
- parent (1x): src/{project_name}/
- parent (2x): src/
- parent (3x): PROJECT_ROOT (e.g., /path/to/research_template/)
"""

from pathlib import Path


# --- Base Directories ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Navigates up from src/{project}/ to project root
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
PLOTS_DIR = PROJECT_ROOT / "plots"
