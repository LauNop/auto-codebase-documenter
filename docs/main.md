main.py
This documentation file was created on 21 September 2023 at 09:16:30

## File path

.\main.py

## Objectif du fichier

Ce fichier est utilisé pour récupérer tous les fichiers Python (`.py`) dans un répertoire donné et ses sous-répertoires, tout en ignorant certains fichiers et répertoires spécifiés.

## Codebase

### Imports: 

1. ```python 
   import os
   ```
   Le module `os` en Python fournit des fonctions pour interagir avec le système d'exploitation. Dans ce fichier, il est utilisé pour manipuler les chemins de fichiers et parcourir les répertoires.

2. ```python 
   import fnmatch
   ```
   Le module `fnmatch` est utilisé pour comparer les noms de fichiers avec des motifs de type glob. Cependant, il semble qu'il ne soit pas utilisé dans ce fichier.

***

### Méthodes:  

#### Méthode: forward_slash_to_backslash(input_string)

Objectif: Cette méthode remplace tous les slashes (/) par des backslashes (\/) dans une chaîne de caractères donnée.

#### Méthode: get_files(root_dir, ignore_list=[], unwanted_file=[])

Objectif: Cette méthode récupère tous les fichiers Python dans le répertoire racine et ses sous-répertoires, tout en ignorant les fichiers et répertoires spécifiés dans `ignore_list` et `unwanted_file`. Elle utilise également le fichier `.gitignore` pour obtenir une liste de motifs à ignorer.

***

### Variables:

#### Variable: root_directory

Objectif: Cette variable est utilisée pour spécifier le répertoire racine à partir duquel la recherche de fichiers doit commencer.

#### Variable: additional_ignore_patterns

Objectif: Cette variable est utilisée pour spécifier des motifs supplémentaires à ignorer lors de la recherche de fichiers. Les répertoires ou fichiers correspondant à ces motifs seront ignorés.

#### Variable: unwanted_file

Objectif: Cette variable est utilisée pour spécifier des fichiers spécifiques à ignorer lors de la recherche de fichiers. Ces fichiers seront ignorés même s'ils correspondent au type de fichier recherché (`.py`).

#### Variable: files

Objectif: Cette variable stocke la liste des fichiers récupérés par la méthode `get_files()`.
