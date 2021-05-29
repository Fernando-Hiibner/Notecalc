from tkinter import *

from ..menusclasses.menu_classes import Format
from ..extras import globals



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
