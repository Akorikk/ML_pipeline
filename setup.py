from setuptools import find_packages, setup
from typing import List

PROJECT_NAME = "Machine learning"
VERSION = '0.0.1'
DESCRIPTION = "This is a Machine Learning Project"
AUTHOR_NAME = "Abhishek Kori"
AUTHOR_EMAIL = "abhishekkori601@gmail.com"

REQUIREMENTS_FILE = "requirements.txt"
HYP = "-e ."

def get_requirements_list()-> List[str]:
    with open(REQUIREMENTS_FILE) as requirements_list:
        requirements_files = requirements_list.readline()
        requirements_files = (req.replace("\n","") for req in requirements_files)

        if HYP in requirements_files:
            requirements_files.remove(HYP)

    return requirements_files        

setup(
     name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list(),

)