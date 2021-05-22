from tkinter.messagebox import showinfo

def main(janela,menuc):
	def ajuda():
	    showinfo("Ajuda", "Um simples editor de texto feito em Python\nFeito por:\nFernando Hiibner | Renan Kawamoto\nContate-nos via Codigo-Aberto@hotmail.com\nNotecalc 3.1.5 Beta")
	menuc.add_command(label = "Ajuda", command=ajuda)
	janela.config(menu=menuc)