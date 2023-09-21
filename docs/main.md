main.py
This documentation file was created on 21 September 2023 at 09:16:30

## File path

.\main.py

## Objectif du fichier

Ce fichier est utilis� pour r�cup�rer tous les fichiers Python (`.py`) dans un r�pertoire donn� et ses sous-r�pertoires, tout en ignorant certains fichiers et r�pertoires sp�cifi�s.

## Codebase

### Imports: 

1. ```python 
   import os
   ```
   Le module `os` en Python fournit des fonctions pour interagir avec le syst�me d'exploitation. Dans ce fichier, il est utilis� pour manipuler les chemins de fichiers et parcourir les r�pertoires.

2. ```python 
   import fnmatch
   ```
   Le module `fnmatch` est utilis� pour comparer les noms de fichiers avec des motifs de type glob. Cependant, il semble qu'il ne soit pas utilis� dans ce fichier.

***

### M�thodes:  

#### M�thode: forward_slash_to_backslash(input_string)

Objectif: Cette m�thode remplace tous les slashes (/) par des backslashes (\/) dans une cha�ne de caract�res donn�e.

#### M�thode: get_files(root_dir, ignore_list=[], unwanted_file=[])

Objectif: Cette m�thode r�cup�re tous les fichiers Python dans le r�pertoire racine et ses sous-r�pertoires, tout en ignorant les fichiers et r�pertoires sp�cifi�s dans `ignore_list` et `unwanted_file`. Elle utilise �galement le fichier `.gitignore` pour obtenir une liste de motifs � ignorer.

***

### Variables:

#### Variable: root_directory

Objectif: Cette variable est utilis�e pour sp�cifier le r�pertoire racine � partir duquel la recherche de fichiers doit commencer.

#### Variable: additional_ignore_patterns

Objectif: Cette variable est utilis�e pour sp�cifier des motifs suppl�mentaires � ignorer lors de la recherche de fichiers. Les r�pertoires ou fichiers correspondant � ces motifs seront ignor�s.

#### Variable: unwanted_file

Objectif: Cette variable est utilis�e pour sp�cifier des fichiers sp�cifiques � ignorer lors de la recherche de fichiers. Ces fichiers seront ignor�s m�me s'ils correspondent au type de fichier recherch� (`.py`).

#### Variable: files

Objectif: Cette variable stocke la liste des fichiers r�cup�r�s par la m�thode `get_files()`.
