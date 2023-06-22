Select Language : [:us:](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/README.md) [:brazil:](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/README-pt.md)
<h1 align="center">
  <p align="center">:construction: Gerenciador de Pastas de Projetos :construction:</p>
  <p align="center">Criador e Atualizador</p>
</h1>

Este software foi desenvolvido para otimizar a criação e atualização de várias pastas de projetos que compartilham os mesmos arquivos. Com ele, é possível criar um novo diretório de projeto no workspace especificado, copiando os arquivos básicos do repositório local, de acordo com as configurações definidas no arquivo de configuração.

O software atualiza apenas os arquivos presentes na pasta de destino correspondente ao repositório, evitando a presença de arquivos básicos desnecessários nas pastas dos projetos.

## Arquivo de Configuração
O arquivo de configuração é um arquivo .json que contém as seguintes chaves:

- **workspace : str**
	- Caminho completo até o workspace.
	- Ex: "/home/gnome/Documents/workspace"  
	
- **internal_folder : str**
	- Pasta dentro de cada pasta do projeto:
	- Ex: "Script"

- **source_folders : List[str]**
	- Pasta(s) que contém os arquivos a serem copiados para as pastas de projetos.
	- Ex: ["repository/library"]

- **target_folders : List[str]**
	- Pasta(s) que receberão os arquivos do projeto presentes no repositório.
 	- Ex: ["project_01/server", "project_01/client", "project_02", "project_03", "project_04", "project_05"] 

## Parameters Argparse

- -up or --update
  - Com este parâmetro todas as pastas serão atualizadas.
- -gc or –get_config
  - Gerar um arquivo de configuração, ele será salvo no mesmo diretório que esta o software.
- -cf or --config_file
  - Caminho do arquivo de configuração, o padrão é na mesma pasta que tá o software.
- -np or –new_project
  - Nome do novo diretório dentro do workspace.

## Cenário

Imagine a seguinte situação: você possui vários arquivos básicos contendo métodos ou classes que precisam ser utilizados em diferentes projetos, os quais estão distribuídos por várias pastas. Sempre que você realizar uma alteração em um desses arquivos base, será necessário fazer manualmente a atualização em todas as outras pastas de projetos.

Para solucionar esse problema, foi desenvolvido um software que visa facilitar essa tarefa. A ideia é utilizar um repositório local, onde você fará a alteração necessária no arquivo base. Em seguida, basta executar esse software para atualizar automaticamente as pastas de projetos que estão especificadas no arquivo de configuração.

Com essa abordagem, você evita a necessidade de atualizar manualmente cada pasta de projeto, tornando o processo mais eficiente e eliminando possíveis erros. O software se encarrega de propagar as alterações para todas as pastas relevantes, conforme indicado no arquivo de configuração.

Então temos a seguinte estrutura do workspace com os arquivos básicos:
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
Com o arquivo de configuração preenchido corretamente, podemos atualizar as pastas de projetos:
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
Só teremos agora que rodar o programa dessa forma:
```
project_creator_updater.py -up
```
 ![](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/docs/updating_all_directories.gif)

Para criar novos projetos com os arquivos básico é só fazer dessa forma:
```
project_creator_updater.py -np project_06
```
 ![](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/docs/creating_project_directory.gif)

Com isso o novo projeto vai ser criado no workspace e o arquivo de configuração será atualizado.
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
O sistema suporta a utilização de vários arquivos de configuração, permitindo ter conjuntos de dados diferentes para diferentes cenários. Dessa forma, cada arquivo de configuração pode conter configurações específicas para um conjunto particular de pastas de projetos e arquivos base.

Além disso, caso deseje criar um novo arquivo de configuração, você pode utilizar o seguinte comando:
```
project_creator_updater.py -gc
```
O qual criará um arquivo novo e o salvará no mesmo diretório onde o software está localizado. No entanto, é importante lembrar de renomear o arquivo de configuração anterior para evitar a sobrescrição indesejada.

Essa funcionalidade permite que você crie configurações personalizadas de forma conveniente, garantindo que cada conjunto de pastas de projetos possua seu próprio arquivo de configuração, evitando conflitos e facilitando a organização do sistema.

E para alternar entre esses arquivos de configuração utilizaremos o comando:
```
project_creator_updater.py -cf config/file/path -np new_project_name
```
ou
```
project_creator_updater.py -cf config/file/path -up
```
Dependendo do que deseja fazer.
