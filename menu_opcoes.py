
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesnocancel, showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font, families
import globais
import pomo


#-------------------------------------#
from ast import literal_eval
from zipfile import ZipFile
#Importação das bibliotecas do sistema para salvar e abrir arquivos#
from os import mkdir, listdir, startfile
from os.path import expanduser, join
from pathlib import Path


class Opcoes():
    def apply(janela, Bloco, Side, Caixa, font, tempj, darktemp, vsctemp, salvartemp, fonttemp, fontstemp, ok):
        globais.darkmode = darktemp.get()
        globais.vsc = vsctemp.get()
        globais.LabelSalvar = salvartemp.get()
        globais.fontp = fonttemp
        globais.fontsp = fontstemp
        Opcoes.mudarpratudo(Caixa, globais.fontp, font)
        Opcoes.fontpa(globais.fontp)
        Opcoes.mudartamanho(Caixa, globais.fontsp, font)
        Opcoes.fontspa(globais.fontsp)
        Opcoes.darkm(Caixa, Bloco, Side)
        Opcoes.vscm(Caixa)
        if globais.darkmode == True:
            Opcoes.temapa('dark')
        else:
            Opcoes.temapa('original')
        if globais.vsc == True:
            Opcoes.corpa('ligado')
        else:
            Opcoes.corpa('desligado')
        Opcoes.salvarauto(janela, Caixa)
        if globais.LabelSalvar == True:
            Opcoes.salvarpa('ligado')
        else:
            Opcoes.salvarpa('desligado')
        if ok == True:
            globais.abertoconfig = False
            tempj.destroy()

    def mudarpratudo(Caixa, opcao, font):
        font.configure(family=opcao)
        Caixa.tag_config("tit", font=(
            font.cget("family"), font.cget("size")+4, "bold"))
        Caixa.tag_config("stit", font=(font.cget("family"),
                         font.cget("size")+2, "italic"))
        Caixa.tag_config("bt", font=(
            font.cget("family"), font.cget("size"), "bold"))
        Caixa.tag_config("it", font=(font.cget("family"),
                         font.cget("size"), "italic"))
        unfont = Font(family=font.cget("family"),
                      size=font.cget("size"), underline=1)
        Caixa.tag_config("un", font=unfont)
        tcfont = Font(family=font.cget("family"),
                      size=font.cget("size"), overstrike=1)
        Caixa.tag_config("tc", font=tcfont)

    def mudartamanho(Caixa, tamanho, font):
        font.configure(size=tamanho)
        Caixa.tag_config("tit", font=(
            font.cget("family"), font.cget("size")+4, "bold"))
        Caixa.tag_config("stit", font=(font.cget("family"),
                         font.cget("size")+2, "italic"))
        Caixa.tag_config("bt", font=(
            font.cget("family"), font.cget("size"), "bold"))
        Caixa.tag_config("it", font=(font.cget("family"),
                         font.cget("size"), "italic"))
        unfont = Font(family=font.cget("family"),
                      size=font.cget("size"), underline=1)
        Caixa.tag_config("un", font=unfont)
        tcfont = Font(family=font.cget("family"),
                      size=font.cget("size"), overstrike=1)
        Caixa.tag_config("tc", font=tcfont)

    def vscm(Caixa):
        if globais.vsc == False and globais.darkmode == False:
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("tit", foreground="black")
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("stit", foreground="black")
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("bt", foreground="black")
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("it", foreground="black")
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("un", foreground="black")
            # ,selectbackground="#185abc", selectforeground="white")
            Caixa.tag_config("tc", foreground="black")
        elif globais.vsc == False and globais.darkmode == True:
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("tit", foreground="#cccccc")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("stit", foreground="#cccccc")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("bt", foreground="#cccccc")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("it", foreground="#cccccc")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("un", foreground="#cccccc")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("tc", foreground="#cccccc")
        elif globais.vsc == True:
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("tit", foreground="#b96fb4")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("stit", foreground="#499cb3")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("bt", foreground="#ce8349")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("it", foreground="#6a9955")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("un", foreground="#3ac9a3")
            # ,selectbackground="#264f78", selectforeground="#cccccc")
            Caixa.tag_config("tc", foreground="#dcdcaa")
            if globais.darkmode == False:
                Caixa.tag_config("tit", foreground="#af00db")
                Caixa.tag_config("stit", foreground="#0000ff")
                Caixa.tag_config("bt", foreground="#ce8349")
                Caixa.tag_config("it", foreground="#008000")
                Caixa.tag_config("un", foreground="#267e99")
                Caixa.tag_config("tc", foreground="#a31515")

    def darkm(Caixa, Bloco, Side):
        if globais.darkmode == False:
            Caixa.configure(bg="SystemWindow", foreground="black", insertbackground="black",
                            selectbackground="#dddddd", selectforeground="black")
            Bloco.config(bg="#f3f3f3")
            Side.configure(bg="#f3f3f3", relief=FLAT, bd=0, highlightthickness=0,
                           foreground="#333333", selectbackground="#dddddd", selectforeground="black")
            Opcoes.vscm(Caixa)
        elif globais.darkmode == True:
            Caixa.configure(bg="#1e1e1e", foreground="#cccccc", insertbackground="#cccccc",
                            selectbackground="#264f78", selectforeground="#cccccc")
            Bloco.config(bg="#1e1e1e")
            Side.configure(bg="#252526", relief=FLAT, bd=0, highlightthickness=0,
                           foreground="#cccccc", selectbackground="#3e3e3e", selectforeground="#cccccc")
            Opcoes.vscm(Caixa)

    def saveas(janela, Caixa):
        #Com esse código abrirá uma janela do explorer para o usuario selecionar o diretorio onde quer salvar o arquivo e o nome dele#
        saveas = filedialog.asksaveasfilename(parent=janela, title='Selecione o local onde quer salvar o arquivo', defaultextension=(
            "*.nxc"), filetypes=(("Documentos Notecalc (*.nxc)", "*.nxc"), ("Documentos de Texto (*.txt)", "*.txt"), ("Todos Arquivos", "*.*")))
        texto = str(Caixa.dump("1.0", "end"))
        textonormal = Caixa.get('1.0', 'end-1c')
        globais.localabrir = saveas
        #Código responsavel por pegar o diretório obtido no código de cima e salvar o arquivo nele, com o nome especificado#
        with open(saveas, 'a+', encoding='utf-8') as saveas:
            saveas.truncate(0)
            if globais.localabrir[-4:] == ".nxc":
                saveas.write(texto)
            else:
                saveas.write(textonormal)
            saveas.close()

    def baozi():
        pass

    def salvarauto(janela, Caixa):
        if globais.LabelSalvar == True:
            def salvarefetivamente(janela, Caixa):
                if globais.localabrir == '' or globais.localabrir == None:
                    print("1 if")
                    try:
                        Opcoes.saveas(janela, Caixa)
                    except Exception as e:
                        print("E", e)
                        globais.localabrir == ''
                else:
                    print("2 if")
                    try:
                        textonormal = Caixa.get('1.0', 'end-1c')
                        texto = str(Caixa.dump("1.0", "end"))
                        with open(globais.localabrir, 'a+', encoding='utf-8') as salvar:
                            salvar.truncate(0)
                            if globais.localabrir[-4:] == ".nxc":
                                salvar.write(texto)
                            else:
                                salvar.write(textonormal)
                            salvar.close()
                    #Código que ele executa caso não consiga, ele automaticamente executa o código de salvar como#
                    except Exception as e:
                        if globais.localabrir != '':
                            pass
                        else:
                            globais.localabrir = ''
                            Opcoes.saveas(janela, Caixa)
                globais.salvarautoafter = janela.after(
                    180000, lambda: salvarefetivamente(janela, Caixa))  # 300000
                globais.salvou = True
            salvarefetivamente(janela, Caixa)
        elif globais.LabelSalvar == False or globais.LabelSalvar == None:
            janela.after_cancel(globais.salvarautoafter)

    def temapa(x):
        globais.temapadrao = ('default', '=', x)
        with open(globais.caminhoconfig, 'r', encoding='utf-8') as defp:
            texto = defp.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "vsc":
                    globais.vscpadrao = (par, e, valor)
                elif par == "fonte":
                    globais.fontepadrao = (par, e, valor)
                elif par == "fontesize":
                    globais.fontesizepadrao = (par, e, valor)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, 'w', encoding='utf-8') as mudarpadrao:
            mudarpadrao.truncate(0)
            mudarpadrao.write(str(configpadrao))
            mudarpadrao.close()

    def corpa(x):
        globais.vscpadrao = ('vsc', '=', x)
        with open(globais.caminhoconfig, 'r', encoding='utf-8') as defp:
            texto = defp.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "default":
                    globais.temapadrao = (par, e, valor)
                elif par == "fonte":
                    globais.fontepadrao = (par, e, valor)
                elif par == "fontesize":
                    globais.fontesizepadrao = (par, e, valor)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, 'w', encoding='utf-8') as mudarpadrao:
            mudarpadrao.truncate(0)
            mudarpadrao.write(str(configpadrao))
            mudarpadrao.close()

    def fontpa(x):
        globais.fontepadrao = ('fonte', '=', x)
        with open(globais.caminhoconfig, 'r', encoding='utf-8') as defp:
            texto = defp.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "default":
                    globais.temapadrao = (par, e, valor)
                elif par == "vsc":
                    globais.vscpadrao = (par, e, valor)
                elif par == "fontesize":
                    globais.fontesizepadrao = (par, e, valor)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, 'w', encoding='utf-8') as mudarpadrao:
            mudarpadrao.truncate(0)
            mudarpadrao.write(str(configpadrao))
            mudarpadrao.close()

    def fontspa(x):
        globais.fontesizepadrao = ('fontesize', '=', x)
        with open(globais.caminhoconfig, 'r', encoding='utf-8') as defp:
            texto = defp.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "default":
                    globais.temapadrao = (par, e, valor)
                elif par == "vsc":
                    globais.vscpadrao = (par, e, valor)
                elif par == "fonte":
                    globais.fontepadrao = (par, e, valor)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, 'w', encoding='utf-8') as mudarpadrao:
            mudarpadrao.truncate(0)
            mudarpadrao.write(str(configpadrao))
            mudarpadrao.close()

    def salvarpa(x):
        globais.salvarautopadrao = ('autosave', '=', x)
        with open(globais.caminhoconfig, 'r', encoding='utf-8') as defp:
            texto = defp.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "default":
                    globais.temapadrao = (par, e, valor)
                elif par == "vsc":
                    globais.vscpadrao = (par, e, valor)
                elif par == "fonte":
                    globais.fontepadrao = (par, e, valor)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, 'w', encoding='utf-8') as mudarpadrao:
            mudarpadrao.truncate(0)
            mudarpadrao.write(str(configpadrao))
            mudarpadrao.close()

    def __init__(self, janela, Caixa, font):
        self.janela = janela
        self.Caixa = Caixa
        globais.user = expanduser("~")
        globais.caminho = join(globais.user, "Documents", "Notecalc")
        globais.caminhoconfig = join(globais.caminho, "Config.txt")
        globais.salvarautoafter = janela.after(1000000, Opcoes.baozi)


def sec(janela, Caixa, menuc, Side, Bloco, Bloco2, font):
    globais.abertoconfig = True

    def fechando():
        globais.abertoconfig = False
        tempj.destroy()
    tempj = Tk()
    tempj.minsize(500, 600)
    tempj.resizable(False, False)
    tempj.title("Configurações")
    tempj.iconbitmap(globais.icon)
    tempj.protocol("WM_DELETE_WINDOW", fechando)
    global darktemp, vsctemp, salvartemp, fonttemp, fontstemp
    darktemp = BooleanVar(tempj)
    vsctemp = BooleanVar(tempj)
    salvartemp = BooleanVar(tempj)
    fonttemp = globais.fontp
    fontstemp = globais.fontsp
    if globais.darkmode == True:
        darktemp.set(True)
    else:
        darktemp.set(False)
    if globais.vsc == True:
        vsctemp.set(True)
    else:
        vsctemp.set(False)
    if globais.LabelSalvar == True:
        salvartemp.set(True)
    else:
        salvartemp.set(False)
    holder = Frame(tempj)
    holder.pack(fill=BOTH, expand=1, ipadx=5, ipady=5)
    abas = ttk.Notebook(holder, style="Baozi.TNotebook")
    #ABAS#
    fontej = Frame(tempj)
    abas.add(fontej, text="Configurações")
    abas.pack(expand=1, fill="both", padx=5, pady=5)
    #ABAS#
    #FONTELIST#
    #----------------------------------------------------------------------------------#
    fontejl = Frame(fontej, highlightbackground="#cccccc",
                    highlightthickness=0.5)
    fontejl.pack(anchor="n", pady=20, padx=10, side=LEFT)
    fontej.pack_propagate(False)
    Labellistfonte = Label(fontej, text="Fonte/Tamanho")
    Labellistfonte.place(anchor="w", x=15, y=20)
    placeholder = Label(fontejl, text="Fonte:")
    placeholder.place(anchor="w", y=20, x=5)
    Fonteslist = Listbox(fontejl, width=0, height=15, activestyle="none")
    Fonteslist.pack(pady=30, padx=5, ipadx=10, ipady=10)
    Fontelistscroll = Scrollbar(fontejl)
    Fontelistscroll.place(height=264, width=18, x=200, y=31)
    Fonteslist.config(yscrollcommand=Fontelistscroll.set)
    Fontelistscroll.config(command=Fonteslist.yview)
    opcoesfonte = families()
    for opcao in opcoesfonte:
        # label=opcao, command=lambda opcao=opcao: Options.fontpa(opcao))
        Fonteslist.insert(END, opcao)

    def fonteselect(evento):
        global fonttemp
        ev = evento.widget
        index = int(ev.curselection()[0])
        valor = ev.get(index)
        fonttemp = valor
    Fonteslist.bind("<<ListboxSelect>>", fonteselect)
    #----------------------------------------------------------------------------------#
    FontesizeEntryText = Label(fontejl, text="Tamanho:")
    FontesizeEntryText.place(x=5, y=300)
    FontesizeEntry = Entry(fontejl)
    FontesizeEntry.insert(0, fontstemp)
    FontesizeEntry.place(x=65, y=300, width=50)
    VSCCheck = Checkbutton(fontejl, text="VSC",
                           variable=vsctemp, onvalue=True, offvalue=False)
    VSCCheck.place(x=135, y=298)
    #-----------------------------------------------------------------------------------#
    SampleFrame = Frame(
        fontej, highlightbackground="#cccccc", highlightthickness=0.5)
    SampleFrame.pack(anchor='n', side=RIGHT, pady=20,
                     padx=5, fill=BOTH, expand=1)
    SampleText = Label(fontej, text="Amostra Fonte (Editavel)")
    SampleText.place(anchor="w", x=255, y=20)
    SampleFont = ScrolledText(SampleFrame, relief=GROOVE, width=30)
    with open(globais.sample, "r", encoding='utf-8') as sp:
        texto = sp.read()
        SampleFont.insert('1.0', texto)
        sp.close()
    SampleFont.pack(fill=BOTH, expand=1, pady=10, padx=5)

    def atualizarsample():
        try:
            fontstemp = int(FontesizeEntry.get())
        except:
            fontstemp = 12
        SampleFont.config(font=(fonttemp, fontstemp))
        tempj.after(200, atualizarsample)
    atualizarsample()
    #-----------------------------------------------------------------------------------#
    TemaFrame = Frame(fontej, highlightbackground="#cccccc",
                      highlightthickness=0.5, width=222, height=77)
    TemaFrame.place(x=10, y=356)
    TemaText = Label(fontej, text="Tema")
    TemaText.place(x=15, y=346)
    Radiobutton(fontej, text="Tema Original", variable=darktemp,
                value=False).place(x=15, y=372)
    Radiobutton(fontej, text="Tema Escuro", variable=darktemp,
                value=True).place(x=15, y=392)
    #-----------------------------------------------------------------------------------#
    SalvarFrame = Frame(fontej, highlightbackground="#cccccc",
                        highlightthickness=0.5, width=222, height=77)
    SalvarFrame.place(x=10, y=442)
    SalvarFrame = Label(fontej, text="Salvar Automaticamente")
    SalvarFrame.place(x=15, y=433)
    SalvarButton = Checkbutton(fontej, text="Salvar Automaticamente:",
                               variable=salvartemp, onvalue=True, offvalue=False)
    SalvarButton.place(x=15, y=449)
    SalvarHelp = Label(
        fontej, text="O arquivo sera salvo automaticamente\na cada 3 minutos", justify=LEFT)
    SalvarHelp.place(x=15, y=474)
    #-----------------------------------------------------------------------------------#
    placeholderbutton = Label(tempj).pack(pady=10)
    BotaoOk = ttk.Button(tempj, text="OK", command=lambda: Opcoes.apply(janela, Bloco, Side, Caixa, font,
                         tempj, darktemp, vsctemp, salvartemp, fonttemp, int(FontesizeEntry.get()), True)).place(x=243, y=560)
    BotaoAplicar = ttk.Button(tempj, text="Aplicar", command=lambda: Opcoes.apply(janela, Bloco, Side, Caixa,
                              font, tempj, darktemp, vsctemp, salvartemp, fonttemp, int(FontesizeEntry.get()), False)).place(x=330, y=560)
    BotaoCancel = ttk.Button(tempj, text="Cancelar",
                             command=tempj.destroy).place(x=417, y=560)

    tempj.mainloop()


def main(janela, Caixa, menuc, Side, Bloco, Bloco2, font):
    global darkm, vscm
    #Criar arquivo config#
    globais.user = expanduser("~")
    globais.caminho = join(globais.user, "Documents", "Notecalc")
    globais.caminhoconfig = join(globais.caminho, "Config.txt")
    globais.temapadrao = ('default', '=', 'original')
    globais.vscpadrao = ('vsc', '=', 'desligado')
    globais.salvarautopadrao = ('autosave', '=', 'desligado')
    globais.fontepadrao = ('fonte', '=', 'Consolas')
    globais.fontesizepadrao = ('fontesize', '=', '12')
    #---------------------------------------------------------------------#
    try:
        mkdir(globais.caminho)
        configpadrao = [globais.temapadrao, globais.vscpadrao,
                        globais.salvarautopadrao, globais.fontepadrao, globais.fontesizepadrao]
        with open(globais.caminhoconfig, "w", encoding='utf-8') as criarconfig:
            configpadrao = str(configpadrao)
            criarconfig.write(configpadrao)
            criarconfig.close()
        globais.fontp = "Calibri"
        globais.fontsp = 18
        globais.LabelSalvar = False
        globais.vsc = False
        globais.darkmode = False
        with ZipFile("externos.zip", "r") as ziparchive:
            ziparchive.extractall(globais.caminho)
    except:
        with open(globais.caminhoconfig, "r", encoding='utf-8') as lerconfig:
            texto = lerconfig.read()
            texto = literal_eval(texto)
            for par, e, valor in texto:
                if par == "default":
                    if valor == "original":
                        globais.darkmode = False
                    elif valor == "dark":
                        globais.darkmode = True
                elif par == "vsc":
                    if valor == "desligado":
                        globais.vsc = False
                    elif valor == "ligado":
                        globais.vsc = True
                elif par == "autosave":
                    if valor == "desligado":
                        globais.LabelSalvar = False
                    elif valor == "ligado":
                        globais.LabelSalvar = True
                elif par == "fonte":
                    globais.fontp = valor
                elif par == "fontesize":
                    globais.fontsp = int(valor)
            lerconfig.close()
    #---------------------------------------------------------------------#
    font = Font(family=globais.fontp, size=globais.fontsp)
    #---------------------------------------------------------------------#
    Opcoes(janela, Caixa, font)
    Opcoes.darkm(Caixa, Bloco, Side)
    Opcoes.vscm(Caixa)
    Opcoes.salvarauto(janela, Caixa)

    def abrirconfig(janela, Caixa, menuc, Side, Bloco, Bloco2, font):
        if globais.abertoconfig == False:
            sec(janela, Caixa, menuc, Side, Bloco, Bloco2, font)
        elif globais.abertoconfig == True:
            pass
    menuc.add_command(label="Opções", command=lambda: abrirconfig(
        janela, Caixa, menuc, Side, Bloco, Bloco2, font))
    janela.config(menu=menuc)
