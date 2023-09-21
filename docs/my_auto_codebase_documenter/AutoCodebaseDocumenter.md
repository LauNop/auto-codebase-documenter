AutoCodebaseDocumenter.py
This documentation file was created on 21 September 2023 at 09:17:26

## File path

.\my_auto_codebase_documenter\AutoCodebaseDocumenter.py

## Objectif du fichier

Ce fichier est con�u pour g�n�rer automatiquement une documentation pour une base de code en utilisant l'API OpenAI. Il parcourt tous les fichiers Python dans un r�pertoire sp�cifi�, envoie le contenu de chaque fichier � l'API OpenAI, et �crit la r�ponse dans un fichier Markdown dans un dossier de documentation.

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
   Le module openai est l'interface Python pour l'API OpenAI. Il est utilis� dans ce fichier pour envoyer le contenu des fichiers Python � l'API OpenAI et obtenir une r�ponse.

4. ```python 
   from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt
   ```
   Ce module importe le message par d�faut qui est envoy� � l'API OpenAI avant le contenu du fichier. Il est utilis� pour donner des instructions � l'API sur la fa�on de g�n�rer la documentation.

***
### Classes
#### Class: AutoCodebaseDocumenter 

Objectif : Cette classe est con�ue pour g�n�rer automatiquement une documentation pour une base de code en utilisant l'API OpenAI.

##### M�thodes : m�thodes de la classe
1. ```python 
   __init__(self, openai_org_id, openai_api_key, root_path=".", output_docs_folder_name="docs", ignore_folders=["venv",".git","tests"], is_ignore_gitignore = True, file_types=[".py"], unwanted_files=None, skip_existing=False, gpt_model="gpt-3.5-turbo", language='en')
   ```
   Initialise la classe avec les param�tres n�cessaires pour g�n�rer la documentation. 
   
   ##### Variables:
   - self.root_path : Le chemin du r�pertoire racine o� se trouvent les fichiers � documenter.
   - self.output_docs_folder_name : Le nom du dossier o� la documentation sera �crite.
   - self.ignore_folders : Les dossiers � ignorer lors de la recherche de fichiers � documenter.
   - self.is_ignore_gitignore : Si vrai, les fichiers sp�cifi�s dans le fichier .gitignore seront ignor�s.
   - self.file_types : Les types de fichiers � documenter.
   - self.unwanted_files : Les fichiers sp�cifiques � ignorer lors de la documentation.
   - self.skip_existing : Si vrai, les fichiers de documentation existants ne seront pas �cras�s.
   - self.gpt_model : Le mod�le OpenAI � utiliser pour g�n�rer la documentation.
   - self.docs_dir : Le chemin du r�pertoire o� la documentation sera �crite.
   - self.system_message : Le message syst�me � envoyer � l'API OpenAI avant le contenu du fichier.
   
2. ```python 
   _get_completion(self, prompt)
   ```
   Envoie le contenu du fichier � l'API OpenAI et obtient une r�ponse. Le param�tre `prompt` est le contenu du fichier � documenter.

3. ```python 
   _get_file_paths(self)
   ```
   Obtient une liste de tous les fichiers � documenter en parcourant le r�pertoire racine et en ignorant les dossiers et fichiers sp�cifi�s.

4. ```python 
   _process_file(self, file_path)
   ```
   Traite un seul fichier en envoyant son contenu � l'API OpenAI, en obtenant une r�ponse et en �crivant cette r�ponse dans un fichier de documentation. Le param�tre `file_path` est le chemin du fichier � documenter.

5. ```python 
   process_all_files(self)
   ```
   Traite tous les fichiers � documenter en appelant la m�thode `_process_file` sur chaque fichier.

6. ```python 
   process_single_file(self, file_path)
   ```
   Cette m�thode est pr�vue pour traiter un seul fichier, mais elle n'est pas encore impl�ment�e. Le param�tre `file_path` serait le chemin du fichier � documenter.

***
### M�thodes:  
Il n'y a pas de m�thodes en dehors de la classe dans ce fichier.

***
### Variables:
Il n'y a pas de variables globales en dehors des fonctions et des classes dans ce fichier.
