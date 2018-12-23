compteur_egal = 16 #Changer la variable selon ce que l'on veut  comme nombre max de disques
t = 1 
compteur = 1
while compteur != compteur_egal:
    t = (2*t)+1
    compteur +=1
    print("Le compteur est égal a " + str(compteur) + ", t est égal à " + str(t))
