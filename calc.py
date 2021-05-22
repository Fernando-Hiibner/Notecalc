import globais
from tkinter import *
class calculadora():
    def __init__(self):
        global darkmcalc
        globais.abertocalc = True
        def fechando():
            globais.abertocalc = False
            self.Calc.destroy()
        self.Calc = Tk()
        self.Calc.geometry("450x575")
        self.Calc.title("Calculadora")
        self.Calc.resizable(False, False)
        self.Calc.iconbitmap(globais.icon)
        self.Calc.protocol("WM_DELETE_WINDOW", fechando)
        self.FrameCalc = Frame(self.Calc)
        self.FrameCalc.grid(row = 0, column = 0)
        self.Calc.grid_rowconfigure(0, weight = 1)
        self.Calc.grid_rowconfigure(1, weight = 1)
        self.Calc.grid_columnconfigure(0, weight = 1)
        self.FrameCalc.grid_columnconfigure(0, weight = 1)
        self.Resultado = Label(self.FrameCalc, text = '0', width = "15", height = "3", foreground='#303030', relief = GROOVE)
        self.Resultado.configure(font = "Arial 36")
        self.Resultado['bg'] = 'white'
        self.Resultado.grid(column = 0, row = 0, padx = 12, pady = 10)
        #------------------------------------------------------------#
        #Aqui criamos as definições que terão os códigos dos botões das calculadoras(desde os números ate os operadores)#
        def apertou(botao):
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = f'{botao}'
            else:
                self.Resultado['text'] = (self.Resultado['text'])+f"{botao}"
        def ponto():
            if '.' not in self.Resultado['text']:
                self.Resultado['text'] = self.Resultado['text'] + '.'
            elif '.' in self.Resultado['text']:
                pass
        def cls():
            self.Resultado['text'] = '0'
        def back():
            self.Resultado['text'] = self.Resultado['text'][0:-1]
        #Aqui começam as definições responsaveis pelo calculo#
        def equacao(op):
            global ope, x1
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            ope = op
        def igual():
            global ope, x1
            x2 = float(self.Resultado['text'])
            if ope == 1:
                resp = str(f"{x1+x2:.2f}")
            elif ope == 2:
                resp = str(f"{x1-x2:.2f}")
            elif ope == 3:
                resp = str(f"{x1*x2:.2f}")
            elif ope == 4:
                resp = str(f"{x1/x2:.2f}")
            elif ope == 5:
                resp = str(f"{x1*(x2/100):.2f}")
            self.Resultado['text'] = float(resp)
            self.Resultado['text'] = str(self.Resultado['text'])
        #------------------------------------------------------------#
        #Aqui começa a criação dos botões da calculadora#
        #Atalhos Numeros#
        self.Calc.bind("0", lambda event: apertou(0))
        self.Calc.bind("1", lambda event: apertou(1))
        self.Calc.bind("2", lambda event: apertou(2))
        self.Calc.bind("3", lambda event: apertou(3))
        self.Calc.bind("4", lambda event: apertou(4))
        self.Calc.bind("5", lambda event: apertou(5))
        self.Calc.bind("6", lambda event: apertou(6))
        self.Calc.bind("7", lambda event: apertou(7))
        self.Calc.bind("8", lambda event: apertou(8))
        self.Calc.bind("9", lambda event: apertou(9))
        #Atalhos operaçoes#
        self.Calc.bind("+", lambda event: equacao(1))
        self.Calc.bind("-", lambda event: equacao(2))
        self.Calc.bind("*", lambda event: equacao(3))
        self.Calc.bind("/", lambda event: equacao(4))
        self.Calc.bind("%", lambda event: equacao(5))
        self.Calc.bind(".", lambda event: ponto())
        self.Calc.bind("<Shift-BackSpace>", lambda event: cls())
        self.Calc.bind("<BackSpace>", lambda event: back())
        self.Calc.bind("<Return>", lambda event: igual())
        #-----------------------------------------------------------#
        self.FramebCalc = Frame(self.Calc)
        self.FramebCalc.grid(row = 1, column = 0)
        for i in range(5):
            self.FramebCalc.grid_rowconfigure(i, weight = 1)
            self.FramebCalc.grid_columnconfigure(i, weight = 1)
        self.seteb = Button(self.FramebCalc, text = "7", relief = GROOVE, width = "8", height = "4", command=lambda:apertou(7))
        self.seteb.configure(font = ("bold"))
        self.seteb['bg'] = '#fefefe'
        self.seteb.grid(row = 1, column = 0, padx = 3, pady = 3)
        
        self.oitob = Button(self.FramebCalc, text = "8", relief = GROOVE, width = "8", height = "4", command=lambda:apertou(8))
        self.oitob.configure(font = ("bold"))
        self.oitob['bg'] = '#fefefe'
        self.oitob.grid(row = 1, column = 1, padx = 3, pady = 3)
        
        self.noveb = Button(self.FramebCalc, text = "9", relief = GROOVE, width = "8", height = "4", command=lambda:apertou(9))
        self.noveb.configure(font = ("bold"))
        self.noveb['bg'] = '#fefefe'
        self.noveb.grid(row = 1, column = 2, padx = 3, pady = 3)
        
        self.cls = Button(self.FramebCalc, text = "CLS", relief = GROOVE,width = "8", height = "4", command = cls)
        self.cls.configure(font = ("bold"))
        self.cls['bg'] = '#fefefe'
        self.cls.grid(row = 1, column = 3, padx = 3, pady = 3)

        self.backb = Button(self.FramebCalc, text = "<<", relief = GROOVE,width = "8", height = "4", command = back)
        self.backb.configure(font = ("bold"))
        self.backb['bg'] = '#fefefe'
        self.backb.grid(row = 1, column = 4, padx = 3, pady = 3)
        #-----------------------------------------------------------#
        self.quatrob = Button(self.FramebCalc, text = "4", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(4))
        self.quatrob.configure(font = ("bold"))
        self.quatrob['bg'] = '#fefefe'
        self.quatrob.grid(row = 2, column = 0, padx = 3, pady = 3)
        
        self.cincob = Button(self.FramebCalc, text = "5", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(5))
        self.cincob.configure(font = ("bold"))
        self.cincob['bg'] = '#fefefe'
        self.cincob.grid(row = 2, column = 1, padx = 3, pady = 3)
        
        self.seisb = Button(self.FramebCalc, text = "6", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(6))
        self.seisb.configure(font = ("bold"))
        self.seisb['bg'] = '#fefefe'
        self.seisb.grid(row = 2, column = 2, padx = 3, pady = 3)
        
        self.barrab = Button(self.FramebCalc, text = "/", relief = GROOVE,width = "8", height = "4", command=lambda:equacao(4))
        self.barrab.configure(font = ("bold"))
        self.barrab['bg'] = '#fefefe'
        self.barrab.grid(row = 2, column = 3, padx = 3, pady = 3)

        self.vezesb = Button(self.FramebCalc, text = "X", relief = GROOVE,width = "8", height = "4", command=lambda:equacao(3))
        self.vezesb.configure(font = ("bold"))
        self.vezesb['bg'] = '#fefefe'
        self.vezesb.grid(row = 2, column = 4, padx = 3, pady = 3)
        #-----------------------------------------------------------#
        self.umb = Button(self.FramebCalc, text = "1", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(1))
        self.umb.configure(font = ("bold"))
        self.umb['bg'] = '#fefefe'
        self.umb.grid(row = 3, column = 0, padx = 3, pady = 3)
        
        self.doisb = Button(self.FramebCalc, text = "2", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(2))
        self.doisb.configure(font = ("bold"))
        self.doisb['bg'] = '#fefefe'
        self.doisb.grid(row = 3, column = 1, padx = 3, pady = 3)
        
        self.tresb = Button(self.FramebCalc, text = "3", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(3))
        self.tresb.configure(font = ("bold"))
        self.tresb['bg'] = '#fefefe'
        self.tresb.grid(row = 3, column = 2, padx = 3, pady = 3)
        
        self.menosb = Button(self.FramebCalc, text = "-", relief = GROOVE,width = "8", height = "4", command=lambda:equacao(2))
        self.menosb.configure(font = ("bold"))
        self.menosb['bg'] = '#fefefe'
        self.menosb.grid(row = 3, column = 3, padx = 3, pady = 3)

        self.maisb = Button(self.FramebCalc, text = "+", relief = GROOVE,width = "8", height = "4", command=lambda:equacao(1))
        self.maisb.configure(font = ("bold"))
        self.maisb['bg'] = '#fefefe'
        self.maisb.grid(row = 3, column = 4, padx = 3, pady = 3)
        #----------------------------------------------------------#
        self.pontob = Button(self.FramebCalc, text = ".", relief = GROOVE,width = "8", height = "4", command=ponto)
        self.pontob.configure(font = ("bold"))
        self.pontob['bg'] = '#fefefe'
        self.pontob.grid(row = 4, column = 0, padx = 3, pady = 3)
        
        self.zerob = Button(self.FramebCalc, text = "0", relief = GROOVE,width = "8", height = "4", command=lambda:apertou(0))
        self.zerob.configure(font = ("bold"))
        self.zerob['bg'] = '#fefefe'
        self.zerob.grid(row = 4, column = 1, padx = 3, pady = 3)

        self.darkb = Button(self.FramebCalc, text = "", relief = GROOVE,width = "8", height = "4",) #botao num lock#
        self.darkb.configure(font = ("bold"))
        self.darkb['bg'] = '#fefefe'
        self.darkb.grid(row = 4, column = 2, padx = 3, pady = 3)
        
        self.porb = Button(self.FramebCalc, text = "%", relief = GROOVE,width = "8", height = "4", command=lambda:equacao(5))
        self.porb.configure(font = ("bold"))
        self.porb['bg'] = '#fefefe'
        self.porb.grid(row = 4, column = 3, padx = 3, pady = 3)

        self.igualb = Button(self.FramebCalc, text = "=", relief = GROOVE,width = "8", height = "4", command = igual)
        self.igualb.configure(font = ("bold"))
        self.igualb['bg'] = '#fefefe'
        self.igualb.grid(row = 4, column = 4, padx = 3, pady = 3)
        #Darkmode#
        def darkmcalc():
            if globais.darkmode == False:
                self.Calc.config(bg = "SystemButtonFace")
                self.FrameCalc.config(bg ="SystemButtonFace")
                self.FramebCalc.config(bg ="SystemButtonFace")
                self.Resultado['bg'] = "white"
                self.Resultado.configure(foreground = "black")
                self.umb['bg'] = "white"
                self.umb.configure(foreground = "black")
                self.doisb['bg'] = "white"
                self.doisb.configure(foreground = "black")
                self.tresb['bg'] = "white"
                self.tresb.configure(foreground = "black")
                self.quatrob['bg'] = "white"
                self.quatrob.configure(foreground = "black")
                self.cincob['bg'] = "white"
                self.cincob.configure(foreground = "black")
                self.seisb['bg'] = "white"
                self.seisb.configure(foreground = "black")
                self.seteb['bg'] = "white"
                self.seteb.configure(foreground = "black")
                self.oitob['bg'] = "white"
                self.oitob.configure(foreground = "black")
                self.noveb['bg'] = "white"
                self.noveb.configure(foreground = "black")
                self.zerob['bg'] = "white"
                self.zerob.configure(foreground = "black")
                #Funcões Calculadora#
                self.maisb['bg'] = "white"
                self.maisb.configure(foreground = "black")
                self.pontob['bg'] = "white"
                self.pontob.configure(foreground = "black")
                self.menosb['bg'] = "white"
                self.menosb.configure(foreground = "black")
                self.vezesb['bg'] = "white"
                self.vezesb.configure(foreground = "black")
                self.barrab['bg'] = "white"
                self.barrab.configure(foreground = "black")
                self.porb['bg'] = "white"
                self.porb.configure(foreground = "black")
                self.cls['bg'] = "white"
                self.cls.configure(foreground = "black")
                self.backb['bg'] = "white"
                self.backb.configure(foreground = "black")
                self.darkb['bg'] = "white"
                self.darkb.configure(foreground = "black")
                self.igualb['bg'] = "white"
                self.igualb.configure(foreground = "black")
            elif globais.darkmode == True:
                self.Calc.config(bg = "#1e1e1e")
                self.FrameCalc.config(bg ="#1e1e1e")
                self.FramebCalc.config(bg ="#1e1e1e")
                self.Resultado['bg'] = "#323232"
                self.Resultado.configure(foreground = "#cccccc")
                self.umb['bg'] = "#1e1e1e"
                self.umb.configure(foreground = "#cccccc")
                self.doisb['bg'] = "#1e1e1e"
                self.doisb.configure(foreground = "#cccccc")
                self.tresb['bg'] = "#1e1e1e"
                self.tresb.configure(foreground = "#cccccc")
                self.quatrob['bg'] = "#1e1e1e"
                self.quatrob.configure(foreground = "#cccccc")
                self.cincob['bg'] = "#1e1e1e"
                self.cincob.configure(foreground = "#cccccc")
                self.seisb['bg'] = "#1e1e1e"
                self.seisb.configure(foreground = "#cccccc")
                self.seteb['bg'] = "#1e1e1e"
                self.seteb.configure(foreground = "#cccccc")
                self.oitob['bg'] = "#1e1e1e"
                self.oitob.configure(foreground = "#cccccc")
                self.noveb['bg'] = "#1e1e1e"
                self.noveb.configure(foreground = "#cccccc")
                self.zerob['bg'] = "#1e1e1e"
                self.zerob.configure(foreground = "#cccccc")
                #Funcões Calculadora#
                self.maisb['bg'] = "#323232"
                self.maisb.configure(foreground = "#cccccc")
                self.pontob['bg'] = "#323232"
                self.pontob.configure(foreground = "#cccccc")
                self.menosb['bg'] = "#323232"
                self.menosb.configure(foreground = "#cccccc")
                self.vezesb['bg'] = "#323232"
                self.vezesb.configure(foreground = "#cccccc")
                self.barrab['bg'] = "#323232"
                self.barrab.configure(foreground = "#cccccc")
                self.porb['bg'] = "#323232"
                self.porb.configure(foreground = "#cccccc")
                self.cls['bg'] = "#323232"
                self.cls.configure(foreground = "#cccccc")
                self.backb['bg'] = "#323232"
                self.backb.configure(foreground = "#cccccc")
                self.darkb['bg'] = "#323232"
                self.darkb.configure(foreground = "#cccccc")
                self.igualb['bg'] = "#323232"
                self.igualb.configure(foreground = "#cccccc")
            self.Calc.after(100, darkmcalc)
        darkmcalc()
        #MAINLOOP#
        self.Calc.mainloop()