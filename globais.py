from os import getcwd
from sys import argv
import fonte as fo
class globais():
	global lock, saindo, abertoop, abertocalc, abertopomo, abertoconfig
	lock = False
	saindo = False
	abertoop = False
	abertopomo = False
	abertocalc = False
	abertoconfig = False
	global localabrir, ultimovalido
	try:
		localabrir = argv[1]
		ultimovalido = argv[1]
	except:
		localabrir = None
		ultimovalido = None
	global user, caminho, caminhoconfig
	user = None
	caminho = None
	caminhoconfig = None
	#---------------------------------#
	global anterior
	anterior = None
	global font, fontp, fontsp, LabelSalvar
	fontp = None
	fontsp = None
	LabelSalvar = None
	global salvou, cor2
	salvou = True
	cor2 = None
	global icon, sample
	icon = None
	sample = None
	#---------------------------------#
	global salvarautoafter
	salvarautoafter = None
	#---------------------------------#
	global darkmode, vsc, darkm, vscm
	darkmode = None
	vsc = None
	#---------------------------------#
	global temapadrao, vscpadrao, salvarautopadrao, fontepadrao, fontesizepadrao
	temapadrao = None
	vscpadrao = None
	salvarautopadrao = None
	fontepadrao = None
	fontesizepadrao = None

