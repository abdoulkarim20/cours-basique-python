#Comment declaraer une fonction: Pour declarer une fonction on utilise def: 
#Le nom d'une fonction doit respecter les normes en snak case (ma_fonction)
#Si un bloc de code ne contient aucune instruction vous pouvez juste mettre le mot cle "pass
# Une indentation représente un ou plusieurs espaces au début d'une ligne de code.
# Il est recommandé avec Python d'indenter son code avec 4 espaces (équivalent à 1 tabulation).
def dire_bonjour_a():
    print("Bonjour ma femme j'espere tu as bien dormi")
print(dire_bonjour_a())
#Fonction nommer
def dire_bonjour_a_une_personne(nom):
    print("Votre nom est: ",nom)
#Les valeurs de retours
def cree_nom_complet(nom:str,prenom:str,age:int):
    resultat=prenom+" "+nom
    print("Votre nom complet est: ",resultat,"Et votre age est :",age)

cree_nom_complet(prenom="Abdoul Karim",nom="DIALLO",age=21)

#Une fonction qui calcul le TVA en fonction d'un Pays
def calcul_taux_tv_par_pay(tva:float,prix_vente:float):
    return tva*prix_vente
print("Le taux de tva pour le senegal est: ",calcul_taux_tv_par_pay(0.18,5000))
#Une fonction qui permet de convertir une chaine miniscule en majuscule
def convertir_text_majuscule(message:str):
    return message.upper() +" "+message.lower()
result=input("Entrer un texte je vais le convertir en majuscule ")
print("Voici votre texte en majuscule",convertir_text_majuscule(result))
from sys import version

print("La version sont: ",version)