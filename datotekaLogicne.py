
# ŠE ZA NAREDIT


from tkinter import *
from tkinter import filedialog
import logicne as l
import pretvorbe as p

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)
stevila1arr = []
sistem1arr = []
stevila2arr= []
sistem2arr = []
logicneArr = []
sistem3arr = []
izpisanIndex = 0


def izracun(stevilo1, stevilo2, sestav1, sestav2, logOperator, izpis, sestav3):
    if sestav1 == 'DEC':
        stevilo1 = p.decToBin(int(stevilo1))
    elif sestav1 == 'OCT':
        stevilo1 = p.octToBin(list(stevilo1))
    elif sestav1 == 'HEX':
        stevilo1 = p.hexToBin(stevilo1)

    if sestav2 == 'DEC':
        stevilo2 = p.decToBin(int(stevilo2))
    elif sestav2 == 'OCT':
        stevilo2 = p.octToBin(list(stevilo2))
    elif sestav2 == 'HEX':
        stevilo2 = p.hexToBin(stevilo2)

    if (len(stevilo1)-len(stevilo2)) < 0:
        for i in range((len(stevilo2)-len(stevilo1))):
            stevilo1 = "0"+stevilo1
    elif (len(stevilo1)-len(stevilo2)) > 0:
        for i in range(len(stevilo1)-len(stevilo2)):
            stevilo2 = "0"+stevilo2

    
    if logOperator == "OR":
        rezultatBin=l.orF(stevilo1, stevilo2)
    elif logOperator == "AND":
        rezultatBin=l.andF(stevilo1, stevilo2)
    elif logOperator == "NAND":
        rezultatBin=l.nandF(stevilo1, stevilo2)
    elif logOperator == "NOR":
        rezultatBin=l.norF(stevilo1, stevilo2)
    elif logOperator == "XOR":
        rezultatBin=l.xorF(stevilo1, stevilo2)
    elif logOperator == "XAND":
        rezultatBin=l.xandF(stevilo1, stevilo2)

    if sestav3 == "BIN":
        izpis.config(text=rezultatBin)
    elif sestav3 == "DEC":
        izpis.config(text=p.binToDec(int(rezultatBin)))
    elif sestav3 == "OCT":
        izpis.config(text=p.binToOct(int(rezultatBin)))
    elif sestav3 == "HEX":
        izpis.config(text=p.binToHex(int(rezultatBin)))

def levo(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis):
    global izpisanIndex
    if(izpisanIndex == 0):
        izpisanIndex = len(stevila1arr)-1
    else:
        izpisanIndex-=1
    izpisiNaZaslon(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis)

def desno(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis):
    global izpisanIndex
    if(izpisanIndex==len(stevila1arr)-1):
        izpisanIndex = 0
    else:
        izpisanIndex+=1
    izpisiNaZaslon(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis)


def izpisiNaZaslon(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis):
    global izpisanIndex
    stevilo1izpis.config(text = stevila1arr[izpisanIndex])
    stevilo2izpis.config(text = stevila2arr[izpisanIndex])

    sestav1izpis.set(sistem1arr[izpisanIndex])
    sestav2izpis.set(sistem2arr[izpisanIndex])
    sestav3izpis.set(sistem3arr[izpisanIndex])

    logicnaFizpis.set(logicneArr[izpisanIndex])


def naloziDatoteko(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis):
    global izpisanIndex
    filename = filedialog.askopenfilename()
    try:
        file = open(filename, 'r')
        vrstice = file.readlines()
        for vrstica in vrstice:
            podatki = vrstica.split(" ")
            sistem1arr.append(podatki[0])
            stevila1arr.append(podatki[1])
            sistem2arr.append(podatki[2])
            stevila2arr.append(podatki[3])
            logicneArr.append(podatki[4])
            sistem3bes = podatki[5]
            sistem3bes = sistem3bes[0: len(sistem3bes)-1]
            sistem3arr.append(sistem3bes)
        izpisanIndex=0
        izpisiNaZaslon(stevilo1izpis, sestav1izpis, stevilo2izpis, sestav2izpis, logicnaFizpis, sestav3izpis)
    except:
        print("ni datoteke")   

def layout(window):
    options = [
        "BIN",
        "OCT",
        "DEC",
        "HEX",
    ]
    optionsFunction = [
        "OR",
        "AND",
        "NAND",
        "NOR",
        "XOR",
        "XAND"
    ]
    logOperacija = StringVar()
    logOperacija.set("OR")

    frame = Frame(window)
    Label(frame, text="Logične funkcije", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    komandneTipke = Frame(frame)
    Button(komandneTipke, text='Open', command=lambda:naloziDatoteko(vpis1, sestav1, vpis2, sestav2, logOperacija, sestav3)).grid(row=1, column=1, columnspan=2)
    Button(komandneTipke, text='<-', command=lambda:levo(vpis1, sestav1, vpis2, sestav2, logOperacija, sestav3)).grid(row=2, column=1)
    Button(komandneTipke, text='->', command=lambda:desno(vpis1, sestav1, vpis2, sestav2, logOperacija, sestav3)).grid(row=2, column=2)
    komandneTipke.pack()
    Frame(frame, height=20).pack()
    line1 = Frame(frame)
    vpis1 = Label(line1, text="")

    sestav1 = StringVar()
    sestav1.set("DEC")
    drop1 = OptionMenu(line1, sestav1, *options)
    drop1.grid(row=1, column=2)
    vpis1.grid(row=1, column=1)

    line1.pack()
    Frame(frame, height=20).pack()
    dropFunc = OptionMenu(frame, logOperacija, *optionsFunction)
    dropFunc.pack()
    Frame(frame, height=20).pack()
    line2 = Frame(frame)
    vpis2 = Label(line2, text="")
    sestav2 = StringVar()
    sestav2.set("DEC")
    drop2 = OptionMenu(line2, sestav2, *options)
    drop2.grid(row=1, column=2)
    vpis2.grid(row=1, column=1)
    line2.pack()
    Frame(frame, height=20).pack()
    Button(frame, text="=", command=lambda: izracun(vpis1.cget("text"), vpis2.cget("text"), sestav1.get(), sestav2.get(), logOperacija.get(), rezultat, sestav3.get())).pack()
    sestav3 = StringVar()
    sestav3.set("DEC")
    drop3 = OptionMenu(frame, sestav3, *options)
    drop3.pack()
    Frame(frame, height=20).pack()
    rezultat = Label(frame, text="")
    rezultat.pack()

    return frame
