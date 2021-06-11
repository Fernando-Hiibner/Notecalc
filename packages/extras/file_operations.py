from ast import literal_eval
from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import askopenfilename, askdirectory
from os import getcwd, chdir
from os.path import dirname

from . import globals
from .utilities import toPath, replaceSubstring

def openFileInterpreter(type, text, value, tagInitIndex, index):
    if type == 0:
        formatFont = Font(text, text.cget("font"))
        try:
            tagDict = eval(value)
        except:
            tagDict = value
        size = tagDict["size"]

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


        formatFont.config(size=size)

        if tagDict["prefix"] == "color" or tagDict["prefix"] == None or globals.vsc == False:
            text.tag_config(value, font=formatFont, foreground=tagDict["hex"])
        elif tagDict["prefix"] in globals.colorConfig.keys() and globals.vsc:
            text.tag_config(value, font=formatFont, foreground=globals.colorConfig[tagDict["prefix"]])

        text.tag_add(value, f"{tagInitIndex}", f"{index}")
    elif type == 1:
        #{"prefix" : None, "tags" : list(), "size" = 18, "hex" : '#cccccc'}
        size = globals.font.cget("size")
        size = str(size)
        if len(size) < 2:
            size = "0"+size
        size = int(size)
        newTag = {"prefix" : None, "tags" : list(), "size" : size, "hex" : globals.colorConfig["default"]}
        if "cor" in value: #Color
            color = value[3::]
            newTag["prefix"] = "color"
            newTag["hex"] = color
        elif value.startswith("#"): #Color from the oldest version
            newTag["prefix"] = "color"
            newTag["hex"] = value
        else:
            conversionDict = {
                "tit" : "title",
                "stit" : "subtitle",
                "bt" : "bold",
                "it" : "italic",
                "un" : "underline",
                "tc" : "overstrike"
            }
            newTag["tags"].append(conversionDict[value])
            newTag["prefix"] = conversionDict[value]
        openFileInterpreter(0, text, newTag, tagInitIndex, index)
    elif type == 2: #TODO Fazer essa retrocompatibilidade, não tenho nenhum arquivo dela aqui agora
        fontDaFormatacao = Font(text, text.cget("font"))
        fontSize = fontDaFormatacao.cget("size")

        if "n" in value[globals.formsIndex["n"]:]:
            fontDaFormatacao.config(weight="bold")
        if "i" in value[globals.formsIndex["n"]:]:
            fontDaFormatacao.config(slant="italic")
        if "t" in value[globals.formsIndex["n"]:]:
            fontDaFormatacao.config(overstrike=1)
        if "s" in value[globals.formsIndex["n"]:]:
            fontDaFormatacao.config(underline=1)

        if(len(value) == 14):
            size = value[5:7]

        fontDaFormatacao.config(size=int(size))

        cor = globals.configCores["padrao"]
        if value[0] == "v" and globals.vsc == True:
            if value[:globals.formsIndex["n"]] == "vbt":
                cor = globals.configCores["negrito"]
            if value[:globals.formsIndex["n"]] == "vtt":
                cor = globals.configCores["titulo"]
            if value[:globals.formsIndex["n"]] == "vit":
                cor = globals.configCores["italico"]
            if value[:globals.formsIndex["n"]] == "vst":
                cor = globals.configCores["subtitulo"]
            if value[:globals.formsIndex["n"]] == "vun":
                cor = globals.configCores["sublinhado"]
            if value[:globals.formsIndex["n"]] == "vtc":
                cor = globals.configCores["tachado"]
        elif value[0] == "c":
            cor = value[globals.formsIndex["hex"]::]

        value = value[:globals.formsIndex["hex"]]+cor

        text.tag_config(value, font=fontDaFormatacao, foreground=cor)

        text.tag_add(value, f"{tagInitIndex}", f"{index}")

def openFile(root, text, dirToOpen = None):
    if dirToOpen == None:
        dirToOpen = askopenfilename(parent=root, title='Choose file to open', filetypes=(
            ("Notecalc documents (*.nxc)", "*.nxc"), ("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))
    dirToOpen = toPath(dirToOpen)

    with open(dirToOpen, 'r', encoding='utf-8') as file:
        text.delete('1.0', 'end')
        fileText = file.read()
        if str(dirToOpen).endswith(".nxc") == True:
            fileText = literal_eval(fileText)
            final = ""
            for (key, value, index) in fileText:
                if key == "text":
                    final += value
            text.insert('1.0', final)
            tagsInitIndexes = list()
            for (key, value, index) in fileText:
                if key == "tagon":
                    tagsInitIndexes.append(index)
                elif key == "tagoff":
                    tagInitIndex = tagsInitIndexes.pop(0)
                    if value.startswith("{"):
                        openFileInterpreter(0, text, value, tagInitIndex, index)
                    elif value == 'sel': #Rare
                        continue
                    elif len(value) < 14: #Retrocomp
                        openFileInterpreter(1, text, value, tagInitIndex, index)
                    elif len(value) >= 14: #Beta retrocomp, really rare to happen just one person that i know have this kind of archive
                        openFileInterpreter(2, text, value, tagInitIndex, index)

            text.edit_modified(False)
            globals.currentWorkingDirectory = dirToOpen
            chdir(dirname(dirToOpen))
            root.title("Lolicalc "+str(globals.currentWorkingDirectory))
            return True
        else:
            text.edit_modified(False)
            globals.currentWorkingDirectory = dirToOpen
            chdir(dirname(dirToOpen))
            root.title("Lolicalc "+str(globals.currentWorkingDirectory))
            text.insert('1.0', fileText)
            return True


def openFolder(janela):
    chdir(toPath(askdirectory(parent = janela, title = "Escolha uma pasta...", initialdir = toPath(getcwd()))))

def saveFile(Caixa):
    if globals.currentWorkingDirectory == '' or globals.currentWorkingDirectory == None:
        return False
    else:
        try:
            if str(globals.currentWorkingDirectory).endswith(".nxc"):
                Caixa.tag_remove("sel", 0.0, END)
                texto = str(Caixa.dump('1.0', 'end'))
                with open(toPath(globals.currentWorkingDirectory), 'w', encoding='utf-8') as arquivo:
                    arquivo.truncate(0)
                    arquivo.write(texto)
                    arquivo.close()
                Caixa.edit_modified(False)
            else:
                Caixa.tag_remove("sel", 0.0, END)
                texto = Caixa.get('1.0', 'end-1c')
                with open(toPath(globals.currentWorkingDirectory), 'w', encoding='utf-8') as arquivo:
                    arquivo.truncate(0)
                    arquivo.write(texto)
                    arquivo.close()
                Caixa.edit_modified(False)
        except NameError:
            globals.currentWorkingDirectory = ''
            return False


def saveFileAs(Caixa, dirAbrir):
    dirAbrir = toPath(dirAbrir)
    if(str(dirAbrir).endswith(".nxc")):
        Caixa.tag_remove("sel", 0.0, END)
        texto = str(Caixa.dump('1.0', 'end'))
        with open(dirAbrir, 'w', encoding='utf-8') as arquivo:
            arquivo.truncate(0)
            arquivo.write(texto)
            arquivo.close()
    else:
        Caixa.tag_remove("sel", 0.0, END)
        texto = Caixa.get('1.0', 'end-1c')
        with open(dirAbrir, 'w', encoding='utf-8') as arquivo:
            arquivo.truncate(0)
            arquivo.write(texto)
            arquivo.close()
    globals.currentWorkingDirectory = dirAbrir
    chdir(toPath(dirname(dirAbrir)))
    Caixa.edit_modified(False)
    return True


