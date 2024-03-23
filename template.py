# This file is used to create the template of our project. By running this we can create the necessary folders and directories for our project our project

import os
from pathlib import Path
import logging

# Creating log files to track our progress
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Initializing project name and list of files
project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  #__init__ is necessary so that we can use our project as local package and import modules
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init_.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/constant/__init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py"
    "main.py",
    "Dockerfile"
    "requirements.txt"
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   # for detecing our OS
    filedir, filename = os.path.split(filepath) # for getting directory and filename separately
    
    # Check if directory exists or not
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # creating directories recursively
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    # Check if file exists or not    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filename}")
        
    else:
        logging.info(f"File: {filename} already exists")
            
        
        
        
        
    