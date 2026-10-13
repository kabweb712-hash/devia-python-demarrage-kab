
"""
# Variables et affichages

prix_unitaire = 12
quantite = 3
total = prix_unitaire * quantite
print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)


prix_unitaire = 7
quantite = 5
total = prix_unitaire * quantite
print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)

## Contrôle
prix_unitaire = 7
quantite = 10
total = prix_unitaire * quantite
print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)

## Défi
prix_unitaire = 12
quantite = 3
frais_fixes = 4
total = prix_unitaire * quantite + frais_fixes
print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Frais Fixes :", frais_fixes)
print("Total :", total)


prix_unitaire = 7
quantite = 5
frais_fixes = 4
total = prix_unitaire * quantite + frais_fixes
print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Frais Fixes :", frais_fixes)
print("Total :", total)

"""
"""
# Conditions

prix_unitaire = 12
quantite = 4
frais_livraison = 4

sous_total = prix_unitaire * quantite

if sous_total >= 50 :
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", 0)
    print("Total :", sous_total)
else :
    total = sous_total + frais_livraison
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", frais_livraison)
    print("Total :", total)

## Défi
prix_unitaire = 10
quantite = 5
frais_livraison = 4

total = prix_unitaire * quantite

if sous_total >= 50 :
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", 0)
    print("Total :", sous_total)
else :
    total = sous_total + frais_livraison
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", frais_livraison)
    print("Total :", total)


prix_unitaire = 7
quantite = 8
frais_livraison = 4

total = prix_unitaire * quantite

if sous_total >= 50 :
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", 0)
    print("Total :", sous_total)
else :
    total = sous_total + frais_livraison
    print("Prix unitaire :", prix_unitaire)
    print("Quantité :", quantite)
    print("Sous-Total :", sous_total)
    print("Frais livraion :", frais_livraison)
    print("Total :", total)

# Contrôle
#### Quand le total article = 50, les frais de livraions ne s'appliquent plus. Ils s'appliquent jusqu'a 49
"""


# Boucles 

prix_unitaire = 12
frais_livraison = 4
for quantite in range(1,6) :
    sous_total = prix_unitaire * quantite
    if sous_total < 50 :
        total = sous_total + frais_livraison
        print("Prix unitaire :", prix_unitaire)
        print("Quantité :", quantite)
        print("Sous-Total :", sous_total)
        print("Frais livraion :", frais_livraison)
        print("Total :", total)
    else : 
        print("Prix unitaire :", prix_unitaire)
        print("Quantité :", quantite)
        print("Sous-Total :", sous_total)
        print("Frais livraion :", 0)
        print("Total :", sous_total)
    print("=" * 50)

## Défi : livraison offerte 1 panier

prix_unitaire = 12
frais_livraison = 4
for quantite in range(1,9) :
    sous_total = prix_unitaire * quantite
    if sous_total < 50 :
        total = sous_total + frais_livraison
        print("Prix unitaire :", prix_unitaire)
        print("Quantité :", quantite)
        print("Sous-Total :", sous_total)
        print("Frais livraion :", frais_livraison)
        print("Total :", total)
    else : 
        print("Prix unitaire :", prix_unitaire)
        print("Quantité :", quantite)
        print("Sous-Total :", sous_total)
        print("Frais livraion :", 0)
        print("Total :", sous_total)
    print("=" * 50)

## Défi : livraison offerte pour 4 paniers