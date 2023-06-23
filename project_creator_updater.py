#!python3
# -*- coding: utf-8 -*-

import argparse
import shutil
import json
import sys

from os.path import basename, realpath, isfile, join, isdir
from os import listdir, makedirs

from typing import (Dict, List, Union)

PROGRAM_NAME     = 'Lib Update'
MAJOR_VERSION    = '1'
MINOR_VERSION    = '0'
REVISION_VERSION = '0'

PROGRAM_VERSION = f"{MAJOR_VERSION}.{MINOR_VERSION}.{REVISION_VERSION}"

CONFIG_FILE_PATH = realpath(__file__).replace('.py','.json') 

def copy_the_files(src : str, dst : str) -> None:
    """
        Method that will copy the file from one folder to another.
    
        Parameters
        ----------
        src : str
            Full path of the file to be copied.
        
        dst : str
            Full path of the folder that will receive the updated file.
    """    
    shutil.copy2(src, dst)

def creating_new_project(repository_file : List[str], new_project_name : str, config_file_path : str, config_file : Dict[str, Union[str, List[str]]]) -> None:
    """
        Method responsible for creating the new project with the concatenation of the workspace
        path and the subfolder and copying all the files from the repository to the new project
        folder it also updates the configuration file adding this new project in the folders that
        have to be updated if run the software only with the -up parameter.

        Parameters
        ----------
        repository_file : List[str]
            Full path of the files in the repository folder.
        
        new_project_name : str
            Name of the new project folder.
        
        config_file_path : str
            Full path of the configuration file.
        
        config_file : Dict[str, Union[str, List[str]]]
            Data taken from the configuration file.
    """   
    new_project_path = join(join(config_file['workspace'], new_project_name), config_file['internal_folder'])

    if not isdir(new_project_path):
        try:
            makedirs(new_project_path)
            print("New Project Created !")
        
        except OSError as erro:
            print(erro)
            sys.exit(1)
    
    else:
        print("The project folder already exists !")

    print(f"\nfolder: {new_project_path}")

    for file in repository_file:        
        copy_the_files(file, new_project_path)
        print(basename(file))

    print("\nTransferred Files.")
    
    if new_project_name not in config_file["target_folders"]:
        config_file["target_folders"].append(new_project_name)
    
        with open(config_file_path, 'w') as up_file:
            json.dump(config_file, up_file, indent=2) 

        print("Updated configuration file.")

def directory_update(config_file : Dict[str, Union[str, List[str]]], repository_file : List[str]) -> None:
    """
        Method that will update all pre-configured folders in the configuration file.

        It will only update files that already exist in the project folder.

        Parameters
        ----------
        config_file : Dict[str, Union[str, List[str]]]
            Data taken from the configuration file.
        
        repository_file : List[str]
            Full path of the files in the repository folder.
    """
    print("Updating project files")

    for target_folder in config_file["target_folders"]:
        print('')
        
        folder_path = join(join(config_file['workspace'], target_folder), config_file['internal_folder'])
        if not isdir(folder_path):
            folder_path = join(config_file['workspace'], target_folder)        
            if not isdir(folder_path):
                print(f"Folder not found: {folder_path}")
                continue

        print(f"Updating folder: {folder_path}")

        for file_path in repository_file:
            if isfile(join(folder_path, basename(file_path))):
                copy_the_files(file_path, folder_path)
                print(basename(file_path))

    print("\nUpdated files.")

def get_files_from_repository(workspace : str, source_folders : List[str]) -> List[str]:
    """
        Method responsible for concatenating all file paths in the local repository folder.

        Parameters
        ----------
        workspace : str
            Full path to the workspace.
        
        source_folders : List[str]
            Folder or folders that have the files that will be copied to the project folders.
        
        Returns
        -------
        List[str]
            Full path of the files in the repository folder.            
    """
    repository_files = []
    for source_folder in source_folders:

        repository_path = join(workspace, source_folder)

        for file in listdir(repository_path):
            
            file_path = join(repository_path, file)

            if isfile(file_path):
                repository_files.append(file_path)

    return repository_files

def processa(config_file : Dict[str, Union[str, List[str]]], update : bool, new_project_name : Union[None,str], config_file_path : str) -> None:
    """
        This method is responsible for directing the workflow.

        Parameters
        ----------
        config_file : Dict[str, Union[str, List[str]]]
            Data taken from the configuration file.
        
        update : bool
            Value that indicates if the folders will be updated.
        
        new_project_name : Union[None,str]
            Indicates the new project folder.
        
        config_file_path : str
            Full path of the configuration file.
    """
    repository_files = get_files_from_repository(config_file['workspace'], config_file['source_folders'])
    
    if update: 
        directory_update(config_file, repository_files)

    if new_project_name:        
        creating_new_project(repository_files, new_project_name, config_file_path, config_file)  

def validator(update : bool, config_file_path : str, new_project_name : Union[None,str], get_config_file: bool) -> None:
    """
        Method that checks the request for a new configuration file and validates information in an existing configuration file.

        Parameters
        ----------
        update : bool
            Value that indicates if the folders will be updated.
        
        config_file_path : str
            Full path of the configuration file.
        
        new_project_name : Union[None,str]
            Indicates the new project folder.
        
        get_config_file : bool
            Value indicating whether you want a new configuration file.
    """
    valid = True

    if get_config_file:
        data = {"workspace"       : "path/workspace", 
                "internal_folder" : "script",
                "source_folders"  : ["path/repository/library"],
                "target_folders"  : ["project_01/server", "project_01/client", "project_02", "project_03", "project_05", "project_06"]                   
                }
        with open(config_file_path, 'w') as config_file:
            json.dump(data, config_file, indent=2)     
    
        print("Configuration file created, now just add the correct paths.")        
        print(f"The file is at:{config_file_path}")        
        sys.exit(0)

    if not isfile(config_file_path):
        print("Configuration file not found!")
        sys.exit(0)
    
    else:
        try:
            with open(config_file_path, 'r') as openfile:
                config_file = json.load(openfile) 
        except:
            print("Error reading configuration file.")
            print("Run the program again with the -gc option to get a new configuration file.")
            sys.exit(0)

    if config_file.get('internal_folder') is None:
        print(f"ERROR: key 'internal_folder' not found in config file {basename(config_file_path)}")
        valid = False

    if not isinstance(config_file['internal_folder'], str):
        print(f"ERROR: internal_folder it has to be a str and not {type(config_file['source_folders'])}")
        valid = False

    if config_file.get('workspace') is None:
        print(f"ERROR: key 'workspace' not found in config file {basename(config_file_path)}")
        valid = False

    if not isinstance(config_file['workspace'], str):
        print(f"ERROR: workspace it has to be a str and not {type(config_file['source_folders'])}")
        valid = False    

    if config_file.get('source_folders') is None:
        print(f"ERROR: key 'source' not found in config file {basename(config_file_path)}")
        valid = False
    
    if not isinstance(config_file['source_folders'], list):
        print(f"ERROR: source_folders it has to be a list and not {type(config_file['source_folders'])}")
        valid = False

    if config_file.get('target_folders') is None:
        print(f"ERROR: key'target' not found in config file {basename(config_file_path)}")
        valid = False    

    if not isinstance(config_file['target_folders'], list):
        print(f"ERROR: target_folders it has to be a list and not {type(config_file['target_folders'])}")
        valid = False

    if not valid:
        sys.exit(1)

    processa(config_file, update, new_project_name, config_file_path)

def print_parameters(update : bool, config_file_path : str, new_project_name : Union[None,str]) -> None:
    """
        Method that will display the options chosen when running the software.
        
        Parameters
        ----------
        update : bool
            Value that indicates if the folders will be updated.
        
        config_file_path : str
            Full path of the configuration file.
        
        new_project_name : Union[None, str]
            Indicates the new project folder.
    """
    print(f"\n{PROGRAM_NAME} Ver {PROGRAM_VERSION} processing")
    print(f"Config file : {config_file_path}")
    print(f"Update File : {update}")    
    print(f"New Project : {new_project_name}\n") if new_project_name else print(f"New Project : None\n") 
  
def main() -> None:
    """
        This software was developed to optimize the updating of several project folders that contain the same
        files and also has the option of creating a project directory that will receive the basic files that
        are in the local repository, based on the configuration file.

        This software only updates the files that are in the folder leaving no garbage in the destination folder.

        The configuration file has the following specifications:
        It's a .json file that has the following keys:

        workspace : str
            Full path to the workspace.
            Ex: "/home/gnome/Documents/workspace"

        internal_folder : str
            Folder within each project folder.
            Ex:  "Script"

        source_folders : List[str]
            Folder or folders that have the files that will be copied to the project folders.
            Ex: ["repository/library"]

        target_folders : List[str]
            Folder or folders that will receive the project files that are in the repository.
            Ex: ["project_01/server", "project_01/client", "project_02", "project_03", "project_04", "project_04"]

        Parameters Argparse
        ----------
        -up or --update 
            With this parameter all folders will be updated.

        -gc or --get_config
            Generate a configuration file, Generate a configuration file, it will be saved in the same directory as this software.

        -cf or --config_file
            Configuration file path, the default is in the same folder as the software.

        -np or --new_project
            Name of the new directory within the workspace.
    """
    parser = argparse.ArgumentParser(description='Lib Update')
    parser.add_argument("-up", "--update", dest='update', help="With this parameter all folders will be updated.", required=False, action="store_true")
    parser.add_argument("-gc", "--get_config", dest='get_config_file', help="Generate a configuration file, it will be saved in the same directory as this software.", required=False, action="store_true")
    parser.add_argument("-cf", "--config_file", dest='config_file_path', type=str, help='Configuration file path, the default is in the same folder as the software.', required=False, default=CONFIG_FILE_PATH)
    parser.add_argument("-np", "--new_project", dest='new_project_name', type=str, help='Name of the new directory within the workspace.', required=False, default=None)
    
    args = parser.parse_args()

    print_parameters(args.update, args.config_file_path, args.new_project_name)

    validator(args.update, args.config_file_path, args.new_project_name, args.get_config_file)

if __name__ == "__main__":
    main()
