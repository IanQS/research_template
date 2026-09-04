import os
from pathlib import Path


def rename_folder(proj_name):
    """
    Rename the template package folder to the project name
    """
    script_dir = Path(__file__).parent
    old_path = script_dir / "src" / "template_package"
    new_path = script_dir / "src" / proj_name

    if old_path.exists():
        os.rename(old_path, new_path)
    else:
        print(f"Warning: {old_path} does not exist")


def create_data_directories(proj_name):
    """
    Create data subdirectories as mentioned in data/README
    """
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"

    # Create the subdirectories
    (data_dir / "raw").mkdir(parents=True, exist_ok=True)
    (data_dir / "processed").mkdir(parents=True, exist_ok=True)
    (data_dir / "modeling_data").mkdir(parents=True, exist_ok=True)

    print(f"Created data directories: raw/, processed/, modeling_data/")


def change_main_import(proj_name):
    """
    Update the import statement in main.py to use the new project name
    """
    script_dir = Path(__file__).parent
    main_file = script_dir / "main.py"

    with open(main_file) as f:
        content = f.read()

    # Replace template_package with the new project name
    updated_content = content.replace("template_package", proj_name)

    with open(main_file, "w") as f:
        f.write(updated_content)


def setup_uv_pyproject(proj_name):
    """
    Update the project name in pyproject.toml
    """
    with open("pyproject.toml") as f:
        lines = f.readlines()

    # Fix TOML syntax: use = "value" instead of : value
    lines[1] = f'name = "{proj_name}"\n'

    with open("pyproject.toml", "w") as f:
        f.writelines(lines)


def append_to_pyproject(proj_name):
    """
    Add build system configuration and tool settings to pyproject.toml
    """
    to_write = f"""
[tool.pyrefly]
# For import resolution
search-path = ["src/{proj_name}**", "experiments/**"]  
# For which files to check! 
project-includes = ["src/{proj_name}/**", "experiments"]
project-excludes = [
    "src/{proj_name}.egg-info",
    "**/tests",
]
python-interpreter-path = ".venv/bin/python3"

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
include = ["{proj_name}*"]

"""
    with open("pyproject.toml", "a") as f:
        f.write(to_write)


if __name__ == "__main__":
    proj_name = input("What is the name of your project? Use '_' instead of spaces: ")

    print(f"\nInitializing project: {proj_name}")
    print("-" * 50)

    rename_folder(proj_name)
    print(f"Renamed src/template_package/ → src/{proj_name}/")

    create_data_directories(proj_name)
    print(f"Created data subdirectories")

    setup_uv_pyproject(proj_name)
    print(f"Updated project name in pyproject.toml")

    change_main_import(proj_name)
    print(f"Updated imports in main.py")

    append_to_pyproject(proj_name)
    print(f"Added build configuration to pyproject.toml")

    print("\n" + "=" * 50)
    print(f"Setup complete! Next steps:")
    print(f"  1. Run 'uv sync' to install all dependencies")
    print(f"  2. Run 'uv run python main.py' to test your setup")
    print("=" * 50)
