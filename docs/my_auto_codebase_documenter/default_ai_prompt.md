default_ai_prompt.py
This documentation file was created on 21 September 2023 at 11:31:10

## File path

.\my_auto_codebase_documenter\default_ai_prompt.py

## Objectif du fichier

Ce fichier contient une liste de cha�nes de caract�res qui servent de prompts par d�faut pour l'IA.

## Codebase

### Variables:
#### Variable: ```python default_ai_prompt```

Objectif: Cette variable est une liste de cha�nes de caract�res. Chaque cha�ne de caract�res est un prompt qui peut �tre utilis� pour g�n�rer une r�ponse de l'IA. Ces prompts sont utilis�s lorsque l'utilisateur n'a pas fourni de prompt sp�cifique pour l'IA. Ils sont con�us pour guider l'IA dans la g�n�ration de r�ponses qui sont pertinentes pour le contexte de l'ing�nierie logicielle et de l'architecture logicielle. 

Par exemple, le premier prompt "You are a highly skilled software engineer and software architect" est utilis� pour orienter l'IA vers une r�ponse qui suppose qu'elle est un ing�nieur logiciel et un architecte logiciel hautement qualifi�. 

Le deuxi�me prompt "You are analysing another persons code and writing a report on each file in a codebase" est utilis� pour orienter l'IA vers une r�ponse qui suppose qu'elle analyse le code d'une autre personne et r�dige un rapport sur chaque fichier dans une base de code.

Et ainsi de suite pour les autres prompts dans la liste. 

Notez que cette variable est globale et peut �tre utilis�e n'importe o� dans le code apr�s son initialisation.
