# filepath: /home/luke/Development/code/phase-3/my-cli-project/setup.py
from setuptools import setup, find_packages

setup(
    name="my-cli-project",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sqlalchemy",  # Add other dependencies here if needed
    ],
    entry_points={
        "console_scripts": [
            "my-cli=lib.cli:run",  # Optional: Create a CLI command
        ],
    },
)