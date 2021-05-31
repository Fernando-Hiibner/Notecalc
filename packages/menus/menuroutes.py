
from tkinter import Menu

from ..menusclasses.menu_classes import File, Edit
from ..menusclasses.options_window import OptionsWindow

from ..extras.utilities import getIcon
from ..extras import globals

from packages.extras.file_operations import openFolder


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

def createEditMenu(root, text, menu):
    editMenu = Menu(menu, tearoff=0)
    edit = Edit(root, text)
    editMenu.add_command(
        label="Undo", command=edit.undo, accelerator="Ctrl+Z")
    editMenu.add_command(
        label="Redo", command=edit.redo, accelerator="Ctrl+Shift+Z")
    editMenu.add_separator()
    editMenu.add_command(
        label="Cut", command=edit.cut, accelerator="Ctrl+X")
    editMenu.add_command(
        label="Copy", command=edit.copy, accelerator="Ctrl+C")
    editMenu.add_command(
        label="Paste", command=edit.paste, accelerator="Ctrl+V")
    editMenu.add_command(
        label="Select All", command=edit.selectAll, accelerator="Ctrl+A")
    editMenu.add_separator()
    editMenu.add_command(
        label="Find...", command=edit.find, accelerator="Ctrl+F")
    text.bind("<Button-1>", lambda event: edit.clearSelection())
    menu.add_cascade(label="Edit", menu=editMenu)
    root.config(menu=menu)

def createFormatMenu(root, text, menu):
    formatMenu = Menu(menu, tearoff=0)
    format = text.format

    formatMenu.add_command(
        label="Title", command=lambda: format.addTags(tag="title", size = 4, sizeMod=True), accelerator="Alt+T")

    formatMenu.add_command(
        label="Subtitle", command=lambda: format.addTags(tag="subtitle", size = 2, sizeMod=True), accelerator="Alt+S")

    formatMenu.add_command(
        label="Bold", command=lambda: format.addTags(tag="bold"), accelerator="Alt+B")

    formatMenu.add_command(
        label="Italic", command=lambda: format.addTags(tag="italic"), accelerator="Alt+I")

    formatMenu.add_command(
        label="Underline", command=lambda: format.addTags(tag="underline"), accelerator="Alt+Shift+-")

    formatMenu.add_command(
        label="Overstrike", command=lambda: format.addTags(tag = "overstrike"))
    
    formatMenu.add_command(
        label = "Remove tags", command=lambda: format.addTags(tag = "remove"), accelerator="Alt+R")

    formatMenu.add_separator()

    formatMenu.add_command(
        label="Choose Color", command=format.chooseColor)

    formatMenu.add_command(
        label="Last Color", command=format.changeColor, accelerator="Alt+C")

    # SubMenu
    predefinedColors = Menu(formatMenu, tearoff=0)
    for name, hex in globals.colorConfig.items():
        predefinedColors.add_command(
            label=name.capitalize(), command=lambda hex=hex: format.changeColor(colorHex=hex))
    formatMenu.add_cascade(
        label="Predefined Colors", menu=predefinedColors)

    formatMenu.add_separator()
    simbolsMenu = Menu(formatMenu, tearoff=0)
    for category, simbols in globals.simbols.items():
        categoryMenu = Menu(simbolsMenu, tearoff=0)
        for simbol in simbols:
            categoryMenu.add_command(
                label=simbol, command=lambda simbol=simbol: format.insertSimbols(simbol))
        simbolsMenu.add_cascade(label=category, menu=categoryMenu)
    formatMenu.add_cascade(
        label="Simbols", menu=simbolsMenu)

    menu.add_cascade(label="Format", menu=formatMenu)
    root.config(menu=menu)

def createOptionsMenu(janela, menu):
    menu.add_command(label = "Options", command = lambda rootMain = janela: OptionsWindow(rootMain))
