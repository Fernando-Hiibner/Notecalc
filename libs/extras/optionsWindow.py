from tkinter import *
from tkinter import ttk
from tkinter.font import Font, families
from tkinter.colorchooser import Chooser, askcolor

from configparser import ConfigParser
from os import listdir, getcwd
from os.path import expanduser, join, basename, isdir, join

from ..utilities import globals
from ..menuClasses.Format import Format
from ..menus.fastMenu import FastMenu
from ..myTkinterWidgets.myWidgets import HighlightListBox, LabelButton
from ..extras.Builder import MainBuilder
from ..extras.configManager import ConfigManager
from ..utilities.utilities import toPath, getIcon

def getThemes():
    configDir = toPath(join(expanduser("~/Documents/Notecalc"), "config.ini"))
    config = ConfigParser()
    config.read(configDir, encoding="utf-8")
    sectionsToIgnore = ["general", "SidePrefix1", "SidePrefix2"]
    themes = [section.capitalize() for section in config.sections() if section not in sectionsToIgnore]
    return themes

def getSidePrefix():
    configDir = toPath(join(expanduser("~/Documents/Notecalc"), "config.ini"))
    config = ConfigParser()
    config.read(configDir, encoding="utf-8")
    prefix = [section for section in config.sections() if "SidePrefix" in section]
    return prefix

def readDir(listbox, **kw):
    if "prefix" not in kw.keys():
        upperFolderPrefix = globals.configSideUpperFolderPrefix
        actualFolderPrefix = globals.configSideActualFolderPrefix
        folderPrefix = globals.configSideFolderPrefix
        filePrefix = globals.configSideFilePrefix
    else:
        prefix = kw.pop("prefix")
        upperFolderPrefix = prefix["upper"]
        actualFolderPrefix = prefix["actual"]
        folderPrefix = prefix["folder"]
        filePrefix = prefix["file"]  

    dirALer = toPath(getcwd())
    listbox.delete(0, "end")
    listbox.insert(0, upperFolderPrefix)
    listbox.insert(1, actualFolderPrefix+basename(dirALer), active=False)
    for dir in listdir(dirALer):
        if isdir(join(dirALer, dir)):
            dir = folderPrefix+dir
            listbox.insert(END, dir)
    for dir in listdir(dirALer):
        if not isdir(join(dirALer, dir)) and dir.endswith(".txt") or dir.endswith(".nxc") or dir.endswith(".ini"):
            auxDir = dir
            dir = filePrefix+dir
            listbox.insert(END, dir)
            if(globals.currentWorkingDirectory != None):
                if toPath(join(dirALer, auxDir)) == toPath(globals.currentWorkingDirectory):
                    listbox.select_set(listbox.size()-1)
    listbox.insert(END, "", active=False)

def changeColors(parent = None, caller = None, title = None, configDict = None, key = None, target = None, targetType = None, chooseColor = True):
    if chooseColor == True:
        (rgb, hex) = askcolor(parent = parent, title = title, color = configDict[key])
    else:
        hex = configDict[key]
    if targetType == 'text' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
        target.config(**{key : hex})
        if key == 'selectbackground':
            target.config({'inactiveselect' : hex})
        if caller != None:
            caller.config(highlightbackground = hex, bg = hex)
    if targetType == 'side' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
        target.config(**{key : hex})
        if caller != None:
            caller.config(highlightbackground = hex, bg = hex)
    if targetType == 'font' and key == 'padrao' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
        target.config(foreground = hex)
        if caller != None:
            caller.config(highlightbackground = hex, bg = hex)
    elif targetType == 'font' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
        configDict[key] = hex
        if caller != None:  
            caller.config(highlightbackground = hex, bg = hex)

class OptionsWindow(MainBuilder):
    def __init__(self, mainRoot):
        self.mainRoot = mainRoot

        self.root = MainBuilder.createTopLevel(mainRoot, geometry = "900x720+0+0", minsizeX=800, minsizeY=620, title = "Options")

        self.tabControl = ttk.Notebook(self.root)

        self.fontTab = ttk.Frame(self.tabControl)
        self.themeTab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.fontTab, text = "Font")
        self.tabControl.add(self.themeTab, text = "Theme")

        self.tabControl.pack(expand = 1, fill = "both", padx = 5, pady = 5)

        self.createLocalConfigs()
        self.createFontTab()

    def createLocalConfigs(self):
        #Local config
        self.tempFont = globals.font
        self.tempVscConfig = globals.vsc
        self.tempTextConfig = globals.textConfig
        self.tempSideConfig = globals.sideConfig
        self.tempColorConfig = globals.colorConfig

        self.tempUpperFolderPrefix = globals.configSideUpperFolderPrefix
        self.tempActualFolderPrefix = globals.configSideActualFolderPrefix
        self.tempFolderPrefix = globals.configSideFolderPrefix
        self.tempFilePrefix = globals.configSideFilePrefix    

    def createFontTab(self):
        #Frame and Listbox for Font and Font Size
        self.fontsFrame1 = Frame(self.fontTab, highlightbackground="#cccccc", highlightthickness=0.5)
        self.fontsFrame1.pack(fill = "both", side = "left", padx = 10, pady = 15, ipadx = 5, ipady = 5, anchor = "nw")
        self.fontsLabel1 = Label(self.fontTab, text = "Font / Size")
        self.fontsLabel1.place(anchor = "w", x = 15, y = 15)

        self.fontsListbox = HighlightListBox(self.fontsFrame1, relief = "flat", activestyle="none", width = 25, exportselection = False)
        self.fontsListbox.config(width = 25)
        
        self.lastSelectedFontsIndex = -1
        for self.fontFamily in families():
            self.fontsListbox.insert(END, self.fontFamily)
            if self.fontFamily == self.tempFont.cget("family"):
                self.lastSelectedFontsIndex = self.fontsListbox.size() - 1
        self.fontsListbox.select_set(self.lastSelectedFontsIndex)
        self.fontsListbox.insert(END, "", active=False)
        self.fontsListbox.pack(expand = 1, fill = "both", padx=5, pady = 20, anchor = "nw")

        self.fontSizeLabel = Label(self.fontsFrame1, text = "Size:", anchor = "w")
        self.fontSizeLabel.pack(fill = "x", anchor = "w", side = "left")
        
        self.possibleFontSizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.fontSizeCombobox = ttk.Combobox(self.fontsFrame1, value = self.possibleFontSizes)
        self.fontSizeCombobox.current(self.possibleFontSizes.index(self.tempFont.cget("size")))
        self.fontSizeCombobox.pack(expand = 1,fill = "x", anchor = "w", side = "left")

        self.vscCheckIntVar = IntVar(self.root, value = self.tempVscConfig)
        self.fontVSCCheckButton = Checkbutton(self.fontsFrame1, text = "VSC", variable = self.vscCheckIntVar, onvalue = 1, offvalue = 0)
        self.fontVSCCheckButton.pack(expand = 1,fill = "x", anchor = "w", side = "left")
        
        #Frame and Text for Font sample
        self.fontsFrame2 = Frame(self.fontTab, highlightbackground="#cccccc", highlightthickness=0.5)
        self.fontsFrame2.pack(expand = 1, fill = "both", side = "top", padx = 10, pady = 15, ipadx = 5, ipady = 5, anchor = "ne")
        self.fontsLabel2 = Label(self.fontTab, text = "Editable Sample")
        self.fontsLabel2.place(anchor = "w", x = 285, y = 15)

        self.fontSampleText = MainBuilder.createText(self, master=self.fontsFrame2, textConfig=self.tempTextConfig, font = self.tempFont)
        self.fontSampleText.config(richText = True)
        self.fontSampleText.pack(expand = 1, fill = "both", padx = 5, pady = 10)

        self.fontsListbox.bind("<<ListboxSelect>>", lambda event: self.getSelectedFontFromListbox(event))
        self.fontSizeCombobox.bind("<<ComboboxSelected>>", lambda event: self.getFontSizeFromCombobox(event))
        self.fontVSCCheckButton.config(command = lambda vsc = self.vscCheckIntVar.get(): self.fontChanges(vsc = vsc))
    
    def getSelectedFontFromListbox(self, event):
        widget = event.widget
        self.lastSelectedFontsIndex = int(widget.curselection()[0])
        return self.fontChanges(selectedFont = widget.get(self.lastSelectedFontsIndex))
    
    def getFontSizeFromCombobox(self, event):
        return self.fontChanges(size = event.widget.get())

    def fontChanges(self, **kw):
        if 'selectedFont' in kw.keys():
            selectedFont = kw.pop('selectedFont')
        elif self.lastSelectedFontsIndex != -1:
            selectedFont = self.fontsListbox.get(self.lastSelectedFontsIndex)
        else:
            selectedFont = self.tempFont.cget("family")
        
        if 'size' in kw.keys():
            size = kw.pop('size')
        else:
            size = self.fontSizeCombobox.get()
        
        self.tempFont.config(family = selectedFont, size = size)
        self.fontSampleText.config(font = self.tempFont)

        if 'vsc' in kw.keys():
            print("Oi")
            vsc = kw.pop('vsc')
            if vsc == 1:
                self.tempVscConfig = True
                #Executar a mudança de vsc
            else:
                self.tempVscConfig = False
                #Executar a mudanca de vsc


        
def optionsWindow(mainRoot):
    window = OptionsWindow(mainRoot)
def aoptionsWindow(mainRoot):
    builder = MainBuilder()
    #root = builder.createRoot(geometry = "900x720+0+0", minsizeX=800, minsizeY=620, title = "Options")
    root = builder.createTopLevel(mainRoot, geometry = "900x720+0+0", minsizeX=800, minsizeY=620, title = "Options")

    tabControl = ttk.Notebook(root)

    fontTab = ttk.Frame(tabControl)
    themeTab = ttk.Frame(tabControl)

    tabControl.add(fontTab, text = "Font")
    tabControl.add(themeTab, text = "Theme")

    tabControl.pack(expand = 1, fill = "both", padx = 5, pady = 5)

    #Local config
    tempFont = globals.font
    tempVscConfig = globals.vsc
    tempTextConfig = globals.textConfig
    tempSideConfig = globals.sideConfig
    tempColorConfig = globals.colorConfig

    tempUpperFolderPrefix = globals.configSideUpperFolderPrefix
    tempActualFolderPrefix = globals.configSideActualFolderPrefix
    tempFolderPrefix = globals.configSideFolderPrefix
    tempFilePrefix = globals.configSideFilePrefix

    #Frame and listbox for themes
    holderFrame = Frame(themeTab)
    holderFrame.pack(fill = "both", side = "left", padx = 10, pady = 15, ipadx = 5, ipady = 20, anchor = "nw")
    themesFrame1 = Frame(holderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
    themesFrame1.pack(expand = 0, fill = "both")
    themesLabel1 = Label(themeTab, text = "Themes")
    themesLabel1.place(anchor = "w", x = 15, y = 15)

    themesList = getThemes()
    themesOptionMenu = ttk.Combobox(themesFrame1, value=themesList)
    themesOptionMenu.current(themesList.index(globals.theme.capitalize()))
    themesOptionMenu.pack(expand = 0, fill = "both", padx = 5, pady = 10, anchor = "nw")
    
    #Main Frame and Label for Text Options
    textOptionsLabel= Label(themeTab, text = "Text Options")
    textOptionsLabel.place(anchor = "w", x = 15, y = 72)

    textOptionsFrame = Frame(holderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
    textOptionsFrame.pack(fill = "both", pady = 15)

    #Left Frame and Labels for Text Options
    leftTextOptionsHolderFrame = Frame(textOptionsFrame)
    leftTextOptionsHolderFrame.pack(expand = 1, side = "left", anchor = "nw", pady = 5)

    textOptionsLabelBGColor = Label(leftTextOptionsHolderFrame, text = "Background:")
    textOptionsLabelBGColor.pack(side = "top", anchor = "nw", pady = 1)

    textOptionsLabelFGColor= Label(leftTextOptionsHolderFrame, text = "Foreground:")
    textOptionsLabelFGColor.pack(side = "top", anchor = "nw", pady = 1)

    textOptionsLabelSelectBGColor= Label(leftTextOptionsHolderFrame, text = "Select Background:")
    textOptionsLabelSelectBGColor.pack(side = "top", anchor = "nw", pady = 1)

    textOptionsLabelSelectFGColor= Label(leftTextOptionsHolderFrame, text = "Select Foreground:")
    textOptionsLabelSelectFGColor.pack(side = "top", anchor = "nw", pady = 1)

    textOptionsLabelInsertBGColor= Label(leftTextOptionsHolderFrame, text = "Insert Background:")
    textOptionsLabelInsertBGColor.pack(side = "top", anchor = "nw", pady = 1)

    #Right frame and Labels for text options
    rightTextOptionsHolderFrame = Frame(textOptionsFrame)
    rightTextOptionsHolderFrame.pack(expand = 1, fill = "x", side = "right", anchor = "nw", pady = 5)

    textOptionsButtonBGColor = LabelButton(rightTextOptionsHolderFrame, width = 10, relief = "flat", bg = tempTextConfig['bg'])
    textOptionsButtonBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    textOptionsButtonFGColor = LabelButton(rightTextOptionsHolderFrame, width = 10, relief = "flat", bg = tempTextConfig['fg'])
    textOptionsButtonFGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    textOptionsButtonSelectBGColor = LabelButton(rightTextOptionsHolderFrame, width = 10, relief = "flat", bg = tempTextConfig['selectbackground'])
    textOptionsButtonSelectBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    textOptionsButtonSelectFGColor = LabelButton(rightTextOptionsHolderFrame, width = 10, relief = "flat", bg = tempTextConfig['selectforeground'])
    textOptionsButtonSelectFGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    textOptionsButtonInsertBGColor = LabelButton(rightTextOptionsHolderFrame, width = 10, relief = "flat", bg = tempTextConfig['insertbackground'])
    textOptionsButtonInsertBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    #Side prefix options
    sidePrefixOptionsLabel = Label(themeTab, text = "Side Prefix Options")
    sidePrefixOptionsLabel.place(anchor = "w", x = 15, y = 213)

    sidePrefixOptionsFrame = Frame(holderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
    sidePrefixOptionsFrame.pack(fill = "both")

    sidePrefixList = getSidePrefix()
    sidePrefixMenu = ttk.Combobox(sidePrefixOptionsFrame, value=sidePrefixList)
    sidePrefixMenu.current(sidePrefixList.index(globals.sidePrefix))
    sidePrefixMenu.pack(expand = 1, fill = "both", padx = 5, pady = 10, anchor = "nw")


    #Main frame and labels for side option
    sideOptionsLabel = Label(themeTab, text = "Side Options")
    sideOptionsLabel.place(anchor = "w", x = 15, y = 273)

    sideOptionsFrame = Frame(holderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
    sideOptionsFrame.pack(fill = "both", pady = 15)

    #Frame and labels for side options
    leftSideOptionsHolderFrame = Frame(sideOptionsFrame)
    leftSideOptionsHolderFrame.pack(expand = 1, side = "left", anchor = "nw", pady = 5)

    sideOptionsLabelBGColor= Label(leftSideOptionsHolderFrame, text = "Background:")
    sideOptionsLabelBGColor.pack(side = "top", anchor = "nw", pady = 1)

    sideOptionsLabelFGColor= Label(leftSideOptionsHolderFrame, text = "Foreground:")
    sideOptionsLabelFGColor.pack(side = "top", anchor = "nw", pady = 1)

    sideOptionsLabelSelectBGColor= Label(leftSideOptionsHolderFrame, text = "Select Background:")
    sideOptionsLabelSelectBGColor.pack(side = "top", anchor = "nw", pady = 1)

    sideOptionsLabelSelectFGColor= Label(leftSideOptionsHolderFrame, text = "Select Foreground:")
    sideOptionsLabelSelectFGColor.pack(side = "top", anchor = "nw", pady = 1)

    sideOptionsLabelHighlightBGColor= Label(leftSideOptionsHolderFrame, text = "Highlight Background:")
    sideOptionsLabelHighlightBGColor.pack(side = "top", anchor = "nw", pady = 1)

    sideOptionsLabelHighlightFGColor= Label(leftSideOptionsHolderFrame, text = "Highlight Foreground:")
    sideOptionsLabelHighlightFGColor.pack(side = "top", anchor = "nw", pady = 1)  

    #Frame and buttons for side options 
    rightSideOptionsHolderFrame = Frame(sideOptionsFrame)
    rightSideOptionsHolderFrame.pack(expand = 1, fill = "x", side = "right", anchor = "nw", pady = 5)

    sideOptionsButtonBGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['bg'])
    sideOptionsButtonBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    sideOptionsButtonFGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['fg'])
    sideOptionsButtonFGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    sideOptionsButtonSelectBGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['selectbackground'])
    sideOptionsButtonSelectBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    sideOptionsButtonSelectFGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['selectforeground'])
    sideOptionsButtonSelectFGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    sideOptionsButtonHighlightBGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['highlightbackground'])
    sideOptionsButtonHighlightBGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    sideOptionsButtonHighlightFGColor= LabelButton(rightSideOptionsHolderFrame, width = 10, relief = "flat", bg = tempSideConfig['highlightforeground'])
    sideOptionsButtonHighlightFGColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    #Vsc options
    vscOptionsFrame = Frame(holderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
    vscOptionsFrame.pack(expand = 1, fill = "both")

    vscOptionsLabel = Label(holderFrame, text = "VSC Options")
    vscOptionsLabel.place(anchor = "w", x = 10, y = 423)

    #Label and and frame for texts
    leftVscOptionsHolderFrame = Frame(vscOptionsFrame)
    leftVscOptionsHolderFrame.pack(expand = 1, side = "left", anchor = "nw", pady = 5)

    vscOptionsLabelDefaultColor = Label(leftVscOptionsHolderFrame, text = "Default Color: ")
    vscOptionsLabelDefaultColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelTitleColor = Label(leftVscOptionsHolderFrame, text = "Title Color: ")
    vscOptionsLabelTitleColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelSubtitleColor = Label(leftVscOptionsHolderFrame, text = "Subtitle Color: ")
    vscOptionsLabelSubtitleColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelBoldColor = Label(leftVscOptionsHolderFrame, text = "Bold Color: ")
    vscOptionsLabelBoldColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelItalicColor = Label(leftVscOptionsHolderFrame, text = "Italic Color: ")
    vscOptionsLabelItalicColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelUnderlineColor = Label(leftVscOptionsHolderFrame, text = "Underline Color: ")
    vscOptionsLabelUnderlineColor.pack(side = "top", anchor = "nw", pady = 1)

    vscOptionsLabelOverstrikeColor = Label(leftVscOptionsHolderFrame, text = "Overstrike Color: ")
    vscOptionsLabelOverstrikeColor.pack(side = "top", anchor = "nw", pady = 1)

    #Right Frame for Button
    rightVscOptionsHolderFrame = Frame(vscOptionsFrame)
    rightVscOptionsHolderFrame.pack(expand = 1, fill = "x", side = "right", anchor = "nw", pady = 5)

    vscOptionsButtonDefaultColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['default'])
    vscOptionsButtonDefaultColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonTitleColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['title'])
    vscOptionsButtonTitleColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonSubtitleColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['subtitle'])
    vscOptionsButtonSubtitleColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonBoldColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['bold'])
    vscOptionsButtonBoldColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonItalicColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['italic'])
    vscOptionsButtonItalicColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonUnderlineColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['underline'])
    vscOptionsButtonUnderlineColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    vscOptionsButtonOverstrikeColor = LabelButton(rightVscOptionsHolderFrame, width = 10, relief = "flat", bg = tempColorConfig['overstrike'])
    vscOptionsButtonOverstrikeColor.pack(side = "top", anchor = "nw", fill = "x", padx = 5, pady = 1)

    #Frame and Listbox / Text for themes demonstratios
    themesFrame2 = Frame(themeTab, highlightbackground="#cccccc", highlightthickness=0.5)
    themesFrame2.pack(expand = 1, fill = "both", side = "top", padx = 10, pady = 15, ipadx = 5, ipady = 5, anchor = "ne")
    themesLabel2 = Label(themeTab, text = "Sample")
    themesLabel2.place(anchor = "w", x = 285, y = 15)

    themeSampleHolder = Frame(themesFrame2)
    themeSampleHolder.pack(expand = 1, fill = "both", padx = 5, anchor = "nw")

    themeSampleSide = builder.createSide(master = themeSampleHolder)
    themeSampleSide.pack(expand = 0, side = "left", fill = "both", pady = 10)
    
    #Sample dir structure in sample side
    readDir(themeSampleSide)

    themeSampleText = builder.createText(master=themeSampleHolder)
    #themeSampleText.config(richText = True)
    themeSampleText.pack(expand = 1, side = "left", fill = "both", pady = 10)
    Format(themeSampleText, themeSampleText)
    FastMenu(themeSampleText, themeSampleText)

    #Programar os botões dessa porra
    def comboboxThemeChange(event):
        textCallersAndKeys = {textOptionsButtonBGColor : 'bg', textOptionsButtonFGColor : 'fg', textOptionsButtonSelectBGColor : 'selectbackground', 
                            textOptionsButtonSelectFGColor : 'selectforeground', textOptionsButtonInsertBGColor : 'insertbackground'}
        sideCallersAndKeys = {sideOptionsButtonBGColor : 'bg', sideOptionsButtonFGColor : 'fg', sideOptionsButtonSelectBGColor : 'selectbackground', 
                            sideOptionsButtonSelectFGColor : 'selectforeground', sideOptionsButtonHighlightBGColor : 'highlightbackground', sideOptionsButtonHighlightFGColor : 'highlightforeground'}
        colorCallersAndKeys = {vscOptionsButtonDefaultColor : 'default', vscOptionsButtonTitleColor : 'title', vscOptionsButtonSubtitleColor : 'subtitle', 
                            vscOptionsButtonBoldColor : 'bold', vscOptionsButtonItalicColor : 'italic', vscOptionsButtonUnderlineColor : 'underline', vscOptionsButtonOverstrikeColor : 'overstrike'}
        
        tempConfig = ConfigManager().readConfig(toPath(join(expanduser("~/Documents/Notecalc"), "config.ini")), globalRead= False, theme=event.widget.get().lower())

        tempTextConfig = tempConfig["textConfig"]
        tempSideConfig = tempConfig["sideConfig"]
        tempColorConfig = tempConfig["colorConfig"]

        for caller, key in textCallersAndKeys.items():
            changeColors(configDict=tempTextConfig, caller = caller, key = key, target=themeSampleText, targetType='text', chooseColor=False)
        for caller, key in sideCallersAndKeys.items():
            changeColors(configDict=tempSideConfig, caller = caller, key = key, target=themeSampleSide, targetType='side', chooseColor=False)
        for caller, key in colorCallersAndKeys.items():
            changeColors(configDict=tempColorConfig, caller = caller, key = key, target=themeSampleText, targetType='font', chooseColor=False)
    
    def comboboxSidePrefixChange(event):
        tempConfig = ConfigManager().readConfig(toPath(join(expanduser("~/Documents/Notecalc"), "config.ini")), globalRead= False, sidePrefix=event.widget.get())

        prefix = {"upper" : tempConfig["cfgSideUpper"], "actual" : tempConfig["cfgSideActual"] , "folder" : tempConfig["cfgSideFolder"], "file" : tempConfig["cfgSideFile"]}
        
        tempUpperFolderPrefix = tempConfig["cfgSideUpper"]
        tempActualFolderPrefix = tempConfig["cfgSideActual"]
        tempFolderPrefix = tempConfig["cfgSideFolder"]
        tempFilePrefix = tempConfig["cfgSideFile"]

        readDir(themeSampleSide, prefix = prefix)
        
            
    textOptionsButtonBGColor.config(command=lambda: changeColors(
        textOptionsButtonBGColor, 'Text Background Color', tempTextConfig, 'bg', themeSampleText, 'text'))
    textOptionsButtonFGColor.config(command=lambda: changeColors(
        textOptionsButtonFGColor, 'Text Foreground Color', tempTextConfig, 'fg', themeSampleText, 'text'))
    textOptionsButtonSelectBGColor.config(command=lambda: changeColors(
        textOptionsButtonSelectBGColor, 'Text Select Background Color', tempTextConfig, 'selectbackground', themeSampleText, 'text'))
    textOptionsButtonSelectFGColor.config(command=lambda: changeColors(
        textOptionsButtonSelectFGColor, 'Text Select Foreground Color', tempTextConfig, 'selectforeground', themeSampleText, 'text'))
    textOptionsButtonInsertBGColor.config(command=lambda: changeColors(
        textOptionsButtonInsertBGColor, 'Text Insert Background Color', tempTextConfig, 'insertbackground', themeSampleText, 'text'))

    sideOptionsButtonBGColor.config(command=lambda: changeColors(
        sideOptionsButtonBGColor, 'Side Background Color', tempSideConfig, 'bg', themeSampleSide, 'side'))
    sideOptionsButtonFGColor.config(command=lambda: changeColors(
        sideOptionsButtonFGColor, 'Side Foreground Color', tempSideConfig, 'fg', themeSampleSide, 'side'))
    sideOptionsButtonSelectBGColor.config(command=lambda: changeColors(
        sideOptionsButtonSelectBGColor, 'Side Select Background Color', tempSideConfig, 'selectbackground', themeSampleSide, 'side'))
    sideOptionsButtonSelectFGColor.config(command=lambda: changeColors(
        sideOptionsButtonSelectFGColor, 'Side Select Foreground Color', tempSideConfig, 'selectforeground', themeSampleSide, 'side'))
    sideOptionsButtonHighlightBGColor.config(command=lambda: changeColors(
        sideOptionsButtonHighlightBGColor, 'Side Highlight Background Color', tempSideConfig, 'highlightbackground', themeSampleSide, 'side'))
    sideOptionsButtonHighlightFGColor.config(command=lambda: changeColors(
        sideOptionsButtonHighlightFGColor, 'Side Highlight Foreground Color', tempSideConfig, 'highlightforeground', themeSampleSide, 'side'))

    #vscOptionsButtonDefaultColor.config(command=lambda: changeColors(
    #    vscOptionsButtonDefaultColor, 'VSC Default Color', tempColorConfig, 'default', themeSampleText, 'font'))
    vscOptionsButtonTitleColor.config(command=lambda: changeColors(
        vscOptionsButtonTitleColor, 'VSC Title Color', tempColorConfig, 'title', themeSampleText, 'font'))
    vscOptionsButtonSubtitleColor.config(command=lambda: changeColors(
        vscOptionsButtonSubtitleColor, 'VSC Subtitle Color', tempColorConfig, 'subtitle', themeSampleText, 'font'))
    vscOptionsButtonBoldColor.config(command=lambda: changeColors(
        vscOptionsButtonBoldColor, 'VSC Bold Color', tempColorConfig, 'bold', themeSampleText, 'font'))
    vscOptionsButtonItalicColor.config(command=lambda: changeColors(
        vscOptionsButtonItalicColor, 'VSC Italic Color', tempColorConfig, 'italic', themeSampleText, 'font'))
    vscOptionsButtonUnderlineColor.config(command=lambda: changeColors(
        vscOptionsButtonUnderlineColor, 'VSC Underline Color', tempColorConfig, 'underline', themeSampleText, 'font'))
    vscOptionsButtonOverstrikeColor.config(command=lambda: changeColors(
        vscOptionsButtonOverstrikeColor, 'VSC Overstrike Color', tempColorConfig, 'overstrike', themeSampleText, 'font'))

    themesOptionMenu.bind("<<ComboboxSelected>>", comboboxThemeChange)
    sidePrefixMenu.bind("<<ComboboxSelected>>", comboboxSidePrefixChange)

    fontOptionsApply = ttk.Button(fontTab, text = "Apply")
    fontOptionsApply.pack(side = "top", anchor = "se", padx = 10, pady = 5)

    themesOptionsSave = ttk.Button(themeTab, text = "Save on Current") 
    themesOptionsSave.pack(side = "right", anchor = "se", padx = 10, pady = 5)

    themesOptionsNewtheme = ttk.Button(themeTab, text = "Save as new")
    themesOptionsNewtheme.pack(side = "right", anchor = "se", padx = 10, pady = 5)

    themesOptionsApply = ttk.Button(themeTab, text = "Apply")
    themesOptionsApply.pack(side = "right", anchor = "se", padx = 10, pady = 5)

    #Trakcs the first change of Tabs
    def onTabChange(event):
        widget = event.widget
        if widget.index(widget.select()) == 0:
            print("Aba 1")
        else:
            print("Aba 2")
    tabControl.bind("<<NotebookTabChanged>>", onTabChange)

