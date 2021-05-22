
from os.path import expanduser, join
from tkinter import *
from os import listdir, startfile, path
import globais
import calc
import pomo

class Outros():
	def chamarcalc():
	    if globais.abertocalc == False:
	        calc.calculadora()
	    elif globais.abertocalc == True:
	        pass
	def chamarpomo():
	    if globais.abertopomo == False:
	        pomo.pomodoro()
	    elif globais.abertopomo == True:
	        pass
	def inserirstigma(self,stig):
	    self.Caixa.insert(INSERT, stig)
	def iniciarexternocalcu(self,py):
	    caminhoaabrir = join(extercalcu, py)
	    startfile(caminhoaabrir)
	def iniciarexternocod(self,py):
	    caminhoabrir = join(extercod, py)
	    startfile(caminhoabrir)
	def iniciarexternoout(self,py):
	    caminhoout = join(exterout, py)
	    startfile(caminhoout)
	def __init__(self, janela, Caixa, outros, extercalcu, extercod, exterout):
		self.janela = janela
		self.Caixa = Caixa
		self.outros = outros

def main(janela,Caixa,menuc):
	outros = Menu(menuc, tearoff=0)
	user = expanduser("~")
	caminho = join(user, "Documents", "Notecalc")
	caminhoexter = join(caminho, "externos")
	extercalcu = join(caminhoexter, "calculos")
	extercod = join(caminhoexter, "codigo")
	exterout = join(caminhoexter, "outros")
	tela = Outros(janela, Caixa, outros, extercalcu, extercod, exterout)
	#Botão outros#
	outros.add_command(label="Calculadora", command = Outros.chamarcalc)#, command=chamarcalc)
	outros.add_command(label="Pomodoro", command = Outros.chamarpomo)#, command=chamarpomo)
	externos = Menu(outros, tearoff = 0)
	calculos = Menu(externos, tearoff = 0)
	codigos = Menu(externos, tearoff = 0)
	out = Menu(externos, tearoff = 0)
	outros.add_cascade(label = "Externos", menu=externos)
	externos.add_cascade(label = "Calculos", menu=calculos)
	externos.add_cascade(label = "Código", menu=codigos)
	#Stigmas#
	externos.add_cascade(label = "Outros", menu=out)
	stigma = Menu(outros, tearoff = 0)
	stigmas = ["Ω","π","≠","≅","α","∈","∋","∉","∌","∆","∪","∩","⋃","⊂","⊃","⊄","⊅","⊆","⊇","⊊","⊉","≥","≤","∅","∀","∑"]
	for stig in stigmas:
	    stigma.add_command(label=stig, command = lambda stig = stig: tela.inserirstigma(stig))
	outros.add_cascade(label="Ω", underline=0, menu=stigma)
	for py in listdir(extercalcu):
	    if py[-3:] == ".py":
	        calculos.add_command(label = py, command = lambda py = py: tela.iniciarexternocalcu(py))
	for py in listdir(extercod):
	    if py[-3:] == ".py":
	        codigos.add_command(label = py, command = lambda py = py: tela.iniciarexternocod(py))
	for py in listdir(exterout):
	    if py[-3:] == ".py":
	        out.add_command(label = py, command = lambda py = py: tela.iniciarexternoout(py))
	menuc.add_cascade(label = "Outros", menu=outros)
	janela.config(menu=menuc)