AutoCodebaseDocumenter.py
This documentation file was created on 21 September 2023 at 13:34:38

## File path

.\my_auto_codebase_documenter\AutoCodebaseDocumenter.py

## Objectif du fichier

Ce fichier est conçu pour générer automatiquement une documentation pour une base de code en utilisant l'API OpenAI. Il parcourt tous les fichiers Python dans un répertoire spécifié, envoie le contenu de chaque fichier à l'API OpenAI, et écrit la réponse dans un fichier Markdown dans un dossier de documentation.

## Codebase

### Imports: 

1. ```python 
   from datetime import datetime
   ```
   Le module datetime est généralement utilisé pour manipuler les dates et les heures. Dans ce fichier, il est utilisé pour générer un horodatage qui est ajouté en haut de chaque fichier de documentation généré.

2. ```python 
   import os
   ```
   Le module os fournit une interface portable pour utiliser les fonctionnalités dépendantes du système d'exploitation. Dans ce fichier, il est utilisé pour manipuler les chemins de fichiers et les répertoires.

3. ```python 
   import openai
   ```
   Le module openai est l'interface Python pour l'API OpenAI. Il est utilisé dans ce fichier pour envoyer le contenu des fichiers Python à l'API OpenAI et obtenir une description de ce contenu.

4. ```python 
   from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt
   ```
   Ce module est spécifique à l'application et semble fournir un message par défaut qui est envoyé à l'API OpenAI avant le contenu du fichier Python. Le but de ce message est probablement de donner des instructions à l'IA sur la façon de traiter le contenu du fichier.

***

### Classes

#### Classe : AutoCodebaseDocumenter 

Objectif : Cette classe est le cœur de l'application. Elle contient toutes les méthodes nécessaires pour parcourir les fichiers Python, envoyer leur contenu à l'API OpenAI, et écrire la réponse dans un fichier de documentation.

##### Méthodes : méthodes de la classe

1. ```python 
   __init__(self, openai_org_id, openai_api_key, root_path=".", output_docs_folder_name="docs", ignore_folders=["venv",".git","tests"], is_ignore_gitignore=True, file_types=[".py"], unwanted_files=None, skip_existing=False, gpt_model="gpt-3.5-turbo", language='en')
   ```
   
   Initialise la classe avec divers paramètres de configuration. 
   
   ##### Variables :
   
   - self.root_path : Le chemin du répertoire racine où se trouvent les fichiers à documenter.
   - self.output_docs_folder_name : Le nom du dossier où les fichiers de documentation seront écrits.
   - self.ignore_folders : Une liste de dossiers à ignorer lors de la recherche de fichiers à documenter.
   - self.is_ignore_gitignore : Un booléen indiquant si les fichiers et dossiers spécifiés dans un fichier .gitignore doivent être ignorés.
   - self.file_types : Une liste des types de fichiers à documenter.
   - self.unwanted_files : Une liste de fichiers spécifiques à ignorer.
   - self.skip_existing : Un booléen indiquant si les fichiers de documentation existants doivent être ignorés ou écrasés.
   - self.gpt_model : Le modèle OpenAI à utiliser pour générer la documentation.
   - self.docs_dir : Le chemin complet du dossier où les fichiers de documentation seront écrits.
   - self.system_message : Le message système à envoyer à l'API OpenAI avant le contenu du fichier.
   
2. ```python 
   _get_completion(self, prompt)
   ```
   
   Envoie le contenu d'un fichier à l'API OpenAI et renvoie la réponse. Le paramètre 'prompt' est une chaîne contenant le contenu du fichier.

3. ```python 
   _get_file_paths(self)
   ```
   
   Parcourt le répertoire racine et ses sous-répertoires pour trouver tous les fichiers qui correspondent aux types de fichiers spécifiés et qui ne sont pas dans les dossiers ignorés ou les fichiers indésirables.

4. ```python 
   _process_file(self, file_path)
   ```
   
   Traite un seul fichier. Il lit le contenu du fichier, l'envoie à l'API OpenAI, et écrit la réponse dans un fichier de documentation.

5. ```python 
   process_all_files(self)
   ```
   
   Traite tous les fichiers dans le répertoire racine et ses sous-répertoires.

6. ```python 
   process_single_file(self, file_path)
   ```
   
   Cette méthode est prévue pour traiter un seul fichier, mais elle n'est pas encore implémentée.

***

### Méthodes:  

Il n'y a pas de méthodes en dehors de la classe dans ce fichier.

***

### Variables:

Il n'y a pas de variables globales en dehors des fonctions et des classes dans ce fichier.
