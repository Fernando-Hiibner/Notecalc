#Notecalc#
#Renan Kawamoto | Fernando Hiibner#

#Importação as bibliotecas necessárias do Tkinter#
from tkinter import *
from sys import argv
from os.path import dirname, join

import side
import menu_arquivo as ma
import menu_editar as me
import menu_formatar as mf
import menu_rapido as mr
import menu_opcoes as mo
import menu_outros as mot
import menu_ajuda as maj
import onopen
import fonte as fo
import globais
#MAIN#
try:
    #Criação da Janela#
    janela = Tk()
    janela.minsize(450, 575)
    janela.geometry("900x575+0+0")
    janela.title("Notecalc Beta")
    globais.icon = dirname(argv[0])
    globais.sample = dirname(argv[0])
    globais.icon = join(globais.icon, "Notecalc.ico")
    globais.sample = join(globais.sample, "Sample Fonte.txt")
    janela.iconbitmap(globais.icon)

    Caixa, Side, Bloco, Bloco2 = side.main(janela)
    font = fo.main()
    Caixa.configure(font=font)

    try:
        onopen.abrir(janela, Caixa, argv[1])
    except:
        pass

    #Menu Master#
    menuc = Menu(janela)
    #Botões do Menu#
    ma.main(janela, Caixa, menuc)
    me.main(janela, Caixa, menuc)
    mf.main(font, janela, Caixa, menuc)
    mr.Main(janela, Caixa)
    mo.main(janela, Caixa, menuc, Side, Bloco, Bloco2, font)
    mot.main(janela, Caixa, menuc)
    maj.main(janela, menuc)
    janela.mainloop()


except Exception as e:
    print('Unexpected error:' + str(e))
    input()
