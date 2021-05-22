from tkinter import *
from tkinter.simpledialog import askstring
class Editar():
	def copiar(self):
	    self.janela.clipboard_clear()
	    tcopiar = self.Caixa.selection_get()
	    self.janela.clipboard_append(tcopiar)
	def cortar(self):
	    self.janela.clipboard_clear()
	    tcortar = self.Caixa.selection_get()
	    self.janela.clipboard_append(tcortar)
	    self.Caixa.delete("sel.first", "sel.last")
	def colar(self):
	    self.Caixa.insert("insert", self.janela.clipboard_get())
	def undo(self):
	    self.Caixa.edit_undo()
	def redo(self):
	    self.Caixa.edit_redo()
	def selecionar_tudo(self):
	    self.Caixa.tag_add(SEL, "1.0", END)
	    self.Caixa.mark_set(0.0, END)
	    self.Caixa.see(INSERT)
	def tirarselecao(self):
	    self.Caixa.tag_remove(SEL,"1.0",END)
	    self.Caixa.tag_remove("Encontrado", "1.0", END)
	def encontrar(self):
	    self.Caixa.tag_remove("Encontrado", "1.0", END)
	    palavrae = askstring("Encontrar", "Econtrar palavra:")
	    if palavrae:
	        index = "1.0"
	        while 1:
	            index = self.Caixa.search(palavrae, index, nocase=1, stopindex=END)
	            if not index: break
	            ultindex = f"{index}"+f"{len(palavrae)}"
	            self.Caixa.tag_add("Encontrado", index, ultindex)
	            index = ultindex
	            self.Caixa.mark_set(INSERT,ultindex)
	        self.Caixa.tag_config("Encontrado", foreground = "white", background = "blue")
	        self.Caixa.see(INSERT)

	def __init__(self,janela,Caixa):
		self.Caixa = Caixa
		self.janela = janela
		self.janela.clipboard_clear()
		self.janela.bind("<Control-Z>", lambda event: self.redo())
		self.janela.bind("<Control-f>", lambda event: self.encontrar())


def main(janela,Caixa,menuc):
	editar = Menu(menuc, tearoff=0)
	tela = Editar(janela,Caixa)
	editar.add_command(label="Desfazer", command=tela.undo, accelerator="Ctrl+Z")
	editar.add_command(label="Refazer", command=tela.redo, accelerator="Ctrl+Shift+Z")
	editar.add_separator()
	editar.add_command(label="Cortar", command = tela.cortar, accelerator="Ctrl+X")
	editar.add_command(label="Copiar", command = tela.copiar, accelerator="Ctrl+C")
	editar.add_command(label="Colar", command = tela.colar, accelerator="Ctrl+V")
	editar.add_command(label="Selecionar Tudo", command=tela.selecionar_tudo, accelerator="Ctrl+A")
	editar.add_separator()
	editar.add_command(label="Econtrar...", command=tela.encontrar,accelerator="Ctrl+F")
	Caixa.bind("<Button-1>", lambda event: tela.tirarselecao())
	menuc.add_cascade(label = "Editar",menu=editar)
	janela.config(menu=menuc)