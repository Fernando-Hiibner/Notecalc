from tkinter import *
from tkinter import ttk
from tkinter.font import Font, families
from tkinter.colorchooser import askcolor
import globais


class Formatar():
	def removbold(self, *args):
	    self.Caixa.tag_remove("bt", "sel.first", "sel.last")
	def removtit(self, *args):
	    self.Caixa.tag_remove("tit", "sel.first", "sel.last")
	def removstit(self, *args):
	    self.Caixa.tag_remove("stit", "sel.first", "sel.last")
	def removit(self, *args):
	    self.Caixa.tag_remove("it", "sel.first", "sel.last")
	def removun(self, *args):
	    self.Caixa.tag_remove("un", "sel.first", "sel.last")
	def removtc(self, *args):
	    self.Caixa.tag_remove("tc", "sel.first", "sel.last")
	def removcolor(self, *args):
		tags = self.Caixa.tag_names("sel.first")
		for tag in tags:
			if tag.startswith("#"):
				self.Caixa.tag_remove(tag, "sel.first", "sel.last")
	def escolhercor(self, *args):
		(cor, globais.cor2) = askcolor()
		if globais.cor2 == None:
			if globais.darkmode == False:
				globais.cor2 = '#000000'
			elif globais.darkmode == True:
				globais.cor2 = '#cccccc'
		Formatar.aplicarcor(self)
	def aplicarcor(self, *args):
		Formatar.removbold(self)
		Formatar.removtit(self)
		Formatar.removstit(self)
		Formatar.removit(self)
		Formatar.removun(self)
		Formatar.removtc(self)
		Formatar.removcolor(self)
		if globais.cor2:
			self.Caixa.tag_add(f"{globais.cor2}", "sel.first", "sel.last")
			fontcaixacor = Font(self.Caixa, self.Caixa.cget("font"))
			self.Caixa.tag_config(f"{globais.cor2}", font=fontcaixacor)
			self.Caixa.tag_config(f"{globais.cor2}", foreground = f"{globais.cor2}")
		elif globais.cor2 == None:
			Formatar.escolhercor(self)
	def bold(self, *args):
		try:
			Formatar.removtit(self)
			Formatar.removstit(self)
			Formatar.removit(self)
			Formatar.removun(self)
			Formatar.removtc(self)
			Formatar.removcolor(self)
			tags = self.Caixa.tag_names("sel.first")
			if "bt" not in tags:
			    self.Caixa.tag_add("bt", "sel.first", "sel.last")
			    fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
			    self.Caixa.tag_config("bt", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "bold"))
			elif "bt" in tags:
			    Formatar.removbold(self)
		except:
			pass
	def italic(self, *args):
	    try:
	        Formatar.removbold(self)
	        Formatar.removtit(self)
	        Formatar.removstit(self)
	        Formatar.removun(self)
	        Formatar.removtc(self)
	        Formatar.removcolor(self)
	        tags = self.Caixa.tag_names("sel.first")
	        if "it" not in tags:
	            self.Caixa.tag_add("it", "sel.first", "sel.last")
	            fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
	            self.Caixa.tag_config("it", font=(fontcaixa.cget("family"), fontcaixa.cget("size"), "italic"))
	        elif "it" in tags:
	            Formatar.removit(self)
	    except:
	        pass
	def titulo(self, *args):
	    try:
	        Formatar.removbold(self)
	        Formatar.removit(self)
	        Formatar.removstit(self)
	        Formatar.removun(self)
	        Formatar.removtc(self)
	        Formatar.removcolor(self)
	        tags = self.Caixa.tag_names("sel.first")
	        if "tit" not in tags:
	            self.Caixa.tag_add("tit", "sel.first", "sel.last")
	            fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
	            self.Caixa.tag_config("tit", font=(fontcaixa.cget("family"), fontcaixa.cget("size")+4, "bold"))
	        elif "tit" in tags:
	            Formatar.removtit(self)
	    except:
	        pass
	def subtit(self, *args):
	    try:
	        Formatar.removbold(self)
	        Formatar.removit(self)
	        Formatar.removtit(self)
	        Formatar.removun(self)
	        Formatar.removtc(self)
	        Formatar.removcolor(self)
	        tags = self.Caixa.tag_names("sel.first")
	        if "stit" not in tags:
	            self.Caixa.tag_add("stit", "sel.first", "sel.last")
	            fontcaixa = Font(self.Caixa, self.Caixa.cget("font"))
	            self.Caixa.tag_config("stit", font=(fontcaixa.cget("family"),fontcaixa.cget("size")+2, "italic"))
	        elif "stit" in tags:
	            Formatar.removstit(self)
	    except:
	        pass
	def un(self, *args):
	    try:
	        Formatar.removtit(self)
	        Formatar.removstit(self)
	        Formatar.removit(self)
	        Formatar.removbold(self)
	        Formatar.removtc(self)
	        Formatar.removcolor(self)
	        tags = self.Caixa.tag_names("sel.first")
	        if "un" not in tags:
	            self.Caixa.tag_add("un", "sel.first", "sel.last")
	            fontcaixaun = Font(self.Caixa, self.Caixa.cget("font"))
	            fontcaixaun.configure(underline=1)
	            self.Caixa.tag_config("un", font=fontcaixaun)
	        elif "un" in tags:
	            Formatar.removun(self)
	    except:
	        pass
	def tc(self, *args):
	    try:
	        Formatar.removtit(self)
	        Formatar.removstit(self)
	        Formatar.removit(self)
	        Formatar.removbold(self)
	        Formatar.removun(self)
	        Formatar.removcolor(self)
	        tags = self.Caixa.tag_names("sel.first")
	        if "tc" not in tags:
	            self.Caixa.tag_add("tc", "sel.first", "sel.last")
	            fontcaixatc = Font(self.Caixa, self.Caixa.cget("font"))
	            fontcaixatc.configure(overstrike =1)
	            self.Caixa.tag_config("tc", font=fontcaixatc)
	        elif "tc" in tags:
	            Formatar.removtc(self)
	    except:
	        pass

	def corVsc(self,cor2):
		globais.cor2 = cor2
		Formatar.aplicarcor(self)
	def menuvsc(self, formatar):
		coresori = Menu(formatar, tearoff=0)
		coresdark = Menu(formatar, tearoff=0)
		coresvscori = ["Titulo(Original)#af00db","Subtítulo(Original)#0000ff","Negrito(Original)#ce8349","Italico(Original)#008000","Sublinhado(Original)#267e99","Tachado(Original)#a31515"]
		coresvscdark = ["Titulo(Escuro)#b96fb4","Subtítulo(Escuro)#499cb3","Negrito(Escuro)#ce8349","Italico(Escuro)#6a9955","Sublinhado(Escuro)#3ac9a3","Tachado(Escuro)#dcdcaa"]
		for cor in coresvscori:
			coresori.add_command(label = cor[:-7], command = lambda cor = cor: Formatar.corVsc(self,cor[-7:]))
		for cor in coresvscdark:
			coresdark.add_command(label = cor[:-7], command = lambda cor = cor: Formatar.corVsc(self,cor[-7:]))
		return coresori, coresdark

	def __init__(self,janela,Caixa):
		self.janela = janela
		self.Caixa = Caixa
		self.janela.bind("<Control-T>", lambda event: self.titulo())
		self.janela.bind("<Alt-T>", lambda event: self.subtit())
		self.janela.bind("<Control-B>", lambda event: self.bold())
		self.janela.bind("<Control-I>", lambda event: self.italic())
		self.janela.bind("<Control-_>", lambda event: self.un())
		self.janela.bind("<Control-C>", lambda event: self.aplicarcor())
		#----------------------------------------------------------------#
		self.janela.bind("<Alt-t>", lambda event: self.titulo())
		self.janela.bind("<Alt-s>", lambda event: self.subtit())
		self.janela.bind("<Alt-b>", lambda event: self.bold())
		self.janela.bind("<Alt-i>", lambda event: self.italic())
		self.janela.bind("<Alt-_>", lambda event: self.un())
		self.janela.bind("<Alt-c>", lambda event: self.aplicarcor())


def main(font,janela,Caixa,menuc):
	formatar = Menu(menuc, tearoff=0)
	tela = Formatar(janela,Caixa)
	formatar.add_command(label="Titulo", command=tela.titulo, accelerator = "Ctrl+Shift+T")
	formatar.add_command(label="Subtítulo", command=tela.subtit, accelerator = "Alt+Shift+T")
	formatar.add_command(label="Negrito", command=tela.bold, accelerator = "Crtl+Shift+B")
	formatar.add_command(label="Italico", command=tela.italic, accelerator = "Ctrl+Shift+I")
	formatar.add_command(label="Sublinhado", command=tela.un, accelerator = "Ctrl+Shift+-")
	formatar.add_command(label="Tachado", command=tela.tc)
	formatar.add_separator()
	formatar.add_command(label="Ecolher Cor", command=tela.escolhercor)
	formatar.add_command(label="Cor anterior", command = tela.aplicarcor, accelerator = "Ctrl+Shift+C")
	coresori, coresdark = tela.menuvsc(formatar)
	formatar.add_cascade(label="Cores VSC(Original)", menu = coresori)
	formatar.add_cascade(label="Cores VSC(Escuro)", menu = coresdark)
	#Font Selector#

	menuc.add_cascade(label = "Formatar", menu=formatar)
	janela.config(menu=menuc)