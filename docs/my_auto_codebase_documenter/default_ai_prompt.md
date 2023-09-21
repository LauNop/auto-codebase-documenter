default_ai_prompt.py
This documentation file was created on 21 September 2023 at 11:31:10

## File path

.\my_auto_codebase_documenter\default_ai_prompt.py

## Objectif du fichier

Ce fichier contient une liste de chaînes de caractères qui servent de prompts par défaut pour l'IA.

## Codebase

### Variables:
#### Variable: ```python default_ai_prompt```

Objectif: Cette variable est une liste de chaînes de caractères. Chaque chaîne de caractères est un prompt qui peut être utilisé pour générer une réponse de l'IA. Ces prompts sont utilisés lorsque l'utilisateur n'a pas fourni de prompt spécifique pour l'IA. Ils sont conçus pour guider l'IA dans la génération de réponses qui sont pertinentes pour le contexte de l'ingénierie logicielle et de l'architecture logicielle. 

Par exemple, le premier prompt "You are a highly skilled software engineer and software architect" est utilisé pour orienter l'IA vers une réponse qui suppose qu'elle est un ingénieur logiciel et un architecte logiciel hautement qualifié. 

Le deuxième prompt "You are analysing another persons code and writing a report on each file in a codebase" est utilisé pour orienter l'IA vers une réponse qui suppose qu'elle analyse le code d'une autre personne et rédige un rapport sur chaque fichier dans une base de code.

Et ainsi de suite pour les autres prompts dans la liste. 

Notez que cette variable est globale et peut être utilisée n'importe où dans le code après son initialisation.
