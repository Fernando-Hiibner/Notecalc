from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfilename
from tkinter.font import Font

from sys import argv
from os import listdir, getcwd, chdir
from os.path import join, isdir, basename, dirname, expanduser, isfile

from .config_manager import ConfigManager
from ..extras import globals
from ..extras.utilities import toPath, getIcon
from ..extras.file_operations import *
from ..mywidgets.my_widgets import myScrolledText, HighlightListBox

class MainBuilder():
    def createRoot(self, minsizeX=450, minsizeY=575, geometry="900x575+0+0", title="Notecalc", icon=None):
        root = Tk()
        root.minsize(minsizeX, minsizeY)
        root.geometry(geometry)
        root.title(title)
        if icon != None:
            root.iconbitmap(icon)
        return root

    def createTopLevel(self, master = None, minsizeX=450, minsizeY=575, geometry="900x575+0+0", title="TopLevel", icon=None):
        topLevel = Toplevel(master=master)
        topLevel.minsize(width=minsizeX, height=minsizeY)
        topLevel.geometry(geometry)
        topLevel.title(title)
        if icon != None:
            topLevel.iconbitmap(icon)
        return topLevel

    def createText(self, master = None, textConfig = None, font = None, **kw):
        if textConfig == None:
            textConfig = globals.textConfig
        if font == None:
            font = globals.font
        text = myScrolledText(master, bg=textConfig["bg"], fg=textConfig["fg"], insertbackground=textConfig["insertbackground"],
                             tabs=(
                                 textConfig["tab"]), selectbackground=textConfig["selectbackground"], selectforeground=textConfig["selectforeground"],
                             relief=FLAT, undo=True, autoseparators=True,**kw)
        text.configure(font=font)
        return text

    def createSide(self, master = None, sideConfig = None):
        if sideConfig == None:
            sideConfig = globals.sideConfig
            print(sideConfig)
        self.upperFolderPrefix = globals.configSideUpperFolderPrefix
        self.actualFolderPrefix = globals.configSideActualFolderPrefix
        self.folderPrefix = globals.configSideFolderPrefix
        self.filePrefix = globals.configSideFilePrefix

        side = HighlightListBox(master, bg=sideConfig["bg"], relief=FLAT, bd=0, highlightthickness=0,
                            fg=sideConfig["fg"], selectbackground=sideConfig["selectbackground"], selectforeground=sideConfig["selectforeground"], activestyle="none",
                            highlightbackground=sideConfig["highlightbackground"], highlightforeground=sideConfig["highlightforeground"])
        sideFont = Font(
            family=sideConfig["family"], size=sideConfig["size"])
        side.config(font=sideFont, width = 25)

        return side

class SubBuilder(MainBuilder):
    def createSide(self, master = None):
        side = super().createSide(master = master)
        side.bind("<<ListboxSelect>>", self.selected)
        return side
    def createText(self, master = None, **kw):
        text = super().createText(master = master, **kw)
        text.pack(fill=BOTH, expand=1)
        return text
    def selected(self, event):
        if not self.side.selectValidation(event):
            return
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        if value == self.upperFolderPrefix:
            try:
                parentDir = toPath(getcwd())
                parentDir = parentDir.parent
                chdir(parentDir)
            except:
                return
            self.side.destroy()
            self.side = self.createSide(master=self.mainPannedWindow)
            self.mainPannedWindow.add(self.side, before=self.subPannedWindow)
            self.readDir(dirToRead=parentDir)
        elif value.startswith(self.folderPrefix):
            dirToOpen = toPath(join(getcwd(), value[len(self.folderPrefix)::]))
            if not isdir(dirToOpen):
                return
            chdir(dirToOpen)
            self.side.destroy()
            self.side = self.createSide(master=self.mainPannedWindow)
            self.mainPannedWindow.add(self.side, before=self.subPannedWindow)
            self.readDir()
        elif value.startswith(self.filePrefix):
            dirToOpen = toPath(join(getcwd(), value[len(self.filePrefix)::]))
            if not isfile(dirToOpen):
                return
            if toPath(globals.currentWorkingDirectory) != toPath(dirToOpen):
                if self.text.edit_modified() == True:
                    self.root.after_cancel(self.update)
                    wantToSave = askyesno(
                        "Save", "Do you want to save before changing files?")
                    if wantToSave == True:
                        try:
                            if(saveFile(self.text) == False):
                                saveDir = asksaveasfilename(parent=self.root, title='Choose where you want to save the file', defaultextension=(
                                    "*.nxc"), filetypes=(("Notecalc documents (*.nxc)", "*.nxc"), ("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))
                                saveFileAs(self.text, saveDir)
                            if(openFile(self.root, self.text, dirToOpen) == True):
                                self.text.edit_modified(False)
                        except Exception as e:
                            error = askyesno(
                                "Error", f"Failed to save.\nError: {e}\nDo you want to leave without saving?")
                            if error == True:
                                if(openFile(self.root, self.text, dirToOpen) == True):
                                    self.text.edit_modified(False)
                    elif wantToSave == False:
                        if(openFile(self.root, self.text, dirToOpen) == True):
                            self.text.edit_modified(False)
                    self.root.after(200, self.update)
                elif self.text.edit_modified() == False:
                    if(openFile(self.root, self.text, dirToOpen) == True):
                            self.text.edit_modified(False)

    def readDir(self, dirToRead=None):
        if dirToRead == None:
            dirToRead = toPath(getcwd())
        else:
            dirToRead = toPath(dirToRead)
        self.side.insert(0, self.upperFolderPrefix)
        self.side.insert(1, self.actualFolderPrefix+basename(dirToRead), active = False)
        for i in listdir(dirToRead):
            if isdir(join(dirToRead, i)):
                i = self.folderPrefix+i
                self.side.insert(END, i)
        for i in listdir(dirToRead):
            if not isdir(join(dirToRead, i)) and i.endswith(".txt") or i.endswith(".nxc") or i.endswith(".json"):
                j = i
                i = self.filePrefix+i
                self.side.insert(END, i)
                if(globals.currentWorkingDirectory != None):
                    if toPath(join(getcwd(), j)) == toPath(globals.currentWorkingDirectory):
                        self.side.selection_set(self.side.size()-1)
        self.side.insert(END, "", active = False)

    def update(self):
        if globals.sideDir != listdir():
            self.side.delete(0, END)
            self.readDir()
            globals.sideDir = listdir()
        else:
            pass
        self.root.after(200, self.update)

    def showHideSide(self):
        self.sideControl = not self.sideControl
        if self.sideControl == False:
            ConfigManager().modifyConfig({"general" : {"showSide" : False}})
            self.mainPannedWindow.forget(self.side)

        elif self.sideControl == True:
            ConfigManager().modifyConfig({"general" : {"showSide" : True}})
            self.mainPannedWindow.add(self.side, before=self.subPannedWindow)

    def __init__(self):
        self.root = self.createRoot(title = "Lolicalc", icon = getIcon("Lolicalc.ico"))
        ConfigManager()
        # Definindo o diretorio de trabalho
        try:
            chdir(toPath(dirname(argv[1])))
            globals.currentWorkingDirectory = toPath(argv[1])
        except:
            chdir(toPath(expanduser('~/Desktop')))
        # Criação do primeiro bloco
        self.mainPannedWindow = PanedWindow(
            relief="flat", bg=globals.pannedWindowBGConfig, borderwidth=0)
        self.mainPannedWindow.pack(fill="both", expand=1)
        self.pannedWindowScroll = Scrollbar(self.mainPannedWindow, orient="vertical")
        # Criação da sidebar
        self.side = self.createSide(master=self.mainPannedWindow)
        self.readDir()
        self.update()
        if globals.side == True:
            self.mainPannedWindow.add(self.side)

        # Criação do Bloco 2
        self.subPannedWindow = PanedWindow(
            self.mainPannedWindow, relief="flat", bg=globals.pannedWindowBGConfig, borderwidth=0)
        self.mainPannedWindow.add(self.subPannedWindow)
        self.text = self.createText(master=self.subPannedWindow, richText = True)
        #Mostrar ou ocultar Side
        self.sideControl = globals.side
        self.root.bind("<Alt-p>", lambda event: self.showHideSide())
