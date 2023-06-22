# :construction: **Gerenciador de Pastas de Projetos - Criador e Atualizador** :construction:

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


<!--
 ![](https://github.com/yhagor/Project_folder_creator_and_updater/blob/main/docs/creating_project_directory.gif)
-->
