# research_template

A template for anyone looking to do modern python experiment research work. This was born after lots of painful lessons were learned, so hopefully it saves you time and effort

# Pre-requisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Have [git](https://git-scm.com) installed, and have your [SSH keys fully set up](https://publish.obsidian.md/ahmedlab/atoms/setting+up+github+SSH)

# Next Steps

0. Run `python init_project.py` and follow the prompt(s) to initialize your project
1. Run `uv sync` to install core dependencies (marimo, tqdm)
2. Install optional dependency groups as needed:
   - `uv sync --extra dev` - development tools (basedpyright, ruff, pdbp, loguru)
   - `uv sync --extra analysis` - data analysis packages (matplotlib, seaborn, pandas, polars)
   - `uv sync --all-extras` - install everything
3. Run `uv run python main.py` to verify everything works
4. Run `uv add x`, where `x` is the name of the package you want to install

# Project Structure

This template uses the modern `src/` layout, which means your package code lives in `src/{your_project_name}/`. This prevents accidentally importing from the source directory and ensures you're testing the installed package.

## Dependency Groups

- **Core**: Minimal dependencies (marimo, tqdm) installed by default
- **dev**: Development and debugging tools (basedpyright, ruff, pdbp, loguru)
- **analysis**: Data analysis and visualization (matplotlib, seaborn, pandas, polars) 

# Data Leakage, Reproducibility and Versioning

See the [data/README](./data/README) for more information, but TL;DR you will want to be cognizant of how you handle your data.
