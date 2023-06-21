# :construction: **Criador e Atualizador de Pastas de Projetos** :construction:

Este software foi desenvolvido para otimizar a atualização de várias pastas de projetos que contem os mesmos arquivos, também é possível com ele criar um novo diretório de projeto que vai receber os arquivos básicos que estão no repositório local, com base nos dados do arquivo de configuração.

Este software só atualiza os arquivos que estiverem presentes na pasta de destino, correspondente ao repositório, com isso não teremos arquivos básicos desnecessários.

## Arquivo de Configuração
Este arquivo é um .json que possui as sequentes chaves:

- **workspace : str**
	- Caminho completo até o workspace.
	- Ex: “D:/usr/Documentos/workspace”  
	
- **internal_folder : str**
	- Pasta dentro de cada pasta do projeto:
	- Exe:  “Script”

- **source_folders : List[str]**
	- Pasta ou pastas que tem os arquivos que serão copiados para as pastas de projetos.
	- Exe: “Repository/Library”

- **target_folders : List[str]**
	- Pasta ou pastas que vão receber os arquivos do projeto que estão no repositório.

## Parameters Argparse

- -up or --update
  - Com este parâmetro todas as pastas serão atualizadas.
- -gc or –get_config
  - Gerar um arquivo de configuração.
- -cf or --config_file
  - Caminho do arquivo de configuração, o padrão é na mesma pasta que tá o software.
- -np or –new_project
  - Nome do novo diretório dentro do workspace.
 
