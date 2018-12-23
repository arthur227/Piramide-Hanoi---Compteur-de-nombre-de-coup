nb_disque_max = 16 #Changer la variable selon ce que l'on veut  comme nombre max de disques
t = 1 #Nombre de coup minimal
nb_disque = 1
print("Pour " + str(nb_disque) + " disque(s)" + ", le nombre de coups minimum est égal à " + str(t))
while nb_disque != nb_disque_max:
    t = (2*t)+1
    nb_disque +=1
    print("Pour " + str(nb_disque) + " disque(s)" + ", le nombre de coups minimum est égal à " + str(t))
