from tkinter import Menu
from ..menusclasses.menu_classes import Format, Edit
from ..extras import globals


class FastMenu():
    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.fastMenu = Menu(self.root, tearoff=0)

        def popup(event):
            try:
                self.fastMenu.tk_popup(event.x_root, event.y_root)
            finally:
                self.fastMenu.grab_release()
                
        self.fastMenu.add_command(
        label="Title", command=lambda: Format(self.root, self.text).addTags(tag = "title", size = 4, sizeMod= True), accelerator="Alt+T")

        self.fastMenu.add_command(
            label="Subtitle", command=lambda: Format(self.root, self.text).addTags(tag = "subtitle", size = 2, sizeMod= True), accelerator="Alt+S")

        self.fastMenu.add_command(
            label="Bold", command=lambda: Format(self.root, self.text).addTags(tag = "bold"), accelerator="Alt+B")

        self.fastMenu.add_command(
            label="Italic", command=lambda: Format(self.root, self.text).addTags(tag = "italic"), accelerator="Alt+I")

        self.fastMenu.add_command(
            label="Underline", command=lambda: Format(self.root, self.text).addTags(tag = "underline"), accelerator="Alt+Shift+-")

        self.fastMenu.add_command(label="Overstrike", command=lambda: Format(self.root, self.text).addTags(tag = "overstrike"))

        self.fastMenu.add_command(label="Remove tags", command=lambda: Format(self.root, self.text).addTags(tag = "remove"), accelerator="Alt+R")

        self.fastMenu.add_separator()
        
        self.fastMenu.add_command(
            label="Choose Color", command=lambda: Format(self.root, self.text).changeColor())

        self.fastMenu.add_command(
            label="Last Color", command=lambda: Format(self.root, self.text).changeColor(), accelerator="Alt+C")

        #SubMenu
        self.predefinedColors = Menu(self.fastMenu, tearoff = 0)
        for name, color in globals.colorConfig.items():
            self.predefinedColors.add_command(label = name.capitalize(), command=lambda color = color: Format(self.root, self.text).changeColor(cor = color))
        self.fastMenu.add_cascade(label = "Predefined Colors", menu = self.predefinedColors)

        self.fastMenu.add_separator()
        self.simbolsMenu = Menu(self.fastMenu, tearoff=0)
        for category, simbols in globals.simbols.items():
            self.categoryMenu = Menu(self.simbolsMenu, tearoff = 0)
            for simbol in simbols:
                self.categoryMenu.add_command(label = simbol, command=lambda simbol = simbol: Format(self.root, self.text).insertSimbols(simbol))
            self.simbolsMenu.add_cascade(label = category, menu = self.categoryMenu)
        self.fastMenu.add_cascade(
            label="Simbols", menu=self.simbolsMenu)
        
        self.fastMenu.add_separator()
        self.fastMenu.add_command(label = "Calculate Selection", command=lambda: self.calculate())

        self.text.bind("<Button-3>", popup)

        self.fastMenu.add_separator()
        self.fastMenu.add_command(
            label="Cut", command=lambda: Edit(self.root, self.text).cut(), accelerator="Ctrl+X")
        self.fastMenu.add_command(
            label="Copy", command=lambda: Edit(self.root, self.text).copy(), accelerator="Ctrl+C")
        self.fastMenu.add_command(
            label="Paste", command=lambda: Edit(self.root, self.text).paste(), accelerator="Ctrl+V")
    def calculate(self):
        try:
            calculus = eval(self.text.get("sel.first", "sel.last"))
            self.text.insert("sel.last", " ==> ("+str(calculus)+")")
        except:
            self.text.insert("sel.last", " ==> (Invalid Operation)")
