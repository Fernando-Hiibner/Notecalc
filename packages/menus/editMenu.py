from tkinter import Menu

from ..menusclasses.menu_classes import Edit


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
