from tkinter import *
from tkinter.font import Font
from tkinter.colorchooser import askcolor

from ..utilities import globals

class Format():
    def chooseColor(self):
        (rgb, globals.hex) = askcolor()
        if globals.hex == None:
            globals.hex = globals.colorConfig["default"]
        self.addTags(colorHex=globals.hex)

    def changeColor(self, colorHex=None):
        if colorHex != None:
            globals.hex = colorHex
        if globals.hex == None:
            return self.chooseColor()
        self.addTags(colorHex=globals.hex)

    def validateTags(self):
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

            if tagDict["prefix"] == "color" or tagDict["prefix"] == None:
                self.text.tag_config(tag, font=formatFont, foreground=tagDict["hex"])
            elif tagDict["prefix"] in globals.colorConfig.keys() and globals.vsc:
                print("Tchau")
                self.text.tag_config(tag, font=formatFont, foreground=globals.colorConfig[tagDict["prefix"]])
    
    def createNewTag(self, tag=None, size=None, colorHex=None, sizeMod = False):
        #Tag template
        #{"prefix" : None, "tags" : list(), "size" = 18, "hex" : '#cccccc'}
        fontSize = globals.font.cget("size")
        if tag == None and size == None and colorHex == None and sizeMod == False:
            return str({"prefix" : None, "tags" : [], "size" : fontSize, "hex" : globals.colorConfig["default"]})
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
        if colorHex != None and colorHex not in globals.colorConfig.values():
            prefix = "color"
        elif colorHex in globals.colorConfig.values() and colorHex != globals.colorConfig["default"]:
            for key, value in globals.colorConfig.items():
                if value == colorHex:
                    prefix = key
                    break
        elif globals.vsc == True and colorHex == None:
            colorHex = globals.colorConfig["default"]
            prefix = tag

        if colorHex == None:
            colorHex = globals.colorConfig["default"]

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
                    fontSize = globals.font.cget("size")

                    if size == None:
                        size = tagSize
                    elif size != None and sizeMod == False:
                        if len(str(size)) < 2:
                            size = "0"+str(size)
                        size = int(size)
                    elif size != None and sizeMod == True:
                        if fontSize+size == tagSize:
                            size = fontSize
                        elif fontSize+size != tagSize:
                            size = fontSize+size
                        if len(str(size)) < 2:
                            size = "0"+str(size)
                        size = int(size)

                    newTagInSel = tagDict

                    newTagInSel["size"] = size

                    if tag != None:
                        if tag in newTagInSel["tags"]:
                            newTagInSel["tags"].remove(tag)
                            if sizeMod:
                                newTagInSel["size"] == fontSize                           
                        elif tag not in newTagInSel["tags"]:
                            newTagInSel["tags"].append(tag)
                    
                    #Acho que pra ficar suave agora so tirar a cor quando todas as tags sumiram, e caso for titulo ou sub, fazer ele tirar o size também
                    #lançar isso como uma função, e poder chamar pq tipo, quando eu tiro o subtitulo, ele perde a cor mesmo que tenha outras tags 
                    if colorHex != None and colorHex not in globals.colorConfig.values():
                        newTagInSel["prefix"] = "color"
                        newTagInSel["hex"] = colorHex
                    elif colorHex in globals.colorConfig.values() and colorHex != globals.colorConfig["default"]:
                        for key, value in globals.colorConfig.items():
                            if value == colorHex:
                                newTagInSel["prefix"] = key
                                newTagInSel["hex"] = colorHex
                                break
                    elif globals.vsc == True and colorHex == None and len(newTagInSel["tags"]) > 0 and newTagInSel["prefix"] != "color":
                        newTagInSel["hex"] = globals.colorConfig["default"]
                        newTagInSel["prefix"] = newTagInSel["tags"][-1]
                    elif newTagInSel["prefix"] != "color":
                        newTagInSel["hex"] = globals.colorConfig["default"]
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

    def __init__(self, root, text):
        self.root = root
        self.text = text

        self.root.bind(
            "<Alt-t>", lambda event: self.addTags(tag="title", size = 4, sizeMod=True))
        self.root.bind(
            "<Alt-s>", lambda event: self.addTags(tag="subtitle", size = 2, sizeMod=True))
        self.root.bind("<Alt-b>", lambda event: self.addTags(tag="bold"))
        self.root.bind("<Alt-i>", lambda event: self.addTags(tag="italic"))
        self.root.bind("<Alt-_>", lambda event: self.addTags(tag="underline"))
        self.root.bind("<Alt-r>", lambda event: self.addTags(tag="remove"))
        self.root.bind("<Alt-c>", lambda event: self.changeColor())





