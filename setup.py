from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_features(file_path:str)->List["str"]:
    """
    this function will return list of requirments 
    """     
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    
    name="mlProject",
    version=0.1,
    author="Kotesh",
    packages=find_packages(),
    install_requires = get_features("requirments.txt")
    
)