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
    colorConfig = None
    global textConfig
    textConfig = None
    global pannedWindowBGConfig
    pannedWindowBGConfig = "#f3f3f3"
    global sideConfig
    sideConfig = None
    #O tema dark que vai vir por padrão
    global darkColorConfig
    darkColorConfig = None

    global darkPannedWindowBGConfig
    darkPannedWindowBGConfig = None

    global darkTextConfig
    darkTextConfig = None

    global darkSideConfig
    darkSideConfig = None
