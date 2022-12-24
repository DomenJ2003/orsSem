from tkinter import *
import pretvorbe as p

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)

def orF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i]=="1" or st2[i]=="1":
            rezultat += "1" 
        else:
            rezultat += "0"
    return rezultat

def norF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i] == 1 or st2[i]=="1":
            rezultat += "0" 
        else:
            rezultat += "1"
    return rezultat

def andF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i]=="1" and st2[i]=="1":
            rezultat += "1" 
        else:
            rezultat += "0"
    return rezultat

def nandF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i]=="1" and st2[i]=="1":
            rezultat += "0" 
        else:
            rezultat += "1"
    return rezultat

def xorF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i]=="1" and st2[i]=="0":
            rezultat += "1"
        elif st1[i]=="0" and st2[i]=="1":
            rezultat += "1"
        else:
            rezultat += "0" 
    return rezultat

def xandF(st1, st2):
    rezultat = ""
    for i in range(len(st1)):
        if st1[i]=="1" and st2[i]=="0":
            rezultat += "0"
        elif st1[i]=="0" and st2[i]=="1":
            rezultat += "0"
        else:
            rezultat += "1" 
    return rezultat



def izracun(stevilo1, stevilo2, sestav1, sestav2, logOperator, izpis):
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

    if (len(stevilo1)-len(stevilo2))<0:
        for i in range((len(stevilo2)-len(stevilo1))):
            stevilo1 = "0"+stevilo1
    elif (len(stevilo1)-len(stevilo2))>0:
        for i in range(len(stevilo1)-len(stevilo2)):
            stevilo2 = "0"+stevilo2


    print ("stevilo1: ")
    print (stevilo1)
    print ("stevilo2: ")
    print (stevilo2)

    if logOperator == "OR":
        izpis.config(text=orF(stevilo1, stevilo2))
    elif logOperator == "AND":
        izpis.config(text=andF(stevilo1, stevilo2))
    elif logOperator == "NAND":
        izpis.config(text=nandF(stevilo1, stevilo2))
    elif logOperator == "NOR":
        izpis.config(text=norF(stevilo1, stevilo2))
    elif logOperator == "XOR":
        izpis.config(text=xorF(stevilo1, stevilo2))
    elif logOperator == "XAND":
        izpis.config(text=xandF(stevilo1, stevilo2))
    
    

def layout(window):
    options = [
        "BIN",
        "OCT",
        "DEC",
        "HEX",
    ]
    optionsFunction = [
        "NOT",
        "OR",
        "AND",
        "NAND",
        "NOR",
        "XOR",
        "XAND"
    ]
    logOperacija = StringVar()
    logOperacija.set("NOT")

    frame = Frame(window)
    Label(frame, text="Logične funkcije", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    line1 = Frame(frame)
    vpis1 = Entry(line1)
    vpis1.insert(0, '')
    

    sestav1 = StringVar()
    sestav1.set("DEC")
    drop1 = OptionMenu(line1 , sestav1 , *options )
    drop1.grid(row=1, column=2)
    vpis1.grid(row=1, column=1)

    line1.pack()
    Frame(frame, height=20).pack()
    dropFunc = OptionMenu(frame , logOperacija , *optionsFunction )
    dropFunc.pack()
    Frame(frame, height=20).pack()
    line2 = Frame(frame)
    vpis2 = Entry(line2)
    vpis2.insert(0, '')
    sestav2 = StringVar()
    sestav2.set("DEC")
    drop2 = OptionMenu(line2 , sestav2 , *options )
    drop2.grid(row=1, column=2)
    vpis2.grid(row=1, column=1)
    line2.pack()
    Frame(frame, height=20).pack()
    Button(frame, text="=", command=lambda:izracun(vpis1.get(), vpis2.get(), sestav1.get(), sestav2.get(), logOperacija.get(), rezultat)).pack() 
    Frame(frame, height=20).pack()
    rezultat = Label(frame, text="")
    rezultat.pack()

    return frame