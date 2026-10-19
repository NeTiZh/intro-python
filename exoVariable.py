#--------------------------------------------------------exo 1--------------------------------------------------------
# Faire une phrase dynamique (dynamique = avec des données changeante)
# "Je suis {PRENOM}, j'habite a {VILLE} et j'ai {AGE}."
# prenom, ville et âge seront dans des variables
name = "Dylan"
city = "Bordeaux"
age = 29

print(f"Je suis {name}, j'habite à {city} et j'ai {age}.")

#--------------------------------------------------------exo 2--------------------------------------------------------
# print une phrase le total est de {TOTAL} euros.
# vous avez acheté une baguette et un croissant
# le montant de ces articles sont dans des variables
baguette = 1
croissant = 2
total = baguette + croissant

print(f"Le total est de {total} euros.")

#--------------------------------------------------------exo 3--------------------------------------------------------
# Lors d'un jeu vous avez dix points
# Faire un print de vos points 
# Au premier tour vous perdez 1 pts
# au deuxieme tour vous en gagnez 5
# au dernier tour vous en perdez la moitié
# faire un print de votre nouveau total de points a chaque tours
points = 10

print(f"Vous avez {points} points.")

points -= 1

print(f"Vous avez perdu 1 point au premier tour , il vous reste {points} points.")

points += 5

print(f"Vous avez gagner 5 points au deuxième tour, vous avez maintenant {points} points.")

perte = points // 2
points -= perte

print(f"Vous avez perdu {perte} points au dernier tour, il vous reste {points} points.")