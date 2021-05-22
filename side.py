from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
from tkinter.font import Font, families
from ast import literal_eval
from os import listdir, getcwd, chdir
from sys import argv
from os.path import join, isdir, basename, dirname, expanduser
from pathlib import Path
import globais


class Funcside():
	def abrir(janela, Caixa):
		#torna a variavel que vai conter o diretório do arquivo que você vai abrir global#
		#Com esse código abrirá uma janela do explorer para o usuario selecionar o arquivo que quer abrir#        
		#Código responsavel por pegar o diretório obtido no código de cima, ler o arquivo de texto, limpar a caixa atual e passar o novo texto para ela#
		try:
			with open(globais.localabrir, 'r', encoding='utf-8') as aberto:
				Caixa.delete('1.0','end')
				texto = aberto.read()
				if globais.localabrir.endswith(".nxc"):
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
				globais.salvou = True
				aberto.close()
		except:
			with open(globais.localabrir, 'r') as aberto:
				Caixa.delete('1.0','end')
				texto = aberto.read()
				if globais.localabrir.endswith(".nxc"):
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
				globais.salvou = True
				aberto.close()
	def salvar(janela,Caixa):
		#Código que tenta salvar o arquivo rapidamente no local que ele ja conhece(proveniente tanto do Salvar como, quanto do Abrir)#
		if globais.localabrir == '' or globais.localabrir == None or not str(globais.localabrir.endswith(".nxc")) or not str(globais.localabrir.endswith(".txt")) or not str(globais.localabrir.endswith(".py")):
			Funcside.saveas(janela,Caixa)
		else:
			try:
				textonormal = Caixa.get('1.0', 'end-1c')
				texto = str(Caixa.dump("1.0", "end"))
				with open(globais.localabrir, 'a+', encoding='utf-8') as salvar:
					salvar.truncate(0)
					if globais.localabrir.endswith(".nxc"):
						salvar.write(texto)
					else:
						salvar.write(textonormal)
					salvar.close()
			#Código que ele executa caso não consiga, ele automaticamente executa o código de salvar como#
			except NameError:
				print("Caiu no nameError")
				globais.localabrir = ''
				Funcside.saveas(janela,Caixa)
		globais.salvou = True
		
	#inicia a definição responsável pelo salvar como#
	def saveas(janela,Caixa):
		#Com esse código abrirá uma janela do explorer para o usuario selecionar o diretorio onde quer salvar o arquivo e o nome dele#
		saveast = filedialog.asksaveasfilename(parent=janela, title='Selecione o local onde quer salvar o arquivo', defaultextension = ("*.nxc"),filetypes = (("Documentos Notecalc (*.nxc)","*.nxc"),("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
		texto = str(Caixa.dump("1.0", "end"))
		textonormal = Caixa.get('1.0', 'end-1c')
		globais.localabrir = saveast
		#Código responsavel por pegar o diretório obtido no código de cima e salvar o arquivo nele, com o nome especificado#
		with open(saveast, 'a+', encoding='utf-8') as saveasf:
			saveasf.truncate(0)
			if globais.localabrir[-4:] == ".nxc":
				saveasf.write(texto)
			else:
				saveasf.write(textonormal)
			saveasf.close()
		globais.salvou = True

def main(janela):
	try:
		chdir(dirname(argv[1]))
		globais.localabrir = argv[1]
	except:
		diretorioPadrao = expanduser('~')
		chdir(diretorioPadrao)
	Bloco = PanedWindow(relief = FLAT, bg = "#1e1e1e", borderwidth = 0)
	Bloco.pack(fill=BOTH, expand = 1)
	Scroll = Scrollbar(Bloco, orient = VERTICAL)
	def selecionado(evento):
		w = evento.widget
		index = int(w.curselection()[0])
		valor = w.get(index)
		if valor == "^":
			cwdparente = Path(getcwd())
			cwdparente = cwdparente.parent
			globais.ultimovalido = cwdparente
			chdir(globais.ultimovalido)
			Side.delete(0,END)
			lerdir(Side,globais.ultimovalido)
		elif valor.startswith("   >"):
			valor = valor[4::]
			globais.ultimovalido = join(getcwd(), valor)
			chdir(globais.ultimovalido)
			Side.delete(0,END)
			lerdir(Side,globais.ultimovalido)
		elif not valor.startswith("   >") and index != 1:
			valor = valor[4::]
			if globais.localabrir != join(getcwd(), valor):
				if globais.salvou == False:
					salvarpergunta = askyesno("Salvar", "Você deseja salvar antes de trocar de arquivo")
					if salvarpergunta == True:
						try:
							Funcside.salvar(janela, Caixa)
							globais.localabrir = join(getcwd(), valor)
							Funcside.abrir(janela, Caixa)
						except Exception as e:
							#if str(e).startswith("[Errno 13]"):
							erro = askyesno("Erro", f'Não foi possivel salvar.\nErro: {e}\nDeseja sair sem salvar?')
					elif salvarpergunta == False:
						globais.localabrir = join(getcwd(), valor)
						Funcside.abrir(janela, Caixa)
				elif globais.salvou == True:
					globais.localabrir = join(getcwd(), valor)
					Funcside.abrir(janela, Caixa)
	def side():
		Side = Listbox(Bloco, bg = "#252526", relief = FLAT, bd = 0,
						 highlightthickness = 0, foreground = "#cccccc",
						 selectbackground = "#3e3e3e")
		Side.config(activestyle='none')
		sidefonte = Font(family = "Courier New", size = "10")
		Side.config(font=sidefonte)
		Side.bind('<<ListboxSelect>>', selecionado)
		return Side
	Side = side()
	def lerdir(Side, dir):
		Side.insert(0, "^")
		Side.insert(1, "v "+basename(getcwd()))
		for i in listdir(dir):
			if isdir(join(getcwd(),i)):
				i = "   >"+i
				Side.insert(END, i)
		for i in listdir(dir):
			if not isdir(join(getcwd(),i)) and i.endswith("py") or i.endswith("txt") or i.endswith("nxc"):
				i = "    "+i
				Side.insert(END,i)
		Side.config(width = 25)
	lerdir(Side, getcwd())
	def atualizar():
		Side.delete(0,"end")
		lerdir(Side, getcwd())
		janela.after(200, atualizar)
	atualizar()
	Bloco.add(Side)
	Bloco2 = PanedWindow(Bloco, relief = FLAT, bg = "#1e1e1e", borderwidth = 0)
	Bloco.add(Bloco2)
	Caixa = ScrolledText(Bloco2, tabs = ('1c'), selectbackground = "#185abc", selectforeground = "white", relief = FLAT, undo = True, autoseparators = True)#declara a caixa de texto do bloco de notas#
	Caixa.pack(fill=BOTH, expand = 1)#posiciona a caixa de texto#
	return Caixa, Side, Bloco, Bloco2
