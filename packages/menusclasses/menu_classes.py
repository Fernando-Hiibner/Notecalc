from tkinter import *
from tkinter.font import Font
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askyesnocancel, askyesno
from tkinter.filedialog import askopenfilename, asksaveasfilename

from ..extras import globals
from ..extras.file_operations import saveFile, saveFileAs, openFile, openFolder

class Format():
    def chooseColor(self, parent = None):
        if parent == None:
            parent = self.root
        (rgb, globals.hex) = askcolor(parent = parent, title = "Choose a color")
        if globals.hex == None:
            globals.hex = globals.colorConfig["default"]
        self.addTags(colorHex=globals.hex)

    def changeColor(self, colorHex=None):
        if colorHex != None:
            globals.hex = colorHex
        if globals.hex == None:
            return self.chooseColor()
        self.addTags(colorHex=globals.hex)

    def validateTags(self, tags = None):
        if tags == None:
            tags = self.text.tagsInSelection()
        for tag in tags:
            #Tag template
            #{"prefix" : None, "tags" : list(), "size" = 18, "hex" : '#cccccc'}
            formatFont = Font(self.text, self.text.cget("font"))
            tagDict = eval(tag)

            for _tag in tagDict["tags"]:
                if _tag == "bold":
                    if "title" not in tagDict["tags"]:
                        formatFont.config(weight="bold")
                    else:
                        formatFont.config(weight="normal")
                if _tag == "title":
                    if "bold" not in tagDict["tags"]:
                        formatFont.config(weight="bold")
                    else:
                        formatFont.config(weight="normal")
                if _tag == "italic":
                    if "subtitle" not in tagDict["tags"]:
                        formatFont.config(slant="italic")
                    else:
                        formatFont.config(slant="roman")
                if _tag == "subtitle":
                    if "italic" not in tagDict["tags"]:
                        formatFont.config(slant="italic")
                    else:
                        formatFont.config(slant="roman")
                if _tag == "underline":
                    formatFont.config(underline=1)
                if _tag == "overstrike":
                    formatFont.config(overstrike=1)

            size = tagDict["size"]
            formatFont.config(size=size)

            if tagDict["prefix"] == "color" or tagDict["prefix"] == None or self.vsc == False:
                self.text.tag_config(tag, font=formatFont, foreground=tagDict["hex"])
            elif tagDict["prefix"] in self.colorConfig.keys() and self.vsc:
                self.text.tag_config(tag, font=formatFont, foreground=self.colorConfig[tagDict["prefix"]])

    def createNewTag(self, tag=None, size=None, colorHex=None, sizeMod = False):
        #Tag template
        #{"prefix" : None, "tags" : list(), "size" = 18, "hex" : '#cccccc'}
        fontSize = self.font.cget("size")
        if tag == None and size == None and colorHex == None and sizeMod == False:
            return str({"prefix" : None, "tags" : [], "size" : fontSize, "hex" : self.colorConfig["default"]})
        if size == None:
            size = fontSize
            if len(str(size)) < 2:
                size = "0"+str(size)
            else:
                size = str(size)
        elif size != None and sizeMod == False:
            if len(str(size)) < 2:
                size = "0"+str(size)
            else:
                size = str(size)
        elif size != None and sizeMod == True:
            size = fontSize+size
            if len(str(size)) < 2:
                size = "0"+str(size)
            else:
                size = str(size)
        prefix = None
        if colorHex != None and colorHex not in self.colorConfig.values():
            prefix = "color"
        elif colorHex in self.colorConfig.values() and colorHex != self.colorConfig["default"] and tag == None:
            prefix = "color"
        elif colorHex in self.colorConfig.values() and colorHex != self.colorConfig["default"]:
            for key, value in self.colorConfig.items():
                if value == colorHex:
                    prefix = key
                    break
        elif self.vsc == True and colorHex == None:
            colorHex = self.colorConfig["default"]
            prefix = tag

        if colorHex == None:
            colorHex = self.colorConfig["default"]

        if tag != None:
            newTag = {"prefix" : prefix, "tags" : [tag], "size" : size, "hex" : colorHex}
        else:
            newTag = {"prefix" : prefix, "tags" : [], "size" : size, "hex" : colorHex}

        return str(newTag)

    def addTags(self, tag=None, size=None, colorHex=None, sizeMod = False):
        tagsInSel = self.text.tagsInSelection()
        if len(tagsInSel) > 0:
            for tagInSel, indexesTupleList in tagsInSel.items():
                for indexRangeTuple in indexesTupleList:
                    self.text.tag_remove(tagInSel, indexRangeTuple[0], indexRangeTuple[1])

            if tag == "remove":
                return

            newTag = self.createNewTag(tag, size, colorHex, sizeMod)
            self.text.tag_add(newTag, "sel.first", "sel.last")

            for tagInSel, indexesTupleList in tagsInSel.items():
                for indexRangeTuple in indexesTupleList:
                    #s prefix == String / f prefix == Float
                    sIndex1 = str(indexRangeTuple[0])
                    sIndex2 = str(indexRangeTuple[1])

                    tagDict = eval(tagInSel)
                    #Dealing with the font size values
                    tagSize = int(tagDict["size"])
                    fontSize = self.font.cget("size")

                    if size == None:
                        newSize = tagSize
                    elif size != None and sizeMod == False:
                        if len(str(size)) < 2:
                            newSize = "0"+str(size)
                        newSize = int(size)
                    elif size != None and sizeMod == True:
                        if fontSize+size == tagSize:
                            newSize = fontSize
                        elif fontSize+size != tagSize:
                            newSize = fontSize+size
                        if len(str(newSize)) < 2:
                            newSize = "0"+str(newSize)
                        newSize = int(newSize)

                    newTagInSel = tagDict

                    newTagInSel["size"] = newSize

                    if tag != None:
                        if tag in newTagInSel["tags"]:
                            newTagInSel["tags"].remove(tag)
                            if sizeMod:
                                newTagInSel["size"] == fontSize
                        elif tag not in newTagInSel["tags"]:
                            newTagInSel["tags"].append(tag)

                    #Acho que pra ficar suave agora so tirar a cor quando todas as tags sumiram, e caso for titulo ou sub, fazer ele tirar o size também
                    #lançar isso como uma função, e poder chamar pq tipo, quando eu tiro o subtitulo, ele perde a cor mesmo que tenha outras tags 
                    if colorHex != None and colorHex not in self.colorConfig.values():
                        newTagInSel["prefix"] = "color"
                        newTagInSel["hex"] = colorHex
                    elif colorHex != None and colorHex in self.colorConfig.values() and tag == None:
                        newTagInSel["prefix"] = "color"
                        newTagInSel["hex"] = colorHex
                    elif colorHex in self.colorConfig.values() and colorHex != self.colorConfig["default"]:
                        for key, value in self.colorConfig.items():
                            if value == colorHex:
                                newTagInSel["prefix"] = key
                                newTagInSel["hex"] = colorHex
                                break
                    elif self.vsc == True and colorHex == None and len(newTagInSel["tags"]) > 0 and newTagInSel["prefix"] != "color":
                        newTagInSel["hex"] = self.colorConfig["default"]
                        newTagInSel["prefix"] = newTagInSel["tags"][-1]
                    elif newTagInSel["prefix"] != "color":
                        newTagInSel["hex"] = self.colorConfig["default"]
                        newTagInSel["prefix"] = None

                    if str(newTagInSel) != self.createNewTag():
                        self.text.tag_remove(newTag, sIndex1, sIndex2)
                        self.text.tag_add(str(newTagInSel), sIndex1, sIndex2)
                    elif str(newTagInSel) == self.createNewTag():
                        self.text.tag_remove(newTag, sIndex1, sIndex2)

        elif tag != "remove":
            self.text.tag_add(self.createNewTag(tag, size, colorHex, sizeMod), "sel.first", "sel.last")
        self.validateTags()

    def insertSimbols(self, simbol):
        self.text.insert(INSERT, simbol)

    def __init__(self, root, text, colorDict = None, configVsc = None, font = None):
        self.root = root
        self.text = text

        if colorDict == None:
            self.colorConfig = globals.colorConfig
        else:
            self.colorConfig = colorDict
        if configVsc == None:
            self.vsc = globals.vsc
        else:
            self.vsc = configVsc
        if font == None:
            self.font = globals.font
        else:
            self.font = font

        self.root.bind(
            "<Alt-t>", lambda event: self.addTags(tag="title", size = 4, sizeMod=True))
        self.root.bind(
            "<Alt-s>", lambda event: self.addTags(tag="subtitle", size = 2, sizeMod=True))
        self.root.bind("<Alt-b>", lambda event: self.addTags(tag="bold"))
        self.root.bind("<Alt-i>", lambda event: self.addTags(tag="italic"))
        self.root.bind("<Alt-_>", lambda event: self.addTags(tag="underline"))
        self.root.bind("<Alt-r>", lambda event: self.addTags(tag="remove"))
        self.root.bind("<Alt-c>", lambda event: self.changeColor())

class File():
    def cwdForTitle(self):
        if globals.currentWorkingDirectory != None and globals.currentWorkingDirectory != "":
            return str(globals.currentWorkingDirectory)
        else:
            return ""

    def save(self):
        if(saveFile(self.text) == False):
            self.saveAs()
        else:
            self.root.title("Lolicalc "+self.cwdForTitle())

    def saveAs(self):
        saveDir = asksaveasfilename(parent=self.root, title='Choose where you want to save the file', defaultextension=(
                                    "*.nxc"), filetypes=(("Notecalc documents (*.nxc)", "*.nxc"), ("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))
        if(saveFileAs(self.text, saveDir) == True):
            self.root.title("Lolicalc "+self.cwdForTitle())

    def open(self):
        dirToOpen = askopenfilename(parent=self.root, title='Choose file to open', filetypes=(
            ("Notecalc documents (*.nxc)", "*.nxc"), ("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))

        openFile(self.root, self.text, dirToOpen)

    def new(self):
        self.text.delete('1.0', 'end')
        self.root.title("Lolicalc")
        globals.currentWorkingDirectory = ''

    def onClosing(self):
        if self.text.edit_modified() == True:
            saveAndExit = askyesnocancel(
                "Exit", "Do you want to save before exit?")
            if saveAndExit == True:
                try:
                    self.save()
                    self.root.destroy()
                except Exception as e:
                    error = askyesno(
                        "Error", f"Failed to save.\nErro: {e}\nExit without saving?")
                    if error == True:
                        self.root.destroy()
            elif saveAndExit == False:
                self.root.destroy()
            else:
                pass
        elif self.text.edit_modified() == False:
            self.root.destroy()

    def modified(self):
        if self.text.edit_modified() == True:
            self.root.title("Lolicalc * "+self.cwdForTitle())
        elif self.text.edit_modified() == False:
            self.root.title("Lolicalc "+self.cwdForTitle())
        self.root.after(200, self.modified)
    def tagAdded(self, event):
        event.widget.edit_modified(True)
    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.modified()


        # Bindings
        self.text.bind("<<TagAdd>>", lambda event: self.tagAdded(event))
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.bind("<Control-s>", lambda event: self.save())
        self.root.bind("<Control-o>", lambda event: self.open())
        self.root.bind("<Control-O>", lambda event: openFolder(self.root))
        self.root.bind("<Control-n>", lambda event: self.new())
        self.root.bind("<Control-S>", lambda event: self.saveAs())

class Edit():
    def copy(self):
        self.root.clipboard_clear()
        textToBeCopied = self.text.get("sel.first", "sel.last")
        self.root.clipboard_append(textToBeCopied)

    def cut(self):
        self.copy()
        self.text.delete("sel.first", "sel.last")

    def paste(self):
        self.text.insert("insert", self.root.clipboard_get())

    def undo(self):
        self.text.edit_undo()

    def redo(self):
        self.text.edit_redo()

    def selectAll(self):
        self.text.tag_add("sel", "1.0", "end")
        self.text.mark_set(0.0, "end")
        self.text.see("insert")

    def clearSelection(self):
        self.text.tag_remove("sel", "1.0", "end")

    def find(self):
        self.text.tag_remove("found", "1.0", "end")
        # Criar um menu de busca

    def __init__(self, root, text):
        self.text = text
        self.root = root
        self.root.bind("<Control-Z>", lambda event: self.redo())
        self.root.bind("<Control-f>", lambda event: self.find())

