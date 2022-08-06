# Quizz de maths contenant des calculs générés aléatoirement
# Nombres compris entre NB_MIN et NB_MAX. Opérations choisies entre '+', '-' et '*'

import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4
score = 0
print("Quizz de math !")
for i in range (0, NB_QUESTIONS):
	print(f"Question n° {i+1} sur {NB_QUESTIONS} :")
	nbr1 = random.randint(NB_MIN, NB_MAX)
	nbr2 = random.randint(NB_MIN, NB_MAX)
	nb_ops = random.randint(1, 3)
	if nb_ops == 1:			# Signe +
		sol = nbr1 + nbr2
		print(f"{nbr1} + {nbr2} = ?")
	elif nb_ops == 2:			# Signe +
		sol = nbr1 - nbr2
		print(f"{nbr1} - {nbr2} = ?")
	else:
		sol = nbr1 * nbr2
		print(f"{nbr1} * {nbr2} = ?")
	usr_ans = int(input("Réponse : "))
	print()
	if (sol == usr_ans):
		score += 1
		print(f"Bonne réponse ! Score : {score} / {i}")
	else:
		print(f"Mauvaise réponse ! Score : {score} / {i}")
	print()
print(f"Score final : {score} / {NB_QUESTIONS}")