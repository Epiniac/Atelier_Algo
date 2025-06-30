# Exercice : construire un histogramme des lettres sans utiliser de fonctions Python prêtes à l'emploi.

histogramme = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}

# Les lettres majuscules compteront comme des lettres minuscule, exemple : A = a. À vous de les convertirs
# De même pour les caractères spéciaux, exemple : à = a

texte =" Une étude publiée en juin 2024 par des chercheurs de l’Université d’Aix-Marseille, a évalué chez l’animal, l’impact sur le cerveau d’une exposition prénatale au CBD. Plus spécifiquement, ces travaux ont porté sur une région cérébrale, le cortex insulaire, impliquée dans la régulation des émotions et la perception de la douleur. Cette étude montre, chez la souris, que l’exposition prénatale au CBD modifie les propriétés des neurones de cette région cérébrale. Les chercheurs soulignent les effets délétères potentiels sur le développement et le fonctionnement du cerveau chez l’homme et qui pourraient augmenter le risque de développement de troubles psychiatriques après la naissance (anxiété, dépression, schizophrénie…). Une autre étude , publiée en juin 2023 et menée par des chercheurs du Colorado aux Etats-Unis, conclut à une perturbation du développement neurologique et du comportement après la naissance chez des progénitures de souris exposées au CBD. Ces travaux appellent donc à une vigilance quant aux potentielles conséquences à long terme, notamment sur le développement cérébral, pour les individus ayant été exposé au CBD in-utero."

#Bonus : J'ai un PDF dans le dossier extra... (Indice : pdfplumber ou PyPDF2)

if __name__ == "__main__":
    pass