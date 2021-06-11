from tkinter import Frame, Label, IntVar, Checkbutton, PanedWindow
from tkinter import ttk
from tkinter.font import Font, families
from tkinter.colorchooser import Chooser, askcolor

from configparser import ConfigParser
from os import listdir, getcwd
from os.path import expanduser, join, basename, isdir, join

from ..extras import globals
from ..mywidgets.my_widgets import HighlightListBox, LabelButton
from ..managers.builder_manager import MainBuilder
from ..managers.config_manager import ConfigManager
from ..extras.utilities import toPath, getIcon


class LocalConfigs():
    def __init__(self):
        self.tempFont = globals.font
        self.tempVscConfig = globals.vsc
        self.tempTextConfig = globals.textConfig
        self.tempSideConfig = globals.sideConfig
        self.tempColorConfig = globals.colorConfig
        self.tempPannedBGColor = {"bg" : globals.pannedWindowBGConfig}

        self.tempUpperFolderPrefix = globals.configSideUpperFolderPrefix
        self.tempActualFolderPrefix = globals.configSideActualFolderPrefix
        self.tempFolderPrefix = globals.configSideFolderPrefix
        self.tempFilePrefix = globals.configSideFilePrefix

    def returnChanges(self):
        localVars = self.vars()
        globalsVars = {
            "font": globals.font,
            "vsc": globals.vsc,
            "textConfig": globals.textConfig,
            "sideConfig": globals.sideConfig,
            "colorConfig": globals.colorConfig,
            "configSideUpperFolderPrefix": globals.configSideUpperFolderPrefix,
            "configSideActualFolderPrefix": globals.configSideActualFolderPrefix,
            "configSideFolderPrefix": globals.configSideFolderPrefix,
            "configSideFilePrefix": globals.configSideFilePrefix
        }
        modifiedVars = dict()
        for key in localVars.keys():
            if localVars[key] != globalsVars[key]:
                modifiedVars[key] = localVars[key]


class FontTabApp():
    def __init__(self, configs, configManager, root, fontTab):
        # Frame and Listbox for Font and Font Size
        self.fontsFrame1 = Frame(
            fontTab, highlightbackground="#cccccc", highlightthickness=0.5)
        self.fontsFrame1.pack(fill="both", side="left",
                              padx=10, pady=15, ipadx=5, ipady=5, anchor="nw")
        self.fontsLabel1 = Label(fontTab, text="Font / Size")
        self.fontsLabel1.place(anchor="w", x=15, y=15)

        self.fontsListbox = HighlightListBox(
            self.fontsFrame1, relief="flat", activestyle="none", width=25, exportselection=False)
        self.fontsListbox.config(width=25)

        self.lastSelectedFontsIndex = -1
        for self.fontFamily in families():
            self.fontsListbox.insert("end", self.fontFamily)
            if self.fontFamily == configs.tempFont.cget("family"):
                self.lastSelectedFontsIndex = self.fontsListbox.size() - 1
        self.fontsListbox.select_set(self.lastSelectedFontsIndex)
        self.fontsListbox.insert("end", "", active=False)
        self.fontsListbox.pack(expand=1, fill="both",
                               padx=5, pady=20, anchor="nw")

        self.fontSizeLabel = Label(self.fontsFrame1, text="Size:", anchor="w")
        self.fontSizeLabel.pack(fill="x", anchor="w", side="left")

        self.possibleFontSizes = [8, 9, 10, 11, 12,
                                  14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.fontSizeCombobox = ttk.Combobox(
            self.fontsFrame1, value=self.possibleFontSizes)
        self.fontSizeCombobox.current(
            self.possibleFontSizes.index(configs.tempFont.cget("size")))
        self.fontSizeCombobox.pack(expand=1, fill="x", anchor="w", side="left")

        self.vscCheckIntVar = IntVar(root, value=configs.tempVscConfig)
        self.fontVSCCheckButton = Checkbutton(
            self.fontsFrame1, text="VSC", variable=self.vscCheckIntVar, onvalue=1, offvalue=0)
        self.fontVSCCheckButton.pack(
            expand=1, fill="x", anchor="w", side="left")

        # Frame and Text for Font sample
        self.fontsFrame2 = Frame(
            fontTab, highlightbackground="#cccccc", highlightthickness=0.5)
        self.fontsFrame2.pack(expand=1, fill="both", side="top",
                              padx=10, pady=15, ipadx=5, ipady=5, anchor="ne")
        self.fontsFrame2.pack_propagate(False)

        self.fontsLabel2 = Label(fontTab, text="Editable Sample")
        self.fontsLabel2.place(anchor="w", x=285, y=15)

        self.fontSampleText = MainBuilder.createText(
            self, master=self.fontsFrame2, textConfig=configs.tempTextConfig, font=configs.tempFont)
        self.fontSampleText.config(richText=True)
        self.fontSampleText.pack(expand=1, fill="both", padx=5, pady=10)

        self.fontsListbox.bind(
            "<<ListboxSelect>>", lambda event: self.getSelectedFontFromListbox(configs, event))
        self.fontSizeCombobox.bind(
            "<<ComboboxSelected>>", lambda event: self.getFontSizeFromCombobox(configs, event))
        self.fontVSCCheckButton.config(
            command=lambda vsc=self.vscCheckIntVar.get(): self.fontChanges(configs, vsc=vsc))

        self.fontApplyButtonFrame = Frame(fontTab)
        self.fontApplyButtonFrame.pack(
            fill="both", side="top", anchor="se", padx=10, pady=5)
        self.fontOptionsApply = ttk.Button(
            self.fontApplyButtonFrame, text="Apply")
        self.fontOptionsApply.pack(anchor="se")
        # self.fontOptionsApply.pack(side = "top", anchor = "se", padx = 10, pady = 5)

    def getSelectedFontFromListbox(self, configs, event):
        widget = event.widget
        self.lastSelectedFontsIndex = int(widget.curselection()[0])
        return self.fontChanges(configs, selectedFont=widget.get(self.lastSelectedFontsIndex))

    def getFontSizeFromCombobox(self, configs, event):
        return self.fontChanges(configs, size=event.widget.get())

    def fontChanges(self, configs, **kw):
        if 'selectedFont' in kw.keys():
            selectedFont = kw.pop('selectedFont')
        elif self.lastSelectedFontsIndex != -1:
            selectedFont = self.fontsListbox.get(self.lastSelectedFontsIndex)
        else:
            selectedFont = configs.tempFont.cget("family")

        if 'size' in kw.keys():
            size = kw.pop('size')
        else:
            size = self.fontSizeCombobox.get()

        configs.tempFont.config(family=selectedFont, size=size)
        self.fontSampleText.config(font=configs.tempFont)

        if 'vsc' in kw.keys():
            print("Oi")
            vsc = kw.pop('vsc')
            if vsc == 1:
                self.tempVscConfig = True
                # Executar a mudança de vsc
            else:
                self.tempVscConfig = False
                # Executar a mudanca de vsc


class ThemeTabApp(MainBuilder):
    def __init__(self, configs, configManager, root, themeTab):
        self.themeMainHolderFrame = Frame(themeTab)
        self.themeMainHolderFrame.pack(
            fill="both", side="left", padx=10, pady=15, ipadx=5, ipady=20, anchor="nw")

        self.themesLeftFrame = Frame(
            self.themeMainHolderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
        self.themesLeftFrame.pack(expand=0, fill="both")
        self.themesLeftLabel = Label(themeTab, text="Themes")
        self.themesLeftLabel.place(anchor="w", x=15, y=15)

        #self.themesList = self.getThemes(configManager)
        self.themesList = configManager.getThemes()
        self.themesSelectionCombobox = ttk.Combobox(
            self.themesLeftFrame, value=self.themesList)
        self.themesSelectionCombobox.current(
            self.themesList.index(globals.theme))
        self.themesSelectionCombobox.pack(
            expand=0, fill="both", padx=5, pady=10, anchor="nw")

        # Main Frame and Label for Text Options
        self.themesTextOptionsLabel = Label(themeTab, text="Text Options")
        self.themesTextOptionsLabel.place(anchor="w", x=15, y=72)

        self.themesTextOptionsFrame = Frame(
            self.themeMainHolderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
        self.themesTextOptionsFrame.pack(fill="both", pady=15)

        # Left Frame and Labels for Text Options
        self.leftTextOptionsHolderFrame = Frame(self.themesTextOptionsFrame)
        self.leftTextOptionsHolderFrame.pack(
            expand=1, side="left", anchor="nw", pady=5)

        self.textOptionsLabelBGColor = Label(
            self.leftTextOptionsHolderFrame, text="Background:")
        self.textOptionsLabelBGColor.pack(side="top", anchor="nw", pady=1)

        self.textOptionsLabelPannedBGColor = Label(
            self.leftTextOptionsHolderFrame, text="Panned Background:")
        self.textOptionsLabelPannedBGColor.pack(side="top", anchor="nw", pady=1)

        self.textOptionsLabelFGColor = Label(
            self.leftTextOptionsHolderFrame, text="Foreground:")
        self.textOptionsLabelFGColor.pack(side="top", anchor="nw", pady=1)

        self.textOptionsLabelSelectBGColor = Label(
            self.leftTextOptionsHolderFrame, text="Select Background:")
        self.textOptionsLabelSelectBGColor.pack(
            side="top", anchor="nw", pady=1)

        self.textOptionsLabelSelectFGColor = Label(
            self.leftTextOptionsHolderFrame, text="Select Foreground:")
        self.textOptionsLabelSelectFGColor.pack(
            side="top", anchor="nw", pady=1)

        self.textOptionsLabelInsertBGColor = Label(
            self.leftTextOptionsHolderFrame, text="Insert Background:")
        self.textOptionsLabelInsertBGColor.pack(
            side="top", anchor="nw", pady=1)

        # Right frame and Labels for text options
        self.rightTextOptionsHolderFrame = Frame(self.themesTextOptionsFrame)
        self.rightTextOptionsHolderFrame.pack(
            expand=1, fill="x", side="right", anchor="nw", pady=5)

        self.textOptionsButtonBGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempTextConfig['bg'])
        self.textOptionsButtonBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.textOptionsButtonPannedBGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempPannedBGColor["bg"])
        self.textOptionsButtonPannedBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.textOptionsButtonFGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempTextConfig['fg'])
        self.textOptionsButtonFGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.textOptionsButtonSelectBGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempTextConfig['selectbackground'])
        self.textOptionsButtonSelectBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.textOptionsButtonSelectFGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempTextConfig['selectforeground'])
        self.textOptionsButtonSelectFGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.textOptionsButtonInsertBGColor = LabelButton(
            self.rightTextOptionsHolderFrame, width=10, relief="flat", bg=configs.tempTextConfig['insertbackground'])
        self.textOptionsButtonInsertBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        # Side prefix options
        self.sidePrefixOptionsLabel = Label(
            themeTab, text="Side Prefix Options")
        self.sidePrefixOptionsLabel.place(anchor="w", x=15, y=238)

        self.sidePrefixOptionsFrame = Frame(
            self.themeMainHolderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
        self.sidePrefixOptionsFrame.pack(fill="both")

        #self.sidePrefixList = self.getSidePrefix()
        self.sidePrefixList = configManager.getSidePrefix()
        self.sidePrefixSelectionCombobox = ttk.Combobox(
            self.sidePrefixOptionsFrame, value=self.sidePrefixList)
        self.sidePrefixSelectionCombobox.current(
            self.sidePrefixList.index(globals.sidePrefix))
        self.sidePrefixSelectionCombobox.pack(
            expand=1, fill="both", padx=5, pady=10, anchor="nw")

        # Main frame and labels for side option
        self.themesSideOptionsLabel = Label(themeTab, text="Side Options")
        self.themesSideOptionsLabel.place(anchor="w", x=15, y=298)

        self.themesSideOptionsFrame = Frame(
            self.themeMainHolderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
        self.themesSideOptionsFrame.pack(fill="both", pady=15)

        # Frame and labels for side options
        self.leftSideOptionsHolderFrame = Frame(self.themesSideOptionsFrame)
        self.leftSideOptionsHolderFrame.pack(
            expand=1, side="left", anchor="nw", pady=5)

        self.sideOptionsLabelBGColor = Label(
            self.leftSideOptionsHolderFrame, text="Background:")
        self.sideOptionsLabelBGColor.pack(side="top", anchor="nw", pady=1)

        self.sideOptionsLabelFGColor = Label(
            self.leftSideOptionsHolderFrame, text="Foreground:")
        self.sideOptionsLabelFGColor.pack(side="top", anchor="nw", pady=1)

        self.sideOptionsLabelSelectBGColor = Label(
            self.leftSideOptionsHolderFrame, text="Select Background:")
        self.sideOptionsLabelSelectBGColor.pack(
            side="top", anchor="nw", pady=1)

        self.sideOptionsLabelSelectFGColor = Label(
            self.leftSideOptionsHolderFrame, text="Select Foreground:")
        self.sideOptionsLabelSelectFGColor.pack(
            side="top", anchor="nw", pady=1)

        self.sideOptionsLabelHighlightBGColor = Label(
            self.leftSideOptionsHolderFrame, text="Highlight Background:")
        self.sideOptionsLabelHighlightBGColor.pack(
            side="top", anchor="nw", pady=1)

        self.sideOptionsLabelHighlightFGColor = Label(
            self.leftSideOptionsHolderFrame, text="Highlight Foreground:")
        self.sideOptionsLabelHighlightFGColor.pack(
            side="top", anchor="nw", pady=1)

        # Frame and buttons for side options
        self.rightSideOptionsHolderFrame = Frame(self.themesSideOptionsFrame)
        self.rightSideOptionsHolderFrame.pack(
            expand=1, fill="x", side="right", anchor="nw", pady=5)

        self.sideOptionsButtonBGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['bg'])
        self.sideOptionsButtonBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.sideOptionsButtonFGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['fg'])
        self.sideOptionsButtonFGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.sideOptionsButtonSelectBGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['selectbackground'])
        self.sideOptionsButtonSelectBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.sideOptionsButtonSelectFGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['selectforeground'])
        self.sideOptionsButtonSelectFGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.sideOptionsButtonHighlightBGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['highlightbackground'])
        self.sideOptionsButtonHighlightBGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.sideOptionsButtonHighlightFGColor = LabelButton(
            self.rightSideOptionsHolderFrame, width=10, relief="flat", bg=configs.tempSideConfig['highlightforeground'])
        self.sideOptionsButtonHighlightFGColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        # Vsc options
        self.themesVscOptionsFrame = Frame(
            self.themeMainHolderFrame, highlightbackground="#cccccc", highlightthickness=0.5)
        self.themesVscOptionsFrame.pack(expand=1, fill="both")

        self.themesVscOptionsLabel = Label(
            self.themeMainHolderFrame, text="VSC Options")
        self.themesVscOptionsLabel.place(anchor="w", x=10, y=448)

        # Label and and frame for texts
        self.leftVscOptionsHolderFrame = Frame(self.themesVscOptionsFrame)
        self.leftVscOptionsHolderFrame.pack(
            expand=1, side="left", anchor="nw", pady=5)

        # self.vscOptionsLabelDefaultColor = Label(
        #     self.leftVscOptionsHolderFrame, text="Default Color: ")
        # self.vscOptionsLabelDefaultColor.pack(side="top", anchor="nw", pady=1)

        self.vscOptionsLabelTitleColor = Label(
            self.leftVscOptionsHolderFrame, text="Title Color: ")
        self.vscOptionsLabelTitleColor.pack(side="top", anchor="nw", pady=1)

        self.vscOptionsLabelSubtitleColor = Label(
            self.leftVscOptionsHolderFrame, text="Subtitle Color: ")
        self.vscOptionsLabelSubtitleColor.pack(side="top", anchor="nw", pady=1)

        self.vscOptionsLabelBoldColor = Label(
            self.leftVscOptionsHolderFrame, text="Bold Color: ")
        self.vscOptionsLabelBoldColor.pack(side="top", anchor="nw", pady=1)

        self.vscOptionsLabelItalicColor = Label(
            self.leftVscOptionsHolderFrame, text="Italic Color: ")
        self.vscOptionsLabelItalicColor.pack(side="top", anchor="nw", pady=1)

        self.vscOptionsLabelUnderlineColor = Label(
            self.leftVscOptionsHolderFrame, text="Underline Color: ")
        self.vscOptionsLabelUnderlineColor.pack(
            side="top", anchor="nw", pady=1)

        self.vscOptionsLabelOverstrikeColor = Label(
            self.leftVscOptionsHolderFrame, text="Overstrike Color: ")
        self.vscOptionsLabelOverstrikeColor.pack(
            side="top", anchor="nw", pady=1)

        # Right Frame for Button
        self.rightVscOptionsHolderFrame = Frame(self.themesVscOptionsFrame)
        self.rightVscOptionsHolderFrame.pack(
            expand=1, fill="x", side="right", anchor="nw", pady=5)

        # self.vscOptionsButtonDefaultColor = LabelButton(
        #     self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['default'])
        # self.vscOptionsButtonDefaultColor.pack(
        #     side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonTitleColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['title'])
        self.vscOptionsButtonTitleColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonSubtitleColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['subtitle'])
        self.vscOptionsButtonSubtitleColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonBoldColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['bold'])
        self.vscOptionsButtonBoldColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonItalicColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['italic'])
        self.vscOptionsButtonItalicColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonUnderlineColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['underline'])
        self.vscOptionsButtonUnderlineColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        self.vscOptionsButtonOverstrikeColor = LabelButton(
            self.rightVscOptionsHolderFrame, width=10, relief="flat", bg=configs.tempColorConfig['overstrike'])
        self.vscOptionsButtonOverstrikeColor.pack(
            side="top", anchor="nw", fill="x", padx=5, pady=1)

        # Frame and Listbox / Text for themes demonstratios
        self.themesRightFrame = Frame(
            themeTab, highlightbackground="#cccccc", highlightthickness=0.5)
        self.themesRightFrame.pack(
            expand=1, fill="both", side="top", padx=10, pady=15, ipadx=5, ipady=5, anchor="ne")
        self.themesRightFrame.pack_propagate(False)
        self.themesRightLabel = Label(themeTab, text="Sample")
        self.themesRightLabel.place(anchor="w", x=285, y=15)

        self.themesLeftPannedWin = PanedWindow(self.themesRightFrame,
                                               relief="flat", bg=configs.tempPannedBGColor["bg"], borderwidth=0)
        self.themesLeftPannedWin.pack(fill="both", expand=1, padx=5, pady=10)
        self.themesRightPannedWin = PanedWindow(self.themesRightFrame,
                                                relief="flat", bg=configs.tempPannedBGColor["bg"], borderwidth=0)

        self.themesSampleSide = MainBuilder.createSide(
            self, master=self.themesLeftPannedWin)
        self.themesSampleSide.pack(expand=0, side="left", fill="both", pady=10)
        self.themesLeftPannedWin.add(self.themesSampleSide)
        self.themesLeftPannedWin.add(self.themesRightPannedWin)

        # Sample dir structure in sample side
        self.readDir(self.themesSampleSide)

        self.themesSampleText = MainBuilder.createText(
            self, master=self.themesRightPannedWin)
        self.themesSampleText.config(richText=True)
        self.themesSampleText.pack(expand=1, side="left", fill="both", pady=10)
        self.themesRightPannedWin.add(self.themesSampleText)

        # Programar os botões

        self.textOptionsButtonBGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonBGColor, 'Text Background Color', configs.tempTextConfig, 'bg', self.themesSampleText, 'text'))
        self.textOptionsButtonPannedBGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonPannedBGColor, 'Panned Background Color', configs.tempPannedBGColor, 'bg', self.themesLeftPannedWin, 'panned'))
        self.textOptionsButtonFGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonFGColor, 'Text Foreground Color', configs.tempTextConfig, 'fg', self.themesSampleText, 'text'))
        self.textOptionsButtonSelectBGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonSelectBGColor, 'Text Select Background Color', configs.tempTextConfig, 'selectbackground', self.themesSampleText, 'text'))
        self.textOptionsButtonSelectFGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonSelectFGColor, 'Text Select Foreground Color', configs.tempTextConfig, 'selectforeground', self.themesSampleText, 'text'))
        self.textOptionsButtonInsertBGColor.config(command=lambda: self.changeColors(
            root, self.textOptionsButtonInsertBGColor, 'Text Insert Background Color', configs.tempTextConfig, 'insertbackground', self.themesSampleText, 'text'))

        self.sideOptionsButtonBGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonBGColor, 'Side Background Color', configs.tempSideConfig, 'bg', self.themesSampleSide, 'side'))
        self.sideOptionsButtonFGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonFGColor, 'Side Foreground Color', configs.tempSideConfig, 'fg', self.themesSampleSide, 'side'))
        self.sideOptionsButtonSelectBGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonSelectBGColor, 'Side Select Background Color', configs.tempSideConfig, 'selectbackground', self.themesSampleSide, 'side'))
        self.sideOptionsButtonSelectFGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonSelectFGColor, 'Side Select Foreground Color', configs.tempSideConfig, 'selectforeground', self.themesSampleSide, 'side'))
        self.sideOptionsButtonHighlightBGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonHighlightBGColor, 'Side Highlight Background Color', configs.tempSideConfig, 'highlightbackground', self.themesSampleSide, 'side'))
        self.sideOptionsButtonHighlightFGColor.config(command=lambda: self.changeColors(
            root, self.sideOptionsButtonHighlightFGColor, 'Side Highlight Foreground Color', configs.tempSideConfig, 'highlightforeground', self.themesSampleSide, 'side'))

        # vscOptionsButtonDefaultColor.config(command=lambda: changeColors(
        #    vscOptionsButtonDefaultColor, 'VSC Default Color', tempColorConfig, 'default', themeSampleText, 'font'))
        self.vscOptionsButtonTitleColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonTitleColor, 'VSC Title Color', configs.tempColorConfig, 'title', self.themesSampleText, 'font'))
        self.vscOptionsButtonSubtitleColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonSubtitleColor, 'VSC Subtitle Color', configs.tempColorConfig, 'subtitle', self.themesSampleText, 'font'))
        self.vscOptionsButtonBoldColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonBoldColor, 'VSC Bold Color', configs.tempColorConfig, 'bold', self.themesSampleText, 'font'))
        self.vscOptionsButtonItalicColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonItalicColor, 'VSC Italic Color', configs.tempColorConfig, 'italic', self.themesSampleText, 'font'))
        self.vscOptionsButtonUnderlineColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonUnderlineColor, 'VSC Underline Color', configs.tempColorConfig, 'underline', self.themesSampleText, 'font'))
        self.vscOptionsButtonOverstrikeColor.config(command=lambda: self.changeColors(
            root, self.vscOptionsButtonOverstrikeColor, 'VSC Overstrike Color', configs.tempColorConfig, 'overstrike', self.themesSampleText, 'font'))

        self.themesSelectionCombobox.bind(
            "<<ComboboxSelected>>", lambda event: self.comboboxThemeChange(event, configs))
        self.sidePrefixSelectionCombobox.bind(
            "<<ComboboxSelected>>", lambda event: self.comboboxSidePrefixChange(event, configs))

        self.themesOptionsSave = ttk.Button(themeTab, text="Save on Current")
        self.themesOptionsSave.pack(side="right", anchor="se", padx=10, pady=5)
        #Salva, não pode salvar em cima dos quatro temas default (Default light, default dark, GitHub, HighContrast)

        self.themesOptionsNewtheme = ttk.Button(themeTab, text="Save as new")
        self.themesOptionsNewtheme.pack(
            side="right", anchor="se", padx=10, pady=5)
        #Salva um tema novo, não pode ter nome repetido e depois disso da um apply

        self.themesOptionsApply = ttk.Button(themeTab, text="Apply")
        self.themesOptionsApply.pack(
            side="right", anchor="se", padx=10, pady=5)
        #Mudar pra tela de options incluido as outras abas, e o programa principal, não salvar o tema mas caso não estiver salvo perguntar se quer salvar


    def readDir(self, listbox, **kw):
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
                listbox.insert("end", dir)
        for dir in listdir(dirALer):
            if not isdir(join(dirALer, dir)) and dir.endswith(".txt") or dir.endswith(".nxc") or dir.endswith(".json"):
                auxDir = dir
                dir = filePrefix+dir
                listbox.insert("end", dir)
                if(globals.currentWorkingDirectory != None):
                    if toPath(join(dirALer, auxDir)) == toPath(globals.currentWorkingDirectory):
                        listbox.select_set(listbox.size()-1)
        listbox.insert("end", "", active=False)

    def changeColors(self, parent=None, caller=None, title=None, configDict=None, key=None, target=None, targetType=None, chooseColor=True):
        if chooseColor == True:
            (rgb, hex) = askcolor(parent=parent,
                                  title=title, color=configDict[key])
        else:
            hex = configDict[key]
        if targetType == 'text' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
            configDict[key] = hex
            target.config(**{key: hex})
            if key == 'selectbackground':
                target.config({'inactiveselect': hex})
            if caller != None:
                caller.config(highlightbackground=hex, bg=hex)
        if targetType == 'side' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
            configDict[key] = hex
            target.config(**{key: hex})
            if caller != None:
                caller.config(highlightbackground=hex, bg=hex)
        if targetType == 'font' and key == 'padrao' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
            configDict[key] = hex
            target.config(foreground=hex)
            target.format.colorConfig = configDict
            target.fastMenu.colorDict = configDict
            if caller != None:
                caller.config(highlightbackground=hex, bg=hex)
            target.format.validateTags(target.tag_indexes("1.0", "end"))
        elif targetType == 'font' and ((hex != configDict[key] and chooseColor == True) or chooseColor == False):
            configDict[key] = hex
            target.format.colorConfig = configDict
            target.fastMenu.colorDict = configDict
            if caller != None:
                caller.config(highlightbackground=hex, bg=hex)
            target.format.validateTags(target.tag_indexes("1.0", "end"))
        elif targetType == "panned":
            configDict[key] = hex
            target.config(**{key: hex})
            if caller != None:
                caller.config(highlightbackground = hex, bg = hex)

    def comboboxThemeChange(self, event, configs):
        textCallersAndKeys = {self.textOptionsButtonBGColor: 'bg', self.textOptionsButtonFGColor: 'fg', self.textOptionsButtonSelectBGColor: 'selectbackground',
                              self.textOptionsButtonSelectFGColor: 'selectforeground', self.textOptionsButtonInsertBGColor: 'insertbackground'}
        sideCallersAndKeys = {self.sideOptionsButtonBGColor: 'bg', self.sideOptionsButtonFGColor: 'fg', self.sideOptionsButtonSelectBGColor: 'selectbackground',
                              self.sideOptionsButtonSelectFGColor: 'selectforeground', self.sideOptionsButtonHighlightBGColor: 'highlightbackground', self.sideOptionsButtonHighlightFGColor: 'highlightforeground'}
        colorCallersAndKeys = {self.vscOptionsButtonTitleColor: 'title', self.vscOptionsButtonSubtitleColor: 'subtitle',
                               self.vscOptionsButtonBoldColor: 'bold', self.vscOptionsButtonItalicColor: 'italic', self.vscOptionsButtonUnderlineColor: 'underline', self.vscOptionsButtonOverstrikeColor: 'overstrike'}

        tempConfig = ConfigManager().readTheme(event.widget.get())

        configs.tempTextConfig = tempConfig["textConfig"]
        configs.tempSideConfig = tempConfig["sideConfig"]
        configs.tempPannedBGColor = {"bg": tempConfig["pannedWindowBGConfig"]}
        configs.tempColorConfig = tempConfig["colorConfig"]

        for caller, key in textCallersAndKeys.items():
            self.changeColors(configDict=configs.tempTextConfig, caller=caller, key=key,
                              target=self.themesSampleText, targetType='text', chooseColor=False)
        for caller, key in sideCallersAndKeys.items():
            self.changeColors(configDict=configs.tempSideConfig, caller=caller, key=key,
                              target=self.themesSampleSide, targetType='side', chooseColor=False)
        for caller, key in colorCallersAndKeys.items():
            self.changeColors(configDict=configs.tempColorConfig, caller=caller, key=key,
                              target=self.themesSampleText, targetType='font', chooseColor=False)
        self.changeColors(configDict=configs.tempPannedBGColor, caller=self.textOptionsButtonPannedBGColor, key = "bg",
                            target=self.themesLeftPannedWin, targetType="panned", chooseColor=False)

    def comboboxSidePrefixChange(self, event, configs):
        tempConfig = ConfigManager().readPrefix(event.widget.get())

        prefix = {"upper": tempConfig["upper"], "actual": tempConfig["actual"],
                  "folder": tempConfig["folder"], "file": tempConfig["file"]}

        configs.tempUpperFolderPrefix = tempConfig["upper"]
        configs.tempActualFolderPrefix = tempConfig["actual"]
        configs.tempFolderPrefix = tempConfig["folder"]
        configs.tempFilePrefix = tempConfig["file"]

        self.readDir(self.themesSampleSide, prefix=prefix)


class OptionsWindow(MainBuilder):
    def __init__(self, mainRoot):
        self.mainRoot = mainRoot
        self.configManager = ConfigManager()

        self.root = MainBuilder.createTopLevel(
            mainRoot, geometry="900x640+0+0", minsizeX=800, minsizeY=640, title="Options")

        self.tabControl = ttk.Notebook(self.root)

        self.fontTab = ttk.Frame(self.tabControl)
        self.themeTab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.fontTab, text="Font")
        self.tabControl.add(self.themeTab, text="Theme")

        self.tabControl.pack(expand=1, fill="both", padx=5, pady=5)

        self.configs = LocalConfigs()
        self.fontTabApp = FontTabApp(self.configs, self.configManager, self.root, self.fontTab)
        self.themeTabApp = ThemeTabApp(self.configs, self.configManager, self.root, self.themeTab)

        self.tabControl.bind("<<NotebookTabChanged>>", self.onTabChange)

    def onTabChange(self, event):
        widget = event.widget
        if widget.index(widget.select()) == 0:
            print("Aba 1")
        else:
            print("Aba 2")
