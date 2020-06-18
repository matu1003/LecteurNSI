from playsound import playsound
import epitran
import time




sons = {
	"f": "f.m4a",   #Fin
	"p": "p.m4a",   #Pain
	"t": "t.m4a",   #Teint
	"d": "d.m4a",   #Daim
	"v": "v.m4a",   #Vin
	"b": "b.m4a",   #Bain
	"m": "m.m4a",   #Main
	"n": "n.m4a",   #Nain
	"s": "s.m4a",   #Saint
	"ch": "ch.m4a", #Chimpanzes
	"k": "k.m4a", 	#Quint
	"z": "z.m4a", 	#Zinc
	"g": "g.m4a", 	#Geint
	"gu": "gu.m4a", #Gain
	"ng": "ng.m4a", #Parking
	"y": "y.m4a",	#Yaourt
	"l": "l.m4a",	#Lin
	"r": "r.m4a", 	#Rein
	"gn": "gn.m4a",	#Vigne, Panier
	"i": "i.m4a",	#Lit
	"a": "a.m4a",	#Patte
	"u": "u.m4a",	#Lu
	"in": "in.m4a", #Frein
	"è": "aie.m4a", #J'aie
	"é": "et.m4a",	#Ré
	"e": "e.m4a",	#Jeune
	"oa": "oa.m4a",	#Moi
	"o^": "ofer.m4a",	#Paume
	"o": "o.m4a",	#Pomme
	"en": "en.m4a",	#Doucement
}

def pron_sounds(mes_sons):
	mes_sons = [sons[i] for i in mes_sons]
	for son in mes_sons:
		playsound(son)


pron_sounds(["l", "u", "k", "a"])
time.sleep(0.25)
pron_sounds(["è", "t", "in", "b", "o", "s"])
# pron_sounds(["m", "a", "t", "u", "r", "in"])
# pron_sounds(["g", "è", "r", "é", "u", "s", "i"])
# pron_sounds(["a", "t", "e", "f", "è", "r", "e", "d", "i", "r", "e", "n", "in", "p", "o", "r", "t", "e", "k", "oa"])

epi = epitran.Epitran("IPA")






