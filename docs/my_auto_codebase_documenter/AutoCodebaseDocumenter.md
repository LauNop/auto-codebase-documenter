AutoCodebaseDocumenter.py
This documentation file was created on 21 September 2023 at 11:27:52

## File path

.\my_auto_codebase_documenter\AutoCodebaseDocumenter.py

## Objectif du fichier

Ce fichier est con�u pour g�n�rer automatiquement une documentation pour une base de code en utilisant l'API OpenAI. Il parcourt tous les fichiers Python dans un r�pertoire sp�cifi�, envoie le contenu de chaque fichier � l'API OpenAI pour analyse, puis �crit la r�ponse de l'API dans un fichier Markdown dans un dossier de documentation.

## Codebase

### Imports: 

1. ```python 
   from datetime import datetime
   ```
   Le module datetime est g�n�ralement utilis� pour manipuler les dates et les heures. Dans ce fichier, il est utilis� pour g�n�rer un horodatage lors de la cr�ation de la documentation.

2. ```python 
   import os
   ```
   Le module os fournit une interface portable pour utiliser les fonctionnalit�s d�pendantes du syst�me d'exploitation. Dans ce fichier, il est utilis� pour manipuler les chemins de fichiers et les r�pertoires.

3. ```python 
   import openai
   ```
   Le module openai est utilis� pour interagir avec l'API OpenAI. Dans ce fichier, il est utilis� pour envoyer le contenu des fichiers Python � l'API OpenAI pour analyse.

4. ```python 
   from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt
   ```
   Ce module est utilis� pour importer le message par d�faut qui sera envoy� � l'API OpenAI. Le message par d�faut est utilis� pour guider l'API sur ce qu'elle doit faire.

***

### Classes

#### Classe: AutoCodebaseDocumenter 

Objectif: Cette classe est con�ue pour g�n�rer automatiquement une documentation pour une base de code.

##### M�thodes: 

1. ```python 
   __init__(self, openai_org_id, openai_api_key, root_path=".", output_docs_folder_name="docs", ignore_folders=["venv",".git","tests"], is_ignore_gitignore=True, file_types=[".py"], unwanted_files=None, skip_existing=False, gpt_model="gpt-3.5-turbo", language='en')
   ```
   Initialise la classe avec les param�tres n�cessaires pour g�n�rer la documentation. 
   
   ##### Variables:
   - self.root_path : Le chemin du r�pertoire racine o� se trouvent les fichiers � documenter.
   - self.output_docs_folder_name : Le nom du dossier o� la documentation sera �crite.
   - self.ignore_folders : Les dossiers � ignorer lors de la recherche de fichiers � documenter.
   - self.is_ignore_gitignore : Un bool�en indiquant si les fichiers sp�cifi�s dans .gitignore doivent �tre ignor�s.
   - self.file_types : Les types de fichiers � documenter.
   - self.unwanted_files : Les fichiers sp�cifiques � ignorer lors de la documentation.
   - self.skip_existing : Un bool�en indiquant si les fichiers de documentation existants doivent �tre ignor�s.
   - self.gpt_model : Le mod�le OpenAI � utiliser pour l'analyse.
   - self.docs_dir : Le chemin du r�pertoire o� la documentation sera �crite.
   - self.system_message : Le message syst�me � envoyer � l'API OpenAI.
   
2. ```python 
   _get_completion(self, prompt)
   ```
   Envoie le contenu d'un fichier � l'API OpenAI pour analyse et renvoie la r�ponse.

3. ```python 
   _get_file_paths(self)
   ```
   Parcourt le r�pertoire racine et ses sous-r�pertoires pour trouver tous les fichiers � documenter.

4. ```python 
   _process_file(self, file_path)
   ```
   Traite un seul fichier : envoie son contenu � l'API OpenAI pour analyse, puis �crit la r�ponse dans un fichier de documentation.

5. ```python 
   process_all_files(self)
   ```
   Traite tous les fichiers dans le r�pertoire racine et ses sous-r�pertoires.

6. ```python 
   process_single_file(self, file_path)
   ```
   Traite un seul fichier sp�cifi� par l'utilisateur. Cette m�thode n'est pas encore impl�ment�e.

***

### M�thodes:  

Il n'y a pas de m�thodes en dehors des classes dans ce fichier.

***

### Variables:

Il n'y a pas de variables globales en dehors des fonctions et des classes dans ce fichier.
