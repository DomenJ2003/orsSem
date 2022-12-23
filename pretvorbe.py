from tkinter import *

fontTitle = ("Moderen", 24)
fontText = ("Moderen", 14)


def izracun(vpis, izpis, izSistema, vSistem):
    if izSistema == 'DEC' and vSistem == 'DEC':
        izpis.config(text=vpis)
    elif izSistema == 'DEC' and vSistem == 'BIN':
        izpis.config(text=decToBin(int(vpis)))
    elif izSistema == 'DEC' and vSistem == 'OCT':
        izpis.config(text=dectoOct(int(vpis)))
    elif izSistema == 'DEC' and vSistem == 'HEX':
        izpis.config(text=decToHex(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'BIN':
        izpis.config(text=vpis)
    elif izSistema == 'BIN' and vSistem == 'DEC':
        izpis.config(text=binToDec(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'OCT':
        izpis.config(text=binToOct(int(vpis)))
    elif izSistema == 'BIN' and vSistem == 'HEX':
        izpis.config(text=binToHex(int(vpis)))
    elif izSistema == 'OCT' and vSistem == 'OCT':
        izpis.config(text=vpis)
    elif izSistema == 'OCT' and vSistem == 'DEC':
        izpis.config(text=octToDec(int(vpis)))
    elif izSistema == 'OCT' and vSistem == 'BIN':
        izpis.config(text=octToBin(list(vpis)))
    elif izSistema == 'OCT' and vSistem == 'HEX':
        izpis.config(text=octToHex(int(vpis)))
    elif izSistema == 'HEX' and vSistem == 'HEX':
        izpis.config(text=vpis)
    elif izSistema == 'HEX' and vSistem == 'DEC':
        izpis.config(text=hexToDec(vpis))
    elif izSistema == 'HEX' and vSistem == 'BIN':
        izpis.config(text=hexToBin(vpis))
    elif izSistema == 'HEX' and vSistem == 'OCT':
        izpis.config(text=hexToOct(vpis))

# Pretvorbe

# DEC


def decToBin(vpis):
    a = ''
    while (vpis > 0):
        dec = vpis % 2
        a += str(dec)
        vpis = vpis // 2
    return a[::-1]


def dectoOct(vpis):
    a = ''
    while (vpis != 0):
        a += str(vpis % 8)
        vpis = int(vpis / 8)
    return a[::-1]


def decToHex(vpis):
    tabela = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
              5: '5', 6: '6', 7: '7',
              8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F'}
    a = ''
    while (vpis > 0):
        ostanek = vpis % 16
        a = tabela[ostanek] + a
        vpis = vpis // 16
    return str(a)

# BIN


def binToDec(vpis):
    a, i = 0, 0
    while (vpis != 0):
        dec = vpis % 10
        a = a + dec * pow(2, i)
        vpis = vpis//10
        i += 1
    return str(a)


def binToOct(vpis):
    octSt = 0
    x = 1
    i = 0
    pozicija = 0
    octPolje = [0] * 32

    while vpis != 0:
        st = vpis % 10
        octSt += st * pow(2, i)
        i += 1
        vpis //= 10
        octPolje[pozicija] = octSt
        if x % 3 == 0:
            octSt = 0
            i = 0
            pozicija += 1
        x += 1
    a = ''
    for j in range(pozicija, -1, -1):
        a += str(octPolje[j])
    return a


def binToHex(vpis):
    temp = 0
    x = 1
    i = 1
    a = ''
    while vpis != 0:
        dec = vpis % 10
        temp = temp + (dec * x)
        if i % 4 == 0:
            if temp < 10:
                a += chr(temp + 48)
            else:
                a += chr(temp + 55)
            x = 1
            temp = 0
            i = 1
        else:
            x = x * 2
            i = i + 1
        vpis = int(vpis / 10)
    if i != 1:
        a += chr(temp + 48)
    return a[::-1]

# OCT


def octToDec(vpis):
    a = 0
    baza = 1
    while (vpis):
        zadnjaSt = vpis % 10
        vpis = int(vpis / 10)
        a += zadnjaSt * baza
        baza = baza * 8
    return str(a)


def octToBin(vpis):
    a = ''
    for i in range(len(vpis)):
        switcher = {
            0: "000",
            1: "001",
            2: "010",
            3: "011",
            4: "100",
            5: "101",
            6: "110",
            7: "111"
        }
        a += switcher.get(int(vpis[i]))
    return a


def octToHex(vpis):
    x = i = y = 0
    while vpis != 0:
        z = vpis % 10
        if z > 7:
            x = 1
            break
        y = y + (z * (8 ** i))
        i = i + 1
        vpis = int(vpis / 10)

    if x == 0:
        a = ""
        while y != 0:
            z = y % 16
            if z < 10:
                z = z + 48
            else:
                z = z + 55
            z = chr(z)
            a = a + z
            y = int(y / 16)
    return a[::-1]

# HEX


def hexToDec(vpis):
    tabela = {'0': 0, '1': 1, '2': 2, '3': 3,
              '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11,
              'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hexadecimal = vpis.strip().upper()
    a = 0
    dolzina = len(hexadecimal) - 1

    for i in hexadecimal:
        a = a + tabela[i]*16**dolzina
        dolzina = dolzina - 1

    return str(a)


def hexToBin(vpis):
    tabela = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    hexadecimal = vpis.strip().upper()
    a = ''
    for i in hexadecimal:
        a = a + tabela[i]
    return a


def hexToOct(vpis):
    return dectoOct(int(hexToDec(vpis)))

# Konec pretvorb


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
    drop1 = OptionMenu(line1, sestav1, *options)
    drop1.grid(row=1, column=2)
    vpis1.grid(row=1, column=1)

    line1.pack()
    Frame(frame, height=20).pack()
    Button(frame, text="=", command=lambda: izracun(
        vpis1.get(), vpis2, sestav1.get(), sestav2.get())).pack()
    Frame(frame, height=20).pack()
    line2 = Frame(frame)
    vpis2 = Label(line2, text=" ")
    sestav2 = StringVar()
    sestav2.set("DEC")
    drop2 = OptionMenu(line2, sestav2, *options)
    drop2.grid(row=1, column=2)
    vpis2.grid(row=1, column=1)

    line2.pack()

    return frame
