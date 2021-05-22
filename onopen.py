from sys import argv
from ast import literal_eval
from tkinter.font import Font
def abrir(janela, Caixa, dirabrir):
	#torna a variavel que vai conter o diretório do arquivo que você vai abrir global#
	#Com esse código abrirá uma janela do explorer para o usuario selecionar o arquivo que quer abrir#        
	#Código responsavel por pegar o diretório obtido no código de cima, ler o arquivo de texto, limpar a caixa atual e passar o novo texto para ela#
	try:
		with open(dirabrir, 'r', encoding='utf-8') as aberto:
			Caixa.delete('1.0','end')
			texto = aberto.read()
			if dirabrir.endswith(".nxc"):
				textop1 = literal_eval(texto)
				final = ""
				for (key, value, index) in textop1:
					if key == "text":
						final += value
				Caixa.insert('1.0',final)
				for (key, value, index) in textop1:
					if key == "tagon":
						indexcomecodetag = index
					elif key == "tagoff":
						if value == "bt":
							Caixa.tag_add("bt", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("bt", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "bold"))
						elif value == "it":
							Caixa.tag_add("it", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("it", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "italic"))
						elif value == "tit":
							Caixa.tag_add("tit", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("tit", font=(fontcaixa.cget("family"), fontcaixa.cget("size")+4, "bold"))
						elif value == "stit":
							Caixa.tag_add("stit", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("stit", font=(fontcaixa.cget("family"),fontcaixa.cget("size")+2, "italic"))
						elif value == "un":
							Caixa.tag_add("un", f"{indexcomecodetag}",f"{index}")
							fontcaixaun = Font(Caixa, Caixa.cget("font"))
							fontcaixaun.configure(underline=1)
							Caixa.tag_config("un", font=fontcaixaun)
						elif value == "tc":
							Caixa.tag_add("tc", f"{indexcomecodetag}",f"{index}")
							fontcaixatc = Font(Caixa, Caixa.cget("font"))
							fontcaixatc.configure(overstrike =1)
							Caixa.tag_config("tc", font=fontcaixatc)
						elif value.startswith("#"):
							Caixa.tag_add(f"{value}", f"{indexcomecodetag}",f"{index}")
							fontecaixacor = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config(f"{value}", font=(fontecaixacor))
							Caixa.tag_config(f"{value}", foreground = f"{value}")
			else:
				Caixa.insert('1.0',texto)
			aberto.close()
	except:
		with open(dirabrir, 'r') as aberto:
			Caixa.delete('1.0','end')
			texto = aberto.read()
			if dirabrir.endswith(".nxc"):
				textop1 = literal_eval(texto)
				final = ""
				for (key, value, index) in textop1:
					if key == "text":
						final += value
				Caixa.insert('1.0',final)
				for (key, value, index) in textop1:
					if key == "tagon":
						indexcomecodetag = index
					elif key == "tagoff":
						if value == "bt":
							Caixa.tag_add("bt", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("bt", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "bold"))
						elif value == "it":
							Caixa.tag_add("it", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("it", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "italic"))
						elif value == "tit":
							Caixa.tag_add("tit", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("tit", font=(fontcaixa.cget("family"), fontcaixa.cget("size")+4, "bold"))
						elif value == "stit":
							Caixa.tag_add("stit", f"{indexcomecodetag}", f"{index}")
							fontcaixa = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config("stit", font=(fontcaixa.cget("family"),fontcaixa.cget("size")+2, "italic"))
						elif value == "un":
							Caixa.tag_add("un", f"{indexcomecodetag}",f"{index}")
							fontcaixaun = Font(Caixa, Caixa.cget("font"))
							fontcaixaun.configure(underline=1)
							Caixa.tag_config("un", font=fontcaixaun)
						elif value == "tc":
							Caixa.tag_add("tc", f"{indexcomecodetag}",f"{index}")
							fontcaixatc = Font(Caixa, Caixa.cget("font"))
							fontcaixatc.configure(overstrike =1)
							Caixa.tag_config("tc", font=fontcaixatc)
						elif value.startswith("#"):
							Caixa.tag_add(f"{value}", f"{indexcomecodetag}",f"{index}")
							fontecaixacor = Font(Caixa, Caixa.cget("font"))
							Caixa.tag_config(f"{value}", font=(fontecaixacor))
							Caixa.tag_config(f"{value}", foreground = f"{value}")
			else:
				Caixa.insert('1.0',texto)
			aberto.close()