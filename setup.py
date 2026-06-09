from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

repo_name = "chicken_disease_classifier"
author = 'Amir'
email = "oyelekeamir123@gmail.com"


setup(
    name= repo_name,
    version=__version__,
    author= author,
    author_email= email,
    description="A simple neural network for detecting chicken diseases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires= get_requirements("requirements.txt")
)