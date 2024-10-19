import os

# Limpa o Terminal
os.system("cls || clear")

# Não embaralha o terminal

import random
atrizes= ["Adriana Prado," "Bárbara Borges", "Camila Queiroz", "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi", "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]

#Embaralha elementos
random.shuffle(atrizes)
print(atrizes)

#Ordena elementos crescente
atrizes.sort()
print(atrizes)

#Ordena elementos descrescente
atrizes.sort(reverse= True)
print(atrizes)

