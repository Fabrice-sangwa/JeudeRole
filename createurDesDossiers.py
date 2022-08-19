from pathlib import Path

chemin = Path.cwd()

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Fcrrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key, value in d.items():
    for i in value:
        chemin = Path.cwd()/key/i
        chemin.mkdir(exist_ok=True, parents = True)
