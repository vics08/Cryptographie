import random

class KeyStream:
	"""
	Classe KeyStream
	Classe pour générer un flux de clés
	"""
	def __init__(self, key=1):
		"""
		init (self, key=1)
		Initialise l'objet clé
		
		Paramètres:
		self : notre objet flux de clé
		key (int) : la clé partagée,
		elle est à 1 par défaut
		
		Return
		Notre objet KeyStream
		"""
		
		# Initialise l'objet à la clé
		self.next = key
	
	def rand(self):
		"""
		rand(self)
		Calcul la valeur aléatoire
		
		Paramètres:
		self : notre objet flux de clés

		Return:
		self.next (int) : la prochaine valeur aléatoire
		"""
		
		# L'équation pour notre LCG
		# Xnext+1 = (a*Xnext + c) mod m
		self.next = (1103515245 * self.next + 12345) % 2**31
		return self.next
		
	def get_key_byte(self):
		"""
		get_key_byte(self)
		Crée le flux de clé
		
		Paramètres:
		self : notre objet flux de clé
		
		Return:
		Retourne une clé aléatoire d’un caractère (le mod 256)
		"""
		
		return self.rand() % 256

########################################################

# Notre objet clé de flux
#key = KeyStream()

# On génère une série de clés
# pour notre flux
#for i in range(10):
#	print(key.get_key_byte())
	
########################################################

def encryptDecrypt(key, message):
	"""
	encryptDecrypt(key, message)
	Chiffre le message
	
	Paramètres
	key (objet KeyStream): flux de clés
	message (bytes): message à chiffrer
	
	Return:
	(bytes) : message chiffré
	"""
	
	# On fait un XOR avec chacun des caractères du message
	# Une nouvelle clé est générée à chaque caractère
	return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

########################################################

def transmit(secret, tauxErreurs):
	"""
	transmit(secret, tauxErreurs)
	Fonction qui simule des erreurs de transmission.
	On passe le message octet par octet et de
	temps en temps on flip un bit selon le tauxErreur passé.
	
	Paramètres :
	secret (bytes) : le message qui est transmis
	tauxErreurs () : le niveau d'erreur qu'on veut insérer dans le message
	
	Return :
	(bytes) : le message avec des erreurs
	"""
	
	# Contiens le message modifié
	b = []
	
	# On passe chaque octet du message et
	# l'ajoute à b
	for c in secret:
		# Selon notre taux d'erreur, on
		# flip un bit dans l'octet
		if random.randrange(0, tauxErreurs) == 0:
			#
			c = c ^ 2**random.randrange(0, 8)
			b.append(c)
	return bytes(b)


def modification(secret):
	"""
	modification(secret)
	Fonction qui modifie certains octets du message,
	sans la clé
	Nous allons flipper des bits, mais pas
	n'importe quels bits, ceux en notre faveur
	
	Paramètres :
	secret (bytes) : le message secret

	Return :
	(bytes) : le message secret modifié
	"""
	
	# On créer une liste de zéro de la même
	# longueur que le secret
	mod = [0] * len(secret)
	mod[18] = ord(' ') ^ ord('1')
	mod[19] = ord(' ') ^ ord('0')
	mod[20] = ord('1') ^ ord('0')
	# On fait la même opération que pour chiffrer
	return bytes([mod[i] ^ secret[i] for i in range(len(secret))])


def get_key(message, secret):
	"""
	get_key(message, secret)
	Génère un flux de clés à partir d'un message en texte clair
	et d'un message chiffré
	
	Paramètres :
	message (bytes) : message en clair
	secret (bytes) : message chiffré
	
	Return :
	(bytes) : flux de clés
	"""
	
	# Fait un XOR octet par octet
	return bytes([message[i] ^ secret[i] for i in range(len(secret))])

def crack(key_stream, secret):
	"""
	crack(key_stream, secret)
	Fonction qui utilise un flux de clés pour déchiffrer
	le message chiffré.
	
	Paramètres :
	key_stream (bytes) : le flux de clés
	secret (bytes) : le message chiffré
	
	Return :
	
	"""
	
	# On ne peut déchiffrer plus que la longueur
	# du flux de clés ou de la longueur du
	# message. On recherche le plus petit
	length = min(len(key_stream), len(secret))
	
	# On refait toujours la même chose :)
	return bytes([key_stream[i] ^ secret[i] for i in range(length)])

# Eve donne un message à Alice
message_Eve = "Ceci est un message super hyper important".encode()

# Alice communique Avec Bob
cle_secret = 33
print("La clé secrète entre Alice et Bob : ", cle_secret)
key = KeyStream(cle_secret)
header = "MESSAGE: "
message = header + "Un message secret vers Bob"
message = message.encode()
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)

# Voilà Bob
key = KeyStream(cle_secret)
message = encryptDecrypt(key, secret)
print("Bob : ", message)


def brute_force(plain, secret):
	"""
	brute_force(plain, cipher)
	Fonction qui trouve une clé secrète par force brute.
	
	Paramètres :
	plain (bytes) : Une partie de texte en clair connu.
	secret (bytes) : le texte chiffré.
	
	Return
	(bytes) : la clé secrète commune
	"""
	
	# On veut faire une attaque force brute.
	# On doit essayer toutes les clés possibles.
	for key in range(2**31):
		# On se crée un flux de clés possible
		bf_key = KeyStream(key)
		
		# On vérifie si le texte connut XOR avec le texte chiffré
		# retourne une clé secrète égale à notre clé.
		# Sinon, on sort et essaie un autre flux de clé.
		# Si oui, on retourne la clé.
		# Au premier caractère qui ne fonctionne pas, on sort.
		# On vérifie tout le texte clair, même si
		# une clé fonctionne. Au cas où un octet serait bon
		# mais pas le suivant, donc mauvaise clé.
		for i in range(len(plain)):
			xor_value = plain[i] ^ secret[i]
			if xor_value != bf_key.get_key_byte():
				break
			else:
				return key
		
	# Si toutes les clés ne fonctionnent pas, Bummer!
	return False

# Encore Eve qui veut notre message secret
#Interception du message chiffré
bf_key = brute_force(header.encode(), secret)
print("La clé force brute d'Eve : ", bf_key)
key = KeyStream(bf_key)
message = encryptDecrypt(key, secret)
print("Eve : ", message)