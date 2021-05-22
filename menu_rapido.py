from tkinter import *
from tkinter import ttk
import menu_editar as me
import menu_formatar as mf


class Main():
    def __init__(self, janela, Caixa):
        self.janela = janela
        self.Caixa = Caixa
        self.menurap = Menu(self.janela, tearoff=0)

        def popup(event):
            try:
                self.menurap.tk_popup(event.x_root, event.y_root)
            finally:
                self.menurap.grab_release()
        self.menurap.add_command(label="Título", command=lambda self=self: mf.Formatar.titulo(
            self), accelerator="Ctrl+Shift+T")
        self.menurap.add_command(label="Subtítulo", command=lambda self=self: mf.Formatar.subtit(
            self), accelerator="Alt+Shift+T")
        self.menurap.add_command(label="Negrito", command=lambda self=self: mf.Formatar.bold(
            self), accelerator="Ctrl+Shift+B")
        self.menurap.add_command(label="Itálico", command=lambda self=self: mf.Formatar.italic(
            self), accelerator="Ctrl+Shift+I")
        self.menurap.add_command(label="Sublinhado", command=lambda self=self: mf.Formatar.un(
            self), accelerator="Ctrl+Shift+-")
        self.menurap.add_command(
            label="Tachado", command=lambda self=self: mf.Formatar.tc(self))
        self.menurap.add_separator()
        self.menurap.add_command(
            label="Escolher Cor", command=lambda self=self: mf.Formatar.escolhercor(self))
        self.menurap.add_command(label="Cor anterior", command=lambda self=self: mf.Formatar.aplicarcor(
            self), accelerator="Ctrl+Shift+C")
        coresori, coresdark = mf.Formatar.menuvsc(self, self.menurap)
        self.menurap.add_cascade(label="Cores VSC(Original)", menu=coresori)
        self.menurap.add_cascade(label="Cores VSC(Escuro)", menu=coresdark)
        self.menurap.add_separator()
        self.menurap.add_command(label="Copiar", command=lambda self=self: me.Editar.copiar(
            self), accelerator="Ctrl+C")
        self.menurap.add_command(label="Colar", command=lambda self=self: me.Editar.colar(
            self), accelerator="Ctrl+V")
        self.menurap.add_command(label="Cortar", command=lambda self=self: me.Editar.cortar(
            self), accelerator="Ctrl+X")
        self.Caixa.bind("<Button-3>", popup)
