from setuptools import setup
from typing import List

## Declaring variables for setup fuctions
PROJECT_NAME="housing-prediction"
VERSION= "0.0.1"
AUTHOR="Shubham Ranakoti"
DESCRIPTION="This is the housing prediction Machine Learning Project"
PACKAGES=["housing"] ## list of package folders
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file

    return This fuction is going to return a list which contain 
    name of libraries mention in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)