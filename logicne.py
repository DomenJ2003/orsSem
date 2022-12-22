from tkinter import *

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)

def izracun(stevilo1, stevilo2, sestav1, sestav2, logOperator, izpis):
    izpis.config(text = "rezultat")    

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
    vpis1.insert(0, ' ')
    

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
    vpis2.insert(0, ' ')
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