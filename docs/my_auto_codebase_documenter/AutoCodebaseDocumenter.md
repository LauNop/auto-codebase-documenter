AutoCodebaseDocumenter.py
This documentation file was created on 21 September 2023 at 11:27:52

## File path

.\my_auto_codebase_documenter\AutoCodebaseDocumenter.py

## Objectif du fichier

Ce fichier est conçu pour générer automatiquement une documentation pour une base de code en utilisant l'API OpenAI. Il parcourt tous les fichiers Python dans un répertoire spécifié, envoie le contenu de chaque fichier à l'API OpenAI pour analyse, puis écrit la réponse de l'API dans un fichier Markdown dans un dossier de documentation.

## Codebase

### Imports: 

1. ```python 
   from datetime import datetime
   ```
   Le module datetime est généralement utilisé pour manipuler les dates et les heures. Dans ce fichier, il est utilisé pour générer un horodatage lors de la création de la documentation.

2. ```python 
   import os
   ```
   Le module os fournit une interface portable pour utiliser les fonctionnalités dépendantes du système d'exploitation. Dans ce fichier, il est utilisé pour manipuler les chemins de fichiers et les répertoires.

3. ```python 
   import openai
   ```
   Le module openai est utilisé pour interagir avec l'API OpenAI. Dans ce fichier, il est utilisé pour envoyer le contenu des fichiers Python à l'API OpenAI pour analyse.

4. ```python 
   from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt
   ```
   Ce module est utilisé pour importer le message par défaut qui sera envoyé à l'API OpenAI. Le message par défaut est utilisé pour guider l'API sur ce qu'elle doit faire.

***

### Classes

#### Classe: AutoCodebaseDocumenter 

Objectif: Cette classe est conçue pour générer automatiquement une documentation pour une base de code.

##### Méthodes: 

1. ```python 
   __init__(self, openai_org_id, openai_api_key, root_path=".", output_docs_folder_name="docs", ignore_folders=["venv",".git","tests"], is_ignore_gitignore=True, file_types=[".py"], unwanted_files=None, skip_existing=False, gpt_model="gpt-3.5-turbo", language='en')
   ```
   Initialise la classe avec les paramètres nécessaires pour générer la documentation. 
   
   ##### Variables:
   - self.root_path : Le chemin du répertoire racine où se trouvent les fichiers à documenter.
   - self.output_docs_folder_name : Le nom du dossier où la documentation sera écrite.
   - self.ignore_folders : Les dossiers à ignorer lors de la recherche de fichiers à documenter.
   - self.is_ignore_gitignore : Un booléen indiquant si les fichiers spécifiés dans .gitignore doivent être ignorés.
   - self.file_types : Les types de fichiers à documenter.
   - self.unwanted_files : Les fichiers spécifiques à ignorer lors de la documentation.
   - self.skip_existing : Un booléen indiquant si les fichiers de documentation existants doivent être ignorés.
   - self.gpt_model : Le modèle OpenAI à utiliser pour l'analyse.
   - self.docs_dir : Le chemin du répertoire où la documentation sera écrite.
   - self.system_message : Le message système à envoyer à l'API OpenAI.
   
2. ```python 
   _get_completion(self, prompt)
   ```
   Envoie le contenu d'un fichier à l'API OpenAI pour analyse et renvoie la réponse.

3. ```python 
   _get_file_paths(self)
   ```
   Parcourt le répertoire racine et ses sous-répertoires pour trouver tous les fichiers à documenter.

4. ```python 
   _process_file(self, file_path)
   ```
   Traite un seul fichier : envoie son contenu à l'API OpenAI pour analyse, puis écrit la réponse dans un fichier de documentation.

5. ```python 
   process_all_files(self)
   ```
   Traite tous les fichiers dans le répertoire racine et ses sous-répertoires.

6. ```python 
   process_single_file(self, file_path)
   ```
   Traite un seul fichier spécifié par l'utilisateur. Cette méthode n'est pas encore implémentée.

***

### Méthodes:  

Il n'y a pas de méthodes en dehors des classes dans ce fichier.

***

### Variables:

Il n'y a pas de variables globales en dehors des fonctions et des classes dans ce fichier.
