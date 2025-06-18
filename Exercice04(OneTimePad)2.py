import random

def generate_key_stream(n):
	"""
	generate_key_stream(n)
	Génère une clé aléatoire pour le chiffrement
	
	Paramètres:
	n (int) : la longueur de la clé
	
	Return:
	Une clé aléatoire d'octets (valeur binaire)
	"""
	
	return bytes([random.randrange(0, 256) for i in range(n)])

def xor_bytes(key_stream, texte):
	"""
	xor_bytes(key_stream, texte)
	Fait un XOR d'une clé aléatoire avec un texte
	
	Paramètres:
	key_stream (int) : clé aléatoire
	texte () : texte à faire un XOR
	
	Return:
	Texte chiffré ou déchiffré
	"""
	
	# Prends la longueur minimale entre les deux paramètres
	# La clé et le texte doivent être de la même longueur,
	# sinon on utilise le plus court des deux.
	length = min(len(key_stream), len(texte))
	# Le texte est traité octet par octet et retourne en octets
	return bytes([key_stream[i] ^ texte[i] for i in range(length)])


#############################################################


# Message de notre ennemi.
message = "UNE ATTAQUE"

# Le message doit être binaire.
message = message.encode()

# Générer une clé aléatoire. La clé doit être la longueur du message (description du One Time PAD).
key_stream = generate_key_stream(len(message))

#Génère le texte chiffré.
secret = xor_bytes(key_stream, message)


#############################################################


# L'équipe 1 essaie avec le texte en clair PAS ATTAQUE
message = "PAS ATTAQUE"

# Le message doit être binaire.
message = message.encode()

# On essaie de générer une clé en utilisant le message chiffré
# et notre texte. Si la clé peut déchiffrer le message
# original, nous avons gagné. Vraiment ?
guess_key_stream = xor_bytes(message, secret)
print("La clé de chiffrement 1 : ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 1 : ", plain_text)


#############################################################


# L'équipe 2 essaie avec le texte en clair DES SURPRIS
message = "DES SURPRIS"

# Le message doit être binaire.
message = message.encode()

# On essaie de générer une clé en utilisant le message chiffré
# et notre texte. Si la clé peut déchiffrer le message
# original, nous avons gagné. Vraiment ?
guess_key_stream = xor_bytes(message, secret)
print("La clé de chiffrement 2 : ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 2 : ", plain_text)