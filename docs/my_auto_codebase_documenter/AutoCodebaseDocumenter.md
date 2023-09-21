AutoCodebaseDocumenter.py
This documentation file was created on 21 September 2023 at 09:17:26

## File path

.\my_auto_codebase_documenter\AutoCodebaseDocumenter.py

## Objectif du fichier

Ce fichier est conçu pour générer automatiquement une documentation pour une base de code en utilisant l'API OpenAI. Il parcourt tous les fichiers Python dans un répertoire spécifié, envoie le contenu de chaque fichier à l'API OpenAI, et écrit la réponse dans un fichier Markdown dans un dossier de documentation.

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
   Le module openai est l'interface Python pour l'API OpenAI. Il est utilisé dans ce fichier pour envoyer le contenu des fichiers Python à l'API OpenAI et obtenir une réponse.

4. ```python 
   from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt
   ```
   Ce module importe le message par défaut qui est envoyé à l'API OpenAI avant le contenu du fichier. Il est utilisé pour donner des instructions à l'API sur la façon de générer la documentation.

***
### Classes
#### Class: AutoCodebaseDocumenter 

Objectif : Cette classe est conçue pour générer automatiquement une documentation pour une base de code en utilisant l'API OpenAI.

##### Méthodes : méthodes de la classe
1. ```python 
   __init__(self, openai_org_id, openai_api_key, root_path=".", output_docs_folder_name="docs", ignore_folders=["venv",".git","tests"], is_ignore_gitignore = True, file_types=[".py"], unwanted_files=None, skip_existing=False, gpt_model="gpt-3.5-turbo", language='en')
   ```
   Initialise la classe avec les paramètres nécessaires pour générer la documentation. 
   
   ##### Variables:
   - self.root_path : Le chemin du répertoire racine où se trouvent les fichiers à documenter.
   - self.output_docs_folder_name : Le nom du dossier où la documentation sera écrite.
   - self.ignore_folders : Les dossiers à ignorer lors de la recherche de fichiers à documenter.
   - self.is_ignore_gitignore : Si vrai, les fichiers spécifiés dans le fichier .gitignore seront ignorés.
   - self.file_types : Les types de fichiers à documenter.
   - self.unwanted_files : Les fichiers spécifiques à ignorer lors de la documentation.
   - self.skip_existing : Si vrai, les fichiers de documentation existants ne seront pas écrasés.
   - self.gpt_model : Le modèle OpenAI à utiliser pour générer la documentation.
   - self.docs_dir : Le chemin du répertoire où la documentation sera écrite.
   - self.system_message : Le message système à envoyer à l'API OpenAI avant le contenu du fichier.
   
2. ```python 
   _get_completion(self, prompt)
   ```
   Envoie le contenu du fichier à l'API OpenAI et obtient une réponse. Le paramètre `prompt` est le contenu du fichier à documenter.

3. ```python 
   _get_file_paths(self)
   ```
   Obtient une liste de tous les fichiers à documenter en parcourant le répertoire racine et en ignorant les dossiers et fichiers spécifiés.

4. ```python 
   _process_file(self, file_path)
   ```
   Traite un seul fichier en envoyant son contenu à l'API OpenAI, en obtenant une réponse et en écrivant cette réponse dans un fichier de documentation. Le paramètre `file_path` est le chemin du fichier à documenter.

5. ```python 
   process_all_files(self)
   ```
   Traite tous les fichiers à documenter en appelant la méthode `_process_file` sur chaque fichier.

6. ```python 
   process_single_file(self, file_path)
   ```
   Cette méthode est prévue pour traiter un seul fichier, mais elle n'est pas encore implémentée. Le paramètre `file_path` serait le chemin du fichier à documenter.

***
### Méthodes:  
Il n'y a pas de méthodes en dehors de la classe dans ce fichier.

***
### Variables:
Il n'y a pas de variables globales en dehors des fonctions et des classes dans ce fichier.
