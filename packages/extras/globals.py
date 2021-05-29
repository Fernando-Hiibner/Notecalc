#Class that holds variables global for the entire code
class Globals():
    global font, side, vsc, hex
    font = None
    side = False
    vsc = True
    hex = None
    global sideDir, currentWorkingDirectory
    sideDir = None
    currentWorkingDirectory = None
    global simbols
    simbols = {
        "Matemática": ["Ω", "π", "√", "≠", "≅", "α", "∈", "∋", "∉", "∌", "∆", "∪", "∩", "⋃", "⊂", "⊃", "⊄", "⊅", "⊆", "⊇", "⊊", "⊉", "≥", "≤", "∅", "∑", "∀"],
        "Matemática 2": ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
        "Frações": ["⅟", "¼", "½", "¾", "⅓", "⅔", "⅕", "⅖", "⅗", "⅘", "⅙", "⅚", "⅐", "⅛", "⅜", "⅝", "⅞", "⅑", "⅒", "↉"],
        "Setas": ["←", "→", "↑", "↓", "↖", "↗", "↙", "↘", "↔", "↩", "↪", "↰", "↱", "↲", "↳"],
        "Quadrados": ["▢", "▥", "■", "▣", "▦", "□", "▤", "▧", "▨", "▬", "▩", "▮", "◆"],
        "Triangulos": ["▲", "◀", "▶", "▼", "△", "◁", "▷", "▽"],
        "Circulos": ["◌", "●", "○", "◍", "◉", "◎"],
        "Porções": ["◖", "◗", "◓", "◐", "◑", "◒", "◕", "◔", "◩", "◪", "◧", "◨", "◲", "◳", "◱", "◰", "◶", "◷", "◵", "◴"]}
    # Configs Variables
    global theme
    theme = "default"
    global sidePrefix, configSideUpperFolderPrefix, configSideActualFolderPrefix, configSideFolderPrefix, configSideFilePrefix
    sidePrefix = "SidePrefix1"
    configSideUpperFolderPrefix = None
    configSideActualFolderPrefix = None
    configSideFolderPrefix = None
    configSideFilePrefix = None
    global colorConfig
    colorConfig = {"default": "#000000", "title": "#af00db", "subtitle": "#0000ff",
                    "bold": "#ce8349", "italic": "#008000", "underline": "#267e99", "overstrike": "#a31515"}
    global textConfig
    textConfig = {"tab": '1c', "bg": 'SystemWindow', "fg": 'black',
                   "selectbackground": '#dddddd', "selectforeground": 'black', "insertbackground": 'black'}
    global pannedWindowBGConfig
    pannedWindowBGConfig = "#f3f3f3"
    global sideConfig
    sideConfig = {"family": "Courier New", "size": "10", "bg": '#f3f3f3',
                  "fg": '#333333', "selectbackground": '#dddddd', "selectforeground": 'black', "highlightbackground" : "#dddddd", "highlightforeground" : "#333333"}
    #O tema dark que vai vir por padrão
    global darkColorConfig
    darkColorConfig = {"default": "#cccccc", "title": "#b96fb4", "subtitle": "#499cb3",
                    "bold": "#ce8349", "italic": "#6a9955", "underline": "#3ac9a3", "overstrike": "#dcdcaa"}

    global darkPannedWindowBGConfig
    darkPannedWindowBGConfig = "#1e1e1e"

    global darkTextConfig
    darkTextConfig = {"tab": '1c', "bg": '#1e1e1e', "fg": '#cccccc',
                   "selectbackground": '#264f78', "selectforeground": '#cccccc', "insertbackground": '#cccccc'}

    global darkSideConfig
    darkSideConfig = {"family": "Courier New", "size": "10", "bg": '#252526',
                  "fg": '#cccccc', "selectbackground": '#3e3e3e', "selectforeground": '#cccccc', "highlightbackground" : "#3e3e3e", "highlightforeground" : "#cccccc"}
