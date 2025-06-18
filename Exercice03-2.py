secret = """LRVMNIR BPR SUMVBWVR JX BPR LMIWV YJERYRKBI JX QMBM WI
BPR XJVNI MKD YMIBRUT JX IRHX WI BPR RIIRKVR JX
YMBINLMTMIPW UTN QMUMBR DJ W IPMHH BUT BJ RHNVWDMBR BPR
YJERYRKBI JX BPR QMBM MVVJUDWKO BJ YT WKBRUSURBMBWJK
LMIRD JK XJUBT TRMUI JX IBNDT
WB WI KJB MK RMIT BMIQ BJ RASHMWK RMVP YJERYRKB MKD WBI
IWOKWXWVMKVR MKD IJYR YNIB URYMWK NKRASHMWKRD BJ OWER M
VJYSHRBR RASHMKMBWJK JKR CJNHD PMER BJ LR FNMHWXWRD MKD
WKISWURD BJ INVP MK RABRKB BPMB PR VJNHD URMVP BPR IBMBR
JX RKHWOPBRKRD YWKD VMSMLHR JX URVJOKWGWKO IJNKDHRII
IJNKD MKD IPMSRHRII IPMSR W DJ KJB DRRY YTIRHX BPR XWKMH
MNBPJUWBT LNB YT RASRUWRKVR CWBP QMBM PMI HRXB KJ DJNLB
BPMB BPR XJHHJCWKO WI BPR SUJSRU MSSHWVMBWJK MKD
WKBRUSURBMBWJK W JXXRU YT BPRJUWRI WK BPR PJSR BPMB BPR
RIIRKVR JX JQWKMCMK QMUMBR CWHH URYMWK WKBMVB
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# On utilise un dictionnaire pour enregistrer
# la fréquence de nos lettres
freq = {}

# On va utiliser un compteur pour compter les lettres
# de notre alphabet dans le texte.
# On va mettre le compteur à 0 pour chacune des lettres
for c in alphabet:
	freq[c] = 0

# On doit également connaître le nombre
# de caractères dans le texte
letter_count = 0

# Nous allons compter la fréquence de chacun
# des caractères dans le texte et le
# nombre de caractères dans le texte
for c in secret:
	if c in freq:
		freq[c] += 1
		letter_count += 1

# On doit maintenant connaître le pourcentage
# d'utilisation de chacun des caractères
for c in freq:
	freq[c] = round(freq[c]/letter_count, 4)

# On imprime le résultat sur 3 colonnes
new_line_count = 0
for c in freq:
	print(c, ":", freq[c], " ", end='')
	if new_line_count % 3 == 2:
		print()
	new_line_count += 1