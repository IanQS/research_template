# research_template

A template for anyone looking to do modern python experiment research work. This was born after lots of painful lessons were learned, so hopefully it saves you time and effort.

## Note:

If you're using `flywire`, you might want to save all the data to one location and then `symlink` them, to avoid needing multiple copies of the data. Here's how you can do it, assuming that `flywire_data` is at the home directory:

`ln -s /home/iq/flywire_data research/some_project/data/raw`

where `iq` was my username, and the project was located in the home directory under `research/some_project`

# Pre-requisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Have [git](https://git-scm.com) installed, and have your [SSH keys fully set up](https://publish.obsidian.md/ahmedlab/atoms/setting+up+github+SSH)

# Next Steps

0. Run `python init_project.py` and follow the prompt(s) to initialize your project
1. Run `uv sync` to install core dependencies (marimo, tqdm)
2. Run `uv run python main.py` to verify everything works
3. Run `uv add x`, where `x` is the name of the package you want to install

# Project Structure

This template uses the modern `src/` layout, which means your package code lives in `src/{your_project_name}/`. This prevents accidentally importing from the source directory and ensures you're testing the installed package.

## Experiments

Typically goes into the `experiment` folder. As the name says, this is more for rough experimentation. Ideally once you've got some groundwork laid you moved the code over into the appropriate `src/...`

# Data Leakage, Reproducibility and Versioning

See the [data/README](./data/README) for more information, but TL;DR you will want to be cognizant of how you handle your data.
