from tkinter import *

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)

def izracun(vpis, izpis, izSistema, vSistem):
    print(vpis)
    print(izSistema)
    print(vSistem)
    # funkcija za pretvorbo sistemov vrne text
    izpis.config(text = "rezultat")

def layout(window):
    frame = Frame(window)
    Label(frame, text="Pretvorbe številskih sestavov", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    line1 = Frame(frame)
    vpis1 = Entry(line1)
    vpis1.insert(0, ' ')
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
    Button(frame, text="=", command=lambda:izracun(vpis1.get(), vpis2, sestav1.get(), sestav2.get())).pack()
    Frame(frame, height=20).pack()
    line2 = Frame(frame)
    vpis2 = Label(line2, text=" ")
    sestav2 = StringVar()
    sestav2.set("DEC")
    drop2 = OptionMenu(line2 , sestav2 , *options )
    drop2.grid(row=1, column=2)
    vpis2.grid(row=1, column=1)

    line2.pack()
    
    return frame