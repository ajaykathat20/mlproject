# Building our applicaton as a package 
from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","")for i in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Ajay',
author_email='ajay.19jdds002@jietjodhpur.ac.in',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')





)

