from packages.extras.file_operations import openFolder
from tkinter import Menu

from ..menusclasses.menu_classes import File
from ..extras.utilities import getIcon

def createFileMenu(janela, Caixa, menu):
    menuDoArquivo = Menu(menu, tearoff=0)
    arquivo = File(janela, Caixa)

    menuDoArquivo.add_command(
        label="New", command=arquivo.new, accelerator="Ctrl+N")
    menuDoArquivo.add_command(
        label="Open...", command=arquivo.open, accelerator="Ctrl+O")
    menuDoArquivo.add_command(
        label="Open folder", command=lambda: openFolder(janela), accelerator="Ctrl+Shift+O")
    menuDoArquivo.add_command(
        label="Save", command=arquivo.save, accelerator="Ctrl+S")
    menuDoArquivo.add_command(
        label="Save as...", command=arquivo.saveAs, accelerator="Ctrl+Shift+S")

    menuDoArquivo.add_separator()
    menuDoArquivo.add_command(
        label="Exit", command=arquivo.onClosing, accelerator="Alt+F4")
    menu.add_cascade(label="File", menu=menuDoArquivo)
    janela.config(menu=menu)
