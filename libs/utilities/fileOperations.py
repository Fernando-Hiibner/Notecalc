from ast import literal_eval
from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import askopenfilename, askdirectory
from os import getcwd, chdir
from os.path import dirname

from ..utilities import globals
from ..utilities.utilities import toPath, replaceSubstring


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
                    if len(value) < 14:
                        size = globals.font.cget("size")
                        size = str(size)                        
                        if len(size) < 2:
                            size = "0"+size
                        sampleTag = "......." + size[0] + size[1] + globals.colorConfig["def"]
                        size = int(size)
                        if "bt" in value:
                            sampleTag = replaceSubstring(
                                sampleTag, ".", "n", globals.formsIndex["n"])
                        elif "stit" in value:
                            sampleTag = replaceSubstring(
                                sampleTag, ".", "i", globals.formsIndex["i"])
                            sizeSubTitulo = size + 2
                            sizeSubTitulo = str(sizeSubTitulo)
                            if len(sizeSubTitulo) < 2:
                                sizeSubTitulo = "0"+sizeSubTitulo
                            sampleTag = replaceSubstring(
                                sampleTag, sampleTag[globals.formsIndex["size"]], sizeSubTitulo[0], globals.formsIndex["size"])
                            sampleTag = replaceSubstring(
                                sampleTag, sampleTag[globals.formsIndex["size"]+1], sizeSubTitulo[1], globals.formsIndex["size"]+1)
                        elif "tit" in value:
                            if(sampleTag[globals.formsIndex["n"]] != "n"):
                                sampleTag = replaceSubstring(
                                    sampleTag, ".", "n", globals.formsIndex["n"])
                            sizeTitulo = size + 4
                            sizeTitulo = str(sizeTitulo)
                            if len(sizeTitulo) < 2:
                                sizeTitulo = "0"+sizeTitulo
                            sampleTag = replaceSubstring(
                                sampleTag, sampleTag[globals.formsIndex["size"]], sizeTitulo[0], globals.formsIndex["size"])
                            sampleTag = replaceSubstring(
                                sampleTag, sampleTag[globals.formsIndex["size"]+1], sizeTitulo[1], globals.formsIndex["size"]+1)
                        elif "it" in value:
                            if(sampleTag[globals.formsIndex["i"]] != "i"):
                                sampleTag = replaceSubstring(
                                    sampleTag, ".", "i", globals.formsIndex["i"])
                        elif "un" in value:
                            sampleTag = replaceSubstring(
                                sampleTag, ".", "s", globals.formsIndex["s"])
                        elif "tc" in value:
                            sampleTag = replaceSubstring(
                                sampleTag, ".", "t", globals.formsIndex["t"])
                        elif "cor" in value:
                            cor = value[3::]
                            sampleTag = "cor"+sampleTag[globals.formsIndex["n"]:globals.formsIndex["hex"]]+cor
                        # Pra manter a compatibilidade com os arquivos da antiga formatação
                        elif value.startswith("#"):
                            cor = value
                            sampleTag = "cor"+sampleTag[globals.formsIndex["n"]:globals.formsIndex["hex"]]+cor

                        fontDaFormatacao = Font(text, text.cget("font"))
                        fontSize = fontDaFormatacao.cget("size")

                        if "n" in sampleTag[globals.formsIndex["n"]:]:
                            fontDaFormatacao.config(weight="bold")
                        if "i" in sampleTag[globals.formsIndex["n"]:]:
                            fontDaFormatacao.config(slant="italic")
                        if "t" in sampleTag[globals.formsIndex["n"]:]:
                            fontDaFormatacao.config(overstrike=1)
                        if "s" in sampleTag[globals.formsIndex["n"]:]:
                            fontDaFormatacao.config(underline=1)

                        if(len(sampleTag) == 14):
                            size = sampleTag[5:7]
                        elif(len(sampleTag) == 16):
                            size = sampleTag[globals.formsIndex["size"]:globals.formsIndex["size"]+2]
                        
                        fontDaFormatacao.config(size=int(size))
                        
                        cor = globals.configCores["padrao"]
                        prefixo = "..."
                        if sampleTag[0] == "c":
                            cor = sampleTag[globals.formsIndex["hex"]::]
                            prefixo = "cor"
                        elif globals.vsc == True:
                            if "n" in sampleTag[globals.formsIndex["n"]:] and int(size) != fontSize+4:
                                cor = globals.configCores["negrito"]
                                prefixo = "vbt"
                            if "n" in sampleTag[globals.formsIndex["n"]:] and int(size) == fontSize+4:
                                cor = globals.configCores["titulo"]
                                prefixo = "vtt"
                            if "i" in sampleTag[globals.formsIndex["n"]:] and int(size) != fontSize+2:
                                cor = globals.configCores["italico"]
                                prefixo = "vit"
                            if "i" in sampleTag[globals.formsIndex["n"]:] and int(size) == fontSize+2:
                                cor = globals.configCores["subtitulo"]
                                prefixo = "vst"
                            if "s" in sampleTag[globals.formsIndex["n"]:]:
                                cor = globals.configCores["sublinhado"]
                                prefixo = "vtc"
                            if "t" in sampleTag[globals.formsIndex["n"]:]:
                                cor = globals.configCores["tachado"]
                                prefixo = "vun"                        
                        
                        sampleTag = prefixo+sampleTag[globals.formsIndex["n"]:globals.formsIndex["hex"]]+cor
                        text.tag_config(sampleTag, font=fontDaFormatacao, foreground=cor)
                    
                        text.tag_add(sampleTag, f"{tagInitIndex}", f"{index}")

                    elif len(value) >= 14:
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
                        elif(len(value) == 16):
                            size = value[globals.formsIndex["size"]:globals.formsIndex["size"]+2]
                        
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

            text.edit_modified(False)
            globals.dirDeTrabalhoAtual = dirToOpen
            chdir(dirname(dirToOpen))
            root.title("Lolicalc "+str(globals.dirDeTrabalhoAtual))
            return True
        else:
            text.edit_modified(False)
            globals.dirDeTrabalhoAtual = dirToOpen
            chdir(dirname(dirToOpen))
            root.title("Lolicalc "+str(globals.dirDeTrabalhoAtual))
            text.insert('1.0', fileText)
            return True
            

def openFolder(janela):
    chdir(toPath(askdirectory(parent = janela, title = "Escolha uma pasta...", initialdir = toPath(getcwd()))))

def saveFile(Caixa):
    if globals.dirDeTrabalhoAtual == '' or globals.dirDeTrabalhoAtual == None:
        return False
    else:
        try:
            if str(globals.dirDeTrabalhoAtual).endswith(".nxc"):
                Caixa.tag_remove("sel", 0.0, END)
                texto = str(Caixa.dump('1.0', 'end'))
                with open(toPath(globals.dirDeTrabalhoAtual), 'w', encoding='utf-8') as arquivo:
                    arquivo.truncate(0)
                    arquivo.write(texto)
                    arquivo.close()
                Caixa.edit_modified(False)
            else:
                Caixa.tag_remove("sel", 0.0, END)
                texto = Caixa.get('1.0', 'end-1c')
                with open(toPath(globals.dirDeTrabalhoAtual), 'w', encoding='utf-8') as arquivo:
                    arquivo.truncate(0)
                    arquivo.write(texto)
                    arquivo.close()
                Caixa.edit_modified(False)
        except NameError:
            globals.dirDeTrabalhoAtual = ''
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
    globals.dirDeTrabalhoAtual = dirAbrir
    chdir(toPath(dirname(dirAbrir)))
    Caixa.edit_modified(False)
    return True


