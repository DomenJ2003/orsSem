from tkinter import *

import datotekaKalkulator
import kalkulator
import logicne
import datotekaLogicne
import pretvorbe
import datotekaPretvorbe

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)


def clear(window):
    for widget in window.winfo_children():
        if (widget.winfo_class() != "Menu"):
            widget.destroy()


def openKalkulator(window):
    clear(window)
    kalkulator.layout(window).pack()


def openDatKalkulator(window):
    clear(window)
    datotekaKalkulator.layout(window).pack()


def openLogicne(window):
    clear(window)
    logicne.layout(window).pack()


def openDatLogicne(window):
    clear(window)
    datotekaLogicne.layout(window).pack()


def openPretvorbe(window):
    clear(window)
    pretvorbe.layout(window).pack()


def openDatPretvorbe(window):
    clear(window)
    datotekaPretvorbe.layout(window).pack()


window = Tk()
window.geometry("600x800")
window.title("Seminarska Naloga ORS")

menubar = Menu(window)

menuKalkulator = Menu(menubar, tearoff=0)
menuKalkulator.add_command(
    label="Kalkulator", command=lambda: openKalkulator(window))
menuKalkulator.add_command(
    label="Datoteka", command=lambda: openDatKalkulator(window))
menubar.add_cascade(label="Kalkulator", menu=menuKalkulator)

menuPretvorbe = Menu(menubar, tearoff=0)
menuPretvorbe.add_command(
    label="Pretvorbe", command=lambda: openPretvorbe(window))
menuPretvorbe.add_command(
    label="Datoteka", command=lambda: openDatPretvorbe(window))
menubar.add_cascade(label="Pretvorbe", menu=menuPretvorbe)

menuLogicne = Menu(menubar, tearoff=0)
menuLogicne.add_command(label="Logicne Funkcije",
                        command=lambda: openLogicne(window))
menuLogicne.add_command(
    label="Datoteka", command=lambda: openDatLogicne(window))

menubar.add_cascade(label="Logicne", menu=menuLogicne)

openKalkulator(window)

window.config(menu=menubar)
window.mainloop()
