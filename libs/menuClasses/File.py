from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesnocancel, askyesno

from ..utilities import globals
from ..utilities.fileOperations import *

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