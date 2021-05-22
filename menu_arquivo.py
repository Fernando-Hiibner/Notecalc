from tkinter import *
from tkinter import filedialog
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesnocancel, showinfo, askyesno
from tkinter.font import Font, families
from ast import literal_eval
from os import chdir, getcwd
from os.path import basename
import globais

class Arquivo():
	def novo(self):
		self.Caixa.delete('1.0','end')
		globais.localabrir = ''
	def abrir(self):
		#torna a variavel que vai conter o diretório do arquivo que você vai abrir global#
		#Com esse código abrirá uma janela do explorer para o usuario selecionar o arquivo que quer abrir#
		globais.localabrir = filedialog.askopenfilename(parent=self.janela,title='Selecione o arquivo que você quer abrir',filetypes = (("Documentos Notecalc (*.nxc)","*.nxc"),("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
		#Código responsavel por pegar o diretório obtido no código de cima, ler o arquivo de texto, limpar a caixa atual e passar o novo texto para ela#
		try:
			with open(globais.localabrir, 'r', encoding='utf-8') as aberto:
				self.Caixa.delete('1.0','end')
				texto = aberto.read()
				if globais.localabrir[-4:] == ".nxc":
					textop1 = literal_eval(texto)
					final = ""
					for (key, value, index) in textop1:
						if key == "text":
							final += value
					self.Caixa.insert('1.0',final)
					for (key, value, index) in textop1:
						if key == "tagon":
							indexcomecodetag = index
						elif key == "tagoff":
							if value == "bt":
								self.Caixa.tag_add("bt", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("bt", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "bold"))
							elif value == "it":
								self.Caixa.tag_add("it", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("it", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "italic"))
							elif value == "tit":
								self.Caixa.tag_add("tit", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("tit", font=(fontcaixa.cget("family"), fontcaixa.cget("size")+4, "bold"))
							elif value == "stit":
								self.Caixa.tag_add("stit", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("stit", font=(fontcaixa.cget("family"),fontcaixa.cget("size")+2, "italic"))
							elif value == "un":
								self.Caixa.tag_add("un", f"{indexcomecodetag}",f"{index}")
								fontcaixaun = Font(self.Caixa, self.Caixa.cget("font"))
								fontcaixaun.configure(underline=1)
								self.Caixa.tag_config("un", font=fontcaixaun)
							elif value == "tc":
								self.Caixa.tag_add("tc", f"{indexcomecodetag}",f"{index}")
								fontcaixatc = Font(self.Caixa, self.Caixa.cget("font"))
								fontcaixatc.configure(overstrike =1)
								self.Caixa.tag_config("tc", font=fontcaixatc)
							elif value.startswith("#"):
								self.Caixa.tag_add(f"{value}", f"{indexcomecodetag}",f"{index}")
								fontecaixacor = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config(f"{value}", font=(fontecaixacor))
								self.Caixa.tag_config(f"{value}", foreground = f"{value}")
				else:
						self.Caixa.insert('1.0',texto)
				globais.salvou = True
				aberto.close()
		except:
			with open(globais.localabrir, 'r') as aberto:
				self.Caixa.delete('1.0','end')
				texto = aberto.read()
				if globais.localabrir[-4:] == ".nxc":
					textop1 = literal_eval(texto)
					final = ""
					for (key, value, index) in textop1:
						if key == "text":
							final += value
					self.Caixa.insert('1.0',final)
					for (key, value, index) in textop1:
						if key == "tagon":
							indexcomecodetag = index
						elif key == "tagoff":
							if value == "bt":
								self.Caixa.tag_add("bt", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("bt", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "bold"))
							elif value == "it":
								self.Caixa.tag_add("it", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("it", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "italic"))
							elif value == "tit":
								self.Caixa.tag_add("tit", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("tit", font=(fontcaixa.cget("family"), fontcaixa.cget("size")+4, "bold"))
							elif value == "stit":
								self.Caixa.tag_add("stit", f"{indexcomecodetag}", f"{index}")
								fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config("stit", font=(fontcaixa.cget("family"),fontcaixa.cget("size")+2, "italic"))
							elif value == "un":
								self.Caixa.tag_add("un", f"{indexcomecodetag}",f"{index}")
								fontcaixaun = Font(self.Caixa, self.Caixa.cget("font"))
								fontcaixaun.configure(underline=1)
								self.Caixa.tag_config("un", font=fontcaixaun)
							elif value == "tc":
								self.Caixa.tag_add("tc", f"{indexcomecodetag}",f"{index}")
								fontcaixatc = Font(self.Caixa, self.Caixa.cget("font"))
								fontcaixatc.configure(overstrike =1)
								self.Caixa.tag_config("tc", font=fontcaixatc)
							elif value.startswith("#"):
								self.Caixa.tag_add(f"{value}", f"{indexcomecodetag}",f"{index}")
								fontecaixacor = Font(self.Caixa, self.Caixa.cget("font"))
								self.Caixa.tag_config(f"{value}", font=(fontecaixacor))
								self.Caixa.tag_config(f"{value}", foreground = f"{value}")
				else:
						self.Caixa.insert('1.0',texto)
				globais.salvou = True
				aberto.close()
	def abrirpasta(self):
		chdir(filedialog.askdirectory(parent = self.janela, title = "Escolha uma pasta...", initialdir = getcwd()))
	#Inicia a definição responsavel pelo salvamento rápido de um documento de texto sendo feito no Notecalc#
	def salvar(self):
		#Código que tenta salvar o arquivo rapidamente no local que ele ja conhece(proveniente tanto do Salvar como, quanto do Abrir)#
		if globais.localabrir == '' or globais.localabrir == None or not str(globais.localabrir.endswith(".nxc")) or not str(globais.localabrir.endswith(".txt")) or not str(globais.localabrir.endswith(".py")):
			self.saveas()
		else:
			try:
				textonormal = self.Caixa.get('1.0', 'end-1c')
				texto = str(self.Caixa.dump("1.0", "end"))
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
				self.saveas()
		globais.salvou = True
		
	#inicia a definição responsável pelo salvar como#
	def saveas(self):
		#Com esse código abrirá uma janela do explorer para o usuario selecionar o diretorio onde quer salvar o arquivo e o nome dele#
		self.saveast = filedialog.asksaveasfilename(parent=self.janela, title='Selecione o local onde quer salvar o arquivo', defaultextension = ("*.nxc"),filetypes = (("Documentos Notecalc (*.nxc)","*.nxc"),("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
		texto = str(self.Caixa.dump("1.0", "end"))
		textonormal = self.Caixa.get('1.0', 'end-1c')
		globais.localabrir = self.saveast
		#Código responsavel por pegar o diretório obtido no código de cima e salvar o arquivo nele, com o nome especificado#
		with open(self.saveast, 'a+', encoding='utf-8') as saveasf:
			saveasf.truncate(0)
			if globais.localabrir[-4:] == ".nxc":
				saveasf.write(texto)
			else:
				saveasf.write(textonormal)
			saveasf.close()
		globais.salvou = True
	def on_closing(self):
		if globais.salvou == False:
			self.sair = askyesnocancel("Sair", "Você deseja salvar antes de sair?")
			if self.sair == True:
				self.saindo = True
				try:
					self.salvar()
					self.janela.destroy()
				except Exception as e:
					self.erro = askyesno("Erro", f'Não foi possivel salvar.\nErro: {e}\nDeseja sair sem salvar?')
					if self.erro == True:
						self.janela.destroy()
			elif self.sair ==  False:
				self.janela.destroy()
			else:
				pass
		elif globais.salvou == True:
			self.janela.destroy()
	def modificou(self):
		globais.salvou = False
	def __init__(self,janela,Caixa):
		if globais.localabrir == None:
			globais.localabrir = ""
		self.janela = janela
		self.Caixa = Caixa
		self.Caixa.bind("<Key>", lambda event: self.modificou())
		self.Caixa.bind("<<Selection>>", lambda event: self.modificou())
		self.janela.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.janela.bind("<Control-s>", lambda event: self.salvar())
		self.janela.bind("<Control-o>", lambda event: self.abrir())
		self.janela.bind("<Control-O>", lambda event: self.abrirpasta())
		self.janela.bind("<Control-n>", lambda event: self.novo())
		self.janela.bind("<Control-S>", lambda event: self.saveas())
		
def main(janela,Caixa,menuc):
	arquivo = Menu(menuc, tearoff=0)
	tela = Arquivo(janela, Caixa)
	arquivo.add_command(label = "Novo", command=tela.novo, accelerator = "Ctrl+N")
	arquivo.add_command(label = "Abrir...", command=tela.abrir, accelerator = "Ctrl+O")
	arquivo.add_command(label = "Abrir pasta", command = tela.abrirpasta, accelerator = "Ctrl+Shift+O")
	arquivo.add_command(label = "Salvar", command=tela.salvar, accelerator = "Ctrl+S")
	arquivo.add_command(label = "Salvar como...", command=tela.saveas, accelerator = "Ctrl+Shift+S")
	arquivo.add_separator()
	arquivo.add_command(label="Sair", command=tela.on_closing, accelerator = "Alt+F4")
	menuc.add_cascade(label = "Arquivo", menu=arquivo)
	janela.config(menu=menuc)