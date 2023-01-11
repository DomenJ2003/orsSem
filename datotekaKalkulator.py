from tkinter import *
from tkinter import filedialog
import kalkulator as kalk
import resevanjeRacunov as resevanje

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)
racuni = []
izpisanIndex = 0

def izpisiNaZaslon(izpisNaZaslonu, text):
    izpisNaZaslonu.config(text = text)

def izracunaj(izpisNaZaslonu):
    if (izpisNaZaslonu.cget("text") != ""):
        kalk.urediKorene(izpisNaZaslonu)
        kalk.urediPotence(izpisNaZaslonu)
        izpisNaZaslonuStr = izpisNaZaslonu.cget("text")
        rezultat = resevanje.resi(izpisNaZaslonuStr)
        izpisNaZaslonu.config(text=rezultat)
        # print("racunam")
        # izpisNaZaslonu.config(text = "rezultat")

def levo(izpisNaZaslonu):
    global izpisanIndex
    if (izpisNaZaslonu.cget("text") != ""):
        if(izpisanIndex == 0):
            izpisanIndex = len(racuni)-1
        else:
            izpisanIndex-=1
        izpisiNaZaslon(izpisNaZaslonu, racuni[izpisanIndex])

def desno(izpisNaZaslonu):
    global izpisanIndex
    if (izpisNaZaslonu.cget("text") != ""):
        if(izpisanIndex==len(racuni)-1):
            izpisanIndex = 0
        else:
            izpisanIndex+=1
        izpisiNaZaslon(izpisNaZaslonu, racuni[izpisanIndex])

def naloziDatoteko(izpisNaZaslonu):
    global izpisanIndex
    filename = filedialog.askopenfilename()
    try:
        file = open(filename, 'r')
        vrstice = file.readlines()
        for vrstica in vrstice:
            racuni.append(vrstica)
        izpisanIndex=0
        izpisiNaZaslon(izpisNaZaslonu, racuni[izpisanIndex])
    except:
        print("ni datoteke")


def layout(window):
    frame = Frame(window)
    Label(frame, text="Kalkulator", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    zaslon=PanedWindow(frame, orient = VERTICAL, height=150, width=550, bg="#d7fcfc")
    izpisNaZaslonu = Label(zaslon, font=fontTitle, text="", bg="#d7fcfc")
    zaslon.add(izpisNaZaslonu)
    zaslon.pack()
    Frame(frame, height=20, width=100, ).pack()
    tipke = Frame(frame)
    levoBtn = Button(tipke, height=6, width=8, text='<-', command=lambda: levo(izpisNaZaslonu))
    desnoBtn = Button(tipke, height=6, width=8, text='->', command=lambda: desno(izpisNaZaslonu))
    resiBtn = Button(tipke, height=6, width=8, text='=', command=lambda: izracunaj(izpisNaZaslonu))
    naloziBtn = Button(tipke, height=6, width=8, text='Open', command=lambda: naloziDatoteko(izpisNaZaslonu))
    
    levoBtn.grid(row=1, column=1)
    desnoBtn.grid(row=1, column=2)
    resiBtn.grid(row=2, column=1, columnspan=2)
    naloziBtn.grid(row=3, column=1, columnspan=2)

    tipke.pack()

    return frame