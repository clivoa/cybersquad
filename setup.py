from setuptools import find_packages, setup

setup(
    name="cybersquad",
    version="0.1.0",
    description="Prompt-driven virtual cybersecurity squad with installable workspace templates",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={"cybersquad": ["template/**"]},
    entry_points={"console_scripts": ["cybersquad=cybersquad.cli:main"]},
)
