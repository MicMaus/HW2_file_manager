from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',     # package will be accessible with this name after instal
    description= "script orginizes files to respective directories, normalizes and transliterates names of files na folders, creates lists of files as per category and lists of formats",
    author= "MicMaus",
    version='1.0', 
    packages=find_namespace_packages(), # already tried: ['clean_folder'], / find_packages(), / include=['clean_folder.*']
    entry_points= {'console_scripts': ['clean-folder = clean_folder.clean:main']} #input in terminal = path.py file:func name
)
