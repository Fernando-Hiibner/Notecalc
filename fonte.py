from tkinter.font import Font, families
#Importação bibliotecas adcionais#
from ast import literal_eval
from zipfile import ZipFile
#Importação das bibliotecas do sistema para salvar e abrir arquivos#
from os import mkdir, listdir, startfile
from os.path import expanduser, join
from pathlib import Path
import globais




def main():
	user = expanduser("~")
	caminho = join(user, "Documents", "Notecalc")
	caminhoconfig = join(caminho, "Config.txt")
	with open(caminhoconfig, "r", encoding='utf-8') as lerconfig:
		texto = lerconfig.read()
		texto = literal_eval(texto)
		for par, e, valor in texto:
		    if par == "fonte":
		        globais.fontp = valor
		    elif par == "fontesize":
		        globais.fontsp = int(valor)
		lerconfig.close()
	font = Font(family = globais.fontp, size = globais.fontsp)
	return font