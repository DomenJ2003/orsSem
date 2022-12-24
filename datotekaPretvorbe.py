from tkinter import *
from tkinter import filedialog
import pretvorbe as p

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)
pretvorbe = []
izSistema = []
vSistem= []
izpisanIndex = 0

def izracun(vpis, izpis, izSistema, vSistem):
    if izSistema == 'DEC' and vSistem == 'DEC':
        izpis.config(text=vpis)
    elif izSistema == 'DEC' and vSistem == 'BIN':
        izpis.config(text=p.decToBin(int(vpis)))
    elif izSistema == 'DEC' and vSistem == 'OCT':
        izpis.config(text=p.dectoOct(int(vpis)))
    elif izSistema == 'DEC' and vSistem == 'HEX':
        izpis.config(text=p.decToHex(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'BIN':
        izpis.config(text=vpis)
    elif izSistema == 'BIN' and vSistem == 'DEC':
        izpis.config(text=p.binToDec(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'OCT':
        izpis.config(text=p.binToOct(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'HEX':
        izpis.config(text=p.binToHex(int(vpis)))
    elif izSistema == 'OCT' and vSistem == 'OCT':
        izpis.config(text=vpis)
    elif izSistema == 'OCT' and vSistem == 'DEC':
        izpis.config(text=p.octToDec(int(vpis)))
    elif izSistema == 'OCT' and vSistem == 'BIN':
        izpis.config(text=p.octToBin(list(vpis)))
    elif izSistema == 'OCT' and vSistem == 'HEX':
        izpis.config(text=p.octToHex(int(vpis)))
    elif izSistema == 'HEX' and vSistem == 'HEX':
        izpis.config(text=vpis)
    elif izSistema == 'HEX' and vSistem == 'DEC':
        izpis.config(text=p.hexToDec(vpis))
    elif izSistema == 'HEX' and vSistem == 'BIN':
        izpis.config(text=p.hexToBin(vpis))
    elif izSistema == 'HEX' and vSistem == 'OCT':
        izpis.config(text=p.hexToOct(vpis))

def izpisiNaZaslon(izpisNaZaslonu, sistem1, sistem2, izpis):
    global izpisanIndex
    izpisNaZaslonu.config(text = pretvorbe[izpisanIndex])
    sistem1.set(izSistema[izpisanIndex])
    sistem2.set(vSistem[izpisanIndex])
    izpis.config(text = "")
    
def levo(izpisNaZaslonu, sistem1, sistem2, izpis):
    global izpisanIndex
    if (izpisNaZaslonu.cget("text") != ""):
        if(izpisanIndex == 0):
            izpisanIndex = len(pretvorbe)-1
        else:
            izpisanIndex-=1
        izpisiNaZaslon(izpisNaZaslonu, sistem1, sistem2, izpis)

def desno(izpisNaZaslonu, sistem1, sistem2, izpis):
    global izpisanIndex
    if (izpisNaZaslonu.cget("text") != ""):
        if(izpisanIndex==len(pretvorbe)-1):
            izpisanIndex = 0
        else:
            izpisanIndex+=1
        izpisiNaZaslon(izpisNaZaslonu, sistem1, sistem2, izpis)

def naloziDatoteko(izpis, sestav1, sestav2, izpisRezultata):
    global izpisanIndex
    filename = filedialog.askopenfilename()
    try:
        file = open(filename, 'r')
        vrstice = file.readlines()
        for vrstica in vrstice:
            pretvorbe.append(vrstica[8:len(vrstica)-1])
            izSistema.append(vrstica[0:3])
            vSistem.append(vrstica[4:7])
        izpisanIndex=0
        izpisiNaZaslon(izpis, sestav1, sestav2, izpisRezultata)
    except:
        print("ni datoteke")
    
def layout(window):
    frame = Frame(window)
    Label(frame, text="Pretvorbe številskih sestavov", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    komandneTipke = Frame(frame)
    Button(komandneTipke, text='Open', command=lambda: naloziDatoteko(vpis1, sestav1, sestav2, vpis2)).grid(row=1, column=1, columnspan=2)
    Button(komandneTipke, text='<-', command=lambda: levo(vpis1, sestav1, sestav2, vpis2)).grid(row=2, column=1)
    Button(komandneTipke, text='->', command=lambda: desno(vpis1, sestav1, sestav2, vpis2)).grid(row=2, column=2)
    komandneTipke.pack()
    Frame(frame, height=20).pack()
    line1 = Frame(frame)
    vpis1 = Label(line1, font=fontTitle, text="")
    options = [
        "BIN",
        "OCT",
        "DEC",
        "HEX",
    ]

    sestav1 = StringVar()
    sestav1.set("DEC")
    drop1 = OptionMenu(line1 , sestav1 , *options )
    drop1.grid(row=1, column=2)
    vpis1.grid(row=1, column=1)

    line1.pack()
    Frame(frame, height=20).pack()
    Button(frame, text="=", command=lambda:izracun(vpis1.cget("text"), vpis2, sestav1.get(), sestav2.get())).pack()
    Frame(frame, height=20).pack()
    line2 = Frame(frame)
    vpis2 = Label(line2, font=fontTitle, text=" ")
    sestav2 = StringVar()
    sestav2.set("DEC")
    drop2 = OptionMenu(line2 , sestav2 , *options )
    drop2.grid(row=1, column=2)
    vpis2.grid(row=1, column=1)

    line2.pack()
    
    return frame