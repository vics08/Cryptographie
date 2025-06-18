# SubstitutionCypher1.py

import random

def generate_dkey(key):
	dkey = {}
	for c in key:
		dkey[key[c]] = c
	return dkey

def generate_key():
	"""
	generate_key()
	Fonction qui génère une clé pour le chiffrement
	On ne passe aucun paramètre, car nous allons utiliser
	une fonction aléatoire pour la générer.

	Paramètres:
	aucun
	
	Return
	Dictionnaire : la clé de mappage
	"""
	
	# Lettres utilisées pour le mappage
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	# Une liste de nos lettres pour utiliser avec
	# la partie aléatoire.
	cletters = list(letters)
	
	# La clé est toujours un dictionnaire
	key = {}
	
	# Nous allons faire un mappage, mais plus intelligent.
	# Nous allons utiliser un mappage plus aléatoire.
	# Pour chaque lettre, nous allons utiliser une autre
	# lettre aléatoire de la liste cletters
	
	for c in letters:
		key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
	return key

def encrypt(key, message):
	"""
	encrypt(key, message)
	Fonction qui chiffre le message.
	
	Paramètres :
	key (dict): clé de mappage.
	message (string): mesage à chiffrer
	
	Return :
	string : le message chiffré
	
	"""
	
	# Va contenir le message chiffré
	secret = ""
	
	# Vous devez créer une boucle for qui vérifie si le
	# caractère est dans
	# dans la clé de mappage. Si oui, on le substitue. Sinon,
	# on le remet tel quel.
	for c in message:
		# On mappe seulement les caractères
		# de notre alphabète
		if c in key:
			secret += key[c]
		else:
			secret += c
	return secret

# Vérifions que notre clé est bien générée
key = generate_key()
print(key)

# Vérifions que le chiffrement fonctionne
message = "AINSI VA LA VIE"
secret = encrypt(key, message)
print(secret)

dkey = generate_dkey(key)
message = encrypt(dkey, secret)
print (message)