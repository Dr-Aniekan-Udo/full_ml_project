from setuptools import find_packages,setup
from typing import List

ignore = '-e .'
def get_req(file_path:str)->List[str]:
    '''
    this function returns a list of requirements to the setup file
    '''
    req = []
    with open(file_path) as file_obj:
        # read file content one per line
        req=file_obj.readlines()
        #replace the \n that comes with the text with space
        req=[name.replace("\n"," ") for name in req]

        if ignore in  req:
            req.remove(ignore)

    return req


setup(
    name='ml project',
    version='0.01',
    author='Aniekan Udo',
    author_email='aniekanetimudo@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)