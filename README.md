Select Language : [:us:](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/README.md) [:brazil:](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/README-pt.md)
<h1 align="center">
  <p align="center">Project Folder Manager</p>
  <p align="center">Creator and Updater</p>
</h1>

This software has been developed to optimize the creation and updating process of multiple project folders that share the same files. With it, you can create a new project directory in the specified workspace, copying the basic files from the local repository according to the settings defined in the configuration file.

The software updates only the files present in the destination folder corresponding to the repository, avoiding the presence of unnecessary basic files in the project folders.

## Configuration File
The configuration file is a .json file that contains the following keys:

- **workspace : str**
	- Full path to the workspace.
	- Ex: "/home/gnome/Documents/workspace"  
	
- **internal_folder : str**
	- Folder within each project folder.
	- Ex: "Script"

- **source_folders : List[str]**
	- Folder(s) that contain the files to be copied to the project folders.
	- Ex: ["repository/library"]

- **target_folders : List[str]**
	- Folder(s) that will receive the project files from the repository.
 	- Ex: ["project_01/server", "project_01/client", "project_02", "project_03", "project_04", "project_05"] 

## Parameters Argparse

- -up or --update
  - With this parameter, all folders will be updated.
- -gc or –get_config
  - Generate a configuration file, it will be saved in the same directory as the software.
- -cf or --config_file
  - Path of the configuration file, the default is in the same folder as the software.
- -np or –new_project
  - Name of the new directory within the workspace.

## Scenario

Imagine the following situation: you have multiple basic files containing methods or classes that need to be used in different projects, which are distributed across various folders. Whenever you make a change to one of these base files, you would need to manually update it in all the other project folders.

To solve this problem, a software has been developed to facilitate this task. The idea is to use a local repository where you can make the necessary changes to the base file. Then, simply run this software to automatically update the project folders specified in the configuration file.

With this approach, you can avoid the need to manually update each project folder, making the process more efficient and eliminating potential errors. The software takes care of propagating the changes to all relevant folders as indicated in the configuration file.

Here is an example of the workspace structure with the basic files:
```shell
workspace
├── repository
│   └── library
│       ├── Basic_enum.py
│       ├── Class_db.py
│       ├── Class_xyz.py
│       ├── Decorators.py
│       ├── Image_filter.py
│       ├── Score_checker.py
│       ├── basic_main_window.ui
│       └── peripheral_analyzer.py
├── project_01
│   ├── client
│   │   └── Script
│   │       ├── Basic_enum.py
│   │       ├── Class_db.py
│   │       ├── Class_xyz.py
│   │       ├── Decorators.py
│   │       ├── Image_filter.py
│   │       ├── Score_checker.py
│   │       ├── basic_main_window.ui
│   │       └── peripheral_analyzer.py
│   └── server
│       └── Script
│           ├── Basic_enum.py
│           ├── Class_db.py
│           ├── Class_xyz.py
│           └── Decorators.py
├── project_02
│   └── Script
│       ├── Basic_enum.py
│       ├── Class_xyz.py
│       ├── Image_filter.py
│       ├── Score_checker.py
│       ├── basic_main_window.ui
│       └── peripheral_analyzer.py
├── project_03
│   └── Script
│       ├── Basic_enum.py
│       ├── Class_db.py
│       ├── Decorators.py
│       ├── Score_checker.py
│       └── basic_main_window.ui
├── project_04
│   └── Script
│       ├── Class_db.py
│       ├── Decorators.py
│       ├── Image_filter.py
│       ├── Score_checker.py
│       ├── basic_main_window.ui
│       └── peripheral_analyzer.py
└── project_05
    └── Script
        ├── Basic_enum.py
        ├── Class_xyz.py
        ├── Decorators.py
        ├── basic_main_window.ui
        └── peripheral_analyzer.py
```
With the configuration file properly filled, we can update the project folders:
```json
{
  "workspace": "/home/gnome/Documents/workspace",
  "internal_folder": "Script",
  "source_folders": [
    "repository/library"
  ],
  "target_folders": [
    "project_01/server",
    "project_01/client",
    "project_02",
    "project_03",
    "project_04",
    "project_05"
  ]
}
```
Now, all we have to do is run the program in the following way:
```
project_creator_updater.py -up
```
 ![](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/docs/updating_all_directories.gif)

To create new projects with the basic files, simply follow these steps:
```
project_creator_updater.py -np project_06
```
 ![](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/docs/creating_project_directory.gif)

This will create the new project in the workspace and update the configuration file.
```json
{
  "workspace": "/home/gnome/Documents/workspace",
  "internal_folder": "Script",
  "source_folders": [
    "repository/library"
  ],
  "target_folders": [
    "project_01/server",
    "project_01/client",
    "project_02",
    "project_03",
    "project_04",
    "project_05",
    "project_06",
  ]
}
```
****
The system supports the use of multiple configuration files, allowing for different sets of data for different scenarios. This way, each configuration file can contain specific settings for a particular set of project folders and base files.

Additionally, if you wish to create a new configuration file, you can use the following command:
```
project_creator_updater.py -gc
```
This command will create a new file and save it in the same directory where the software is located. However, it's important to remember to rename the previous configuration file to avoid unwanted overwriting.

This functionality allows you to conveniently create customized configurations, ensuring that each set of project folders has its own configuration file, thereby avoiding conflicts and facilitating system organization.

To switch between these configuration files, you can use the command:
```
project_creator_updater.py -cf config/file/path -np new_project_name
```
or
```
project_creator_updater.py -cf config/file/path -up
```
depending on what you want to do.
