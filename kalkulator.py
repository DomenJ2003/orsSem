from tkinter import *

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)

def dodajNaZaslon(izpisNaZaslonu, znak):
    izpisNaZaslonu.config(text = izpisNaZaslonu.cget("text")+znak)

def izbrisiZaslon(izpisNaZaslonu):
    izpisNaZaslonu.config(text = "")

def izbrisiZadnjiZnak(izpisNaZaslonu):
    izpisNaZaslonu.config(text = izpisNaZaslonu.cget("text")[0:len(izpisNaZaslonu.cget("text"))-1])

def izracunaj(izpisNaZaslonu):
    # funkcija ki vrne rezultat iz string racuna
    print("racunam")
    izpisNaZaslonu.config(text = "rezultat")

def layout(window):
    frame = Frame(window)
    Label(frame, text="Kalkulator", font=fontTitle).pack()
    Frame(frame, height=20).pack()
    zaslon=PanedWindow(frame, orient = VERTICAL, height=150, width=550, bg="#d7fcfc")
    izpisNaZaslonu = Label(zaslon, font=fontTitle, text="", bg="#d7fcfc")
    zaslon.add(izpisNaZaslonu)
    
    tipke = Frame(frame)
    Button(tipke,font=fontText, command=lambda:izbrisiZadnjiZnak(izpisNaZaslonu), height=6, width=20, text="del").grid(row=1, column=1, columnspan=2)
    Button(tipke,font=fontText, command=lambda:izbrisiZaslon(izpisNaZaslonu), height=6, width=8, text="C").grid(row=1, column=3)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "("), height=6, width=8, text="(").grid(row=1, column=4)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, ")"), height=6, width=8, text=")").grid(row=1, column=5)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "7"), height=6, width=8, text="7").grid(row=2, column=1)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "8"), height=6, width=8, text="8").grid(row=2, column=2)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "9"), height=6, width=8, text="9").grid(row=2, column=3)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "/"), height=6, width=8, text="/").grid(row=2, column=4)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "^"), height=6, width=8, text="x^y").grid(row=2, column=5)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "4"), height=6, width=8, text="4").grid(row=3, column=1)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "5"), height=6, width=8, text="5").grid(row=3, column=2)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "6"), height=6, width=8, text="6").grid(row=3, column=3)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "*"), height=6, width=8, text="*").grid(row=3, column=4)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "√"), height=6, width=8, text="√").grid(row=3, column=5)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "3"), height=6, width=8, text="3").grid(row=4, column=1)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "2"), height=6, width=8, text="2").grid(row=4, column=2)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "1"), height=6, width=8, text="1").grid(row=4, column=3)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "+"), height=6, width=8, text="+").grid(row=4, column=4)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "%"), height=6, width=8, text="mod").grid(row=4, column=5)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "0"), height=6, width=8, text="0").grid(row=5, column=1)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "."), height=6, width=8, text=".").grid(row=5, column=2)
    Button(tipke,font=fontText, command=lambda:dodajNaZaslon(izpisNaZaslonu, "-"), height=6, width=8, text="-").grid(row=5, column=3)
    Button(tipke,font=fontText, command=lambda:izracunaj(izpisNaZaslonu), height=6, width=20, text="=").grid(row=5, column=4, columnspan=2)
    
    zaslon.pack()
    Frame(frame, height=20, width=100, ).pack()
    tipke.pack()


    return frame