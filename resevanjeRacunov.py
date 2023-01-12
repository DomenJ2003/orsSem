def sestej(a,b):
    return a+b

def odstej(a,b):
    return a-b

def mnozenje(a,b):
    return a*b

def deljenje(a,b):
    return a/b

def module(a,b):
    return a%b

def poisciSteviloPredZminus(izraz, znak):
    index = izraz.index(znak)-1
    steviloP = ""
    while not(("*" in steviloP) or ("/" in steviloP) or("+" in steviloP) or("=" in steviloP)):
        steviloP = izraz[index]+steviloP
        index-=1
        if steviloP[0] == "-":
            index =-1
        if index==-1:
            steviloP = "*"+steviloP
            break
        
    steviloP = steviloP[1:]
    return steviloP

def poisciSteviloPredBrezMinus(izraz, znak):
    index = izraz.index(znak)-1
    steviloP = ""
    while not(("*" in steviloP) or ("/" in steviloP) or("+" in steviloP) or ("-" in steviloP) or("=" in steviloP)):
        steviloP = izraz[index]+steviloP
        index-=1
        if index==-1:
            steviloP = "*"+steviloP
            break
    steviloP = steviloP[1:]
    return steviloP

def poisciSteviloZa(izraz, znak):
    index = izraz.index(znak)+len(znak)
    steviloK = ""
    while not(("*" in steviloK) or ("/" in steviloK) or("+" in steviloK) or("-" in steviloK) or("=" in steviloK) or (")" in steviloK)):
        try:
            steviloK = steviloK + izraz[index]
            index+=1
        except:
            steviloK = steviloK+"*"
            break
    steviloK = steviloK[:-1]
    return steviloK

def resiOklepaje(a):
    if "+(" in a:
        a = a.replace("+(", "+")

    elif "+(-" in a:
        a = a.replace("+(-", "-")  
    elif "-(" in a:
        stevilaVoklepaju = []
        prviZnak =""
        novRacun = ""
        if "-(-" in a:
            stevilaVoklepaju.append(poisciSteviloZa(a, "-(-"))
            prviZnak = "-"
            novRacun = "+"+stevilaVoklepaju[0]
        else:
            stevilaVoklepaju.append(poisciSteviloZa(a, "-("))
            prviZnak = ""
            novRacun = "-"+stevilaVoklepaju[0]
        
        while True:

            stevilaVoklepajuStr = prviZnak + stevilaVoklepaju[0]
            
            for i in range(len(stevilaVoklepaju)):
                if i==0: continue
                if("-("+stevilaVoklepajuStr+"+" in a):
                    stevilaVoklepajuStr += "+"+stevilaVoklepaju[i]
                elif("-("+stevilaVoklepajuStr+"-" in a):
                    
                    stevilaVoklepajuStr += "-"+stevilaVoklepaju[i]
            if "-("+stevilaVoklepajuStr+")" in a:
                break
            if("-("+stevilaVoklepajuStr+"+" in a):
    
                naslednjeStevilo = poisciSteviloZa(a, "-("+stevilaVoklepajuStr+"+")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "+"

            elif("-("+stevilaVoklepajuStr+"-" in a):
                naslednjeStevilo = poisciSteviloZa(a, "-("+stevilaVoklepajuStr+"-")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "-"

            if naslednjiZnak == "-":
                naslednjiZnak = "+"
            else:
                naslednjiZnak = "-"
            novRacun = novRacun + naslednjiZnak + naslednjeStevilo
        a = a.replace(a[a.index("-("):a.index(")")+1], novRacun)
    elif ("*(-" in a):
        steviloPredOklepajem = poisciSteviloPredZminus(a, "*(-")
        if "-" in steviloPredOklepajem:
            negativniFaktor = True
            steviloPredOklepajem = steviloPredOklepajem[1:]
        else:
            negativniFaktor = False
        stevilaVoklepaju = []
        stevilaVoklepaju.append(poisciSteviloZa(a, "*(-"))
        if negativniFaktor:
            novRacun = stevilaVoklepaju[0] +"*"+steviloPredOklepajem
        else:
            novRacun = "-" + stevilaVoklepaju[0] +"*"+steviloPredOklepajem
        while True:
            stevilaVoklepajuStr = stevilaVoklepaju[0]
            for i in range(len(stevilaVoklepaju)):
                if i==0: continue
                if("*(-"+stevilaVoklepajuStr+"+" in a):
                    stevilaVoklepajuStr += "+"+stevilaVoklepaju[i]
                elif("*(-"+stevilaVoklepajuStr+"-" in a):
                    stevilaVoklepajuStr += "-"+stevilaVoklepaju[i]
            if stevilaVoklepajuStr+")" in a:
                break
            if("*(-"+stevilaVoklepajuStr+"+" in a):
                naslednjeStevilo = poisciSteviloZa(a, "*(-"+stevilaVoklepajuStr+"+")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "+"
                if negativniFaktor:
                    naslednjiZnak = "-"
            elif("*(-"+stevilaVoklepajuStr+"-" in a):
                naslednjeStevilo = poisciSteviloZa(a, "*(-"+stevilaVoklepajuStr+"-")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "-"
                if negativniFaktor:
                    naslednjiZnak = "+"
            novRacun = novRacun + naslednjiZnak + naslednjeStevilo +"*"+steviloPredOklepajem
        if negativniFaktor:
            novRacun = "+"+novRacun
            a = a.replace(a[a.index("-"+steviloPredOklepajem+"*(-"):a.index(")")+1], novRacun)
        else:
            a = a.replace(a[a.index(steviloPredOklepajem+"*(-"):a.index(")")+1], novRacun)

    elif ("*(" in a):           
        steviloPredOklepajem = poisciSteviloPredZminus(a, "*(")
        if "-" in steviloPredOklepajem:
            negativniFaktor = True
            steviloPredOklepajem = steviloPredOklepajem[1:]
        else:
            negativniFaktor = False
        stevilaVoklepaju = []
        stevilaVoklepaju.append(poisciSteviloZa(a, "*("))
        if negativniFaktor:
            novRacun = "-" + stevilaVoklepaju[0] +"*"+steviloPredOklepajem
        else:
            novRacun = stevilaVoklepaju[0] +"*"+steviloPredOklepajem
        while True:
            stevilaVoklepajuStr = stevilaVoklepaju[0]
            for i in range(len(stevilaVoklepaju)):
                if i==0: continue
                if("*("+stevilaVoklepajuStr+"+" in a):
                    stevilaVoklepajuStr += "+"+stevilaVoklepaju[i]
                elif("*("+stevilaVoklepajuStr+"-" in a):
                    stevilaVoklepajuStr += "-"+stevilaVoklepaju[i]
            if stevilaVoklepajuStr+")" in a:
                break
            if("*("+stevilaVoklepajuStr+"+" in a):
                naslednjeStevilo = poisciSteviloZa(a, "*("+stevilaVoklepajuStr+"+")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "+"
                if negativniFaktor:
                    naslednjiZnak = "-"
            elif("*("+stevilaVoklepajuStr+"-" in a):
                naslednjeStevilo = poisciSteviloZa(a, "*("+stevilaVoklepajuStr+"-")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "-"
                if negativniFaktor:
                    naslednjiZnak = "+"
            novRacun = novRacun + naslednjiZnak + naslednjeStevilo +"*"+steviloPredOklepajem
        if negativniFaktor:
            novRacun = "+"+novRacun
            a = a.replace(a[a.index("-"+steviloPredOklepajem+"*("):a.index(")")+1], novRacun)
        else:
            a = a.replace(a[a.index(steviloPredOklepajem+"*("):a.index(")")+1], novRacun)
            
    elif ("/(-" in a):
        steviloPredOklepajem = poisciSteviloPredZminus(a, "/(-")
        if "-" in steviloPredOklepajem:
            negativniFaktor = True
            steviloPredOklepajem = steviloPredOklepajem[1:]
        else:
            negativniFaktor = False
        stevilaVoklepaju = []
        stevilaVoklepaju.append(poisciSteviloZa(a, "/(-"))
        if negativniFaktor:
            novRacun = stevilaVoklepaju[0] +"/"+steviloPredOklepajem
        else:
            novRacun = "-" + stevilaVoklepaju[0] +"/"+steviloPredOklepajem
        while True:
            stevilaVoklepajuStr = stevilaVoklepaju[0]
            for i in range(len(stevilaVoklepaju)):
                if i==0: continue
                if("/(-"+stevilaVoklepajuStr+"+" in a):
                    stevilaVoklepajuStr += "+"+stevilaVoklepaju[i]
                elif("/(-"+stevilaVoklepajuStr+"-" in a):
                    stevilaVoklepajuStr += "-"+stevilaVoklepaju[i]
            if stevilaVoklepajuStr+")" in a:
                break
            if("/(-"+stevilaVoklepajuStr+"+" in a):
                naslednjeStevilo = poisciSteviloZa(a, "/(-"+stevilaVoklepajuStr+"+")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "+"
                if negativniFaktor:
                    naslednjiZnak = "-"
            elif("/(-"+stevilaVoklepajuStr+"-" in a):
                naslednjeStevilo = poisciSteviloZa(a, "/(-"+stevilaVoklepajuStr+"-")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "-"
                if negativniFaktor:
                    naslednjiZnak = "+"
            novRacun = novRacun + naslednjiZnak + naslednjeStevilo +"/"+steviloPredOklepajem
        if negativniFaktor:
            novRacun = "+"+novRacun
            a = a.replace(a[a.index("-"+steviloPredOklepajem+"/(-"):a.index(")")+1], novRacun)
        else:
            a = a.replace(a[a.index(steviloPredOklepajem+"/(-"):a.index(")")+1], novRacun)
    elif ("/(" in a):    
        steviloPredOklepajem = poisciSteviloPredZminus(a, "/(")
        if "-" in steviloPredOklepajem:
            negativniFaktor = True
            steviloPredOklepajem = steviloPredOklepajem[1:]
        else:
            negativniFaktor = False
        stevilaVoklepaju = []
        stevilaVoklepaju.append(poisciSteviloZa(a, "/("))
        if negativniFaktor:
            novRacun = "-" + stevilaVoklepaju[0] +"/"+steviloPredOklepajem
        else:
            novRacun = stevilaVoklepaju[0] +"/"+steviloPredOklepajem
        while True:
            stevilaVoklepajuStr = stevilaVoklepaju[0]
            for i in range(len(stevilaVoklepaju)):
                if i==0: continue
                if("/("+stevilaVoklepajuStr+"+" in a):
                    stevilaVoklepajuStr += "+"+stevilaVoklepaju[i]
                elif("/("+stevilaVoklepajuStr+"-" in a):
                    stevilaVoklepajuStr += "-"+stevilaVoklepaju[i]
            if stevilaVoklepajuStr+")" in a:
                break
            if("/("+stevilaVoklepajuStr+"+" in a):
                naslednjeStevilo = poisciSteviloZa(a, "/("+stevilaVoklepajuStr+"+")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "+"
                if negativniFaktor:
                    naslednjiZnak = "-"
            elif("/("+stevilaVoklepajuStr+"-" in a):
                naslednjeStevilo = poisciSteviloZa(a, "/("+stevilaVoklepajuStr+"-")
                stevilaVoklepaju.append(naslednjeStevilo)
                naslednjiZnak = "-"
                if negativniFaktor:
                    naslednjiZnak = "+"
            novRacun = novRacun + naslednjiZnak + naslednjeStevilo +"/"+steviloPredOklepajem
    
        if negativniFaktor:
            novRacun = "+"+novRacun
            a = a.replace(a[a.index("-"+steviloPredOklepajem+"/("):a.index(")")+1], novRacun)
        else:
            a = a.replace(a[a.index(steviloPredOklepajem+"/("):a.index(")")+1], novRacun)

    while (("+-" in a) or ("-+" in a)):
        a = a.replace("+-", "-")
        a = a.replace("-+", "-")
    return a

def resiPotence(a):
    while "**" in a:
        rezultat = 1
        stPrej = poisciSteviloPredBrezMinus(a,"**")
        stPrejF = float(stPrej)
        stPotem = poisciSteviloZa(a, "**")
        stPotemF = int(stPotem)
        for i in range(stPotemF):
            rezultat *= stPrejF
        a = a.replace(stPrej+"**"+stPotem, str(rezultat))
    return a

def resiKorene(a):
    while("root(" in a):
        
        stevilo = poisciSteviloZa(a, "root(")
        steviloF = float(stevilo)
        ugib = steviloF / 2
        while abs(ugib * ugib - steviloF) > 0.00001:
            ugib = (ugib + steviloF / ugib) / 2
        rezultat = round(ugib, 5)
        a = a.replace("root("+stevilo+")", str(rezultat))
    return a

def resiModule(a):
    while("%" in a):
        stPrej = poisciSteviloPredBrezMinus(a,"%")
        stPrejF = int(stPrej)
        stPotem = poisciSteviloZa(a, "%")
        stPotemF = int(stPotem)
        rezultat = module(stPrejF, stPotemF)
        a = a.replace(stPrej+"%"+stPotem, str(rezultat))
    return a

def resiMnozenjaDeljenja(x):
    while ("*" in x or "/" in x):
        splitPlusMinus = []
        splitMinus = x.split("-")
        for delRsP in splitMinus:
            splitPlusMinus += delRsP.split("+")
        for delMnozenjeDeljenje in splitPlusMinus:
            if "/" in delMnozenjeDeljenje:
                st1 = poisciSteviloPredBrezMinus(delMnozenjeDeljenje, "/")
                st2 = poisciSteviloZa(delMnozenjeDeljenje, "/")
                rezultat = deljenje(float(st1), float(st2))
                x = x.replace(st1+"/"+st2, str(rezultat))
            if "*" in delMnozenjeDeljenje:
                st1 = poisciSteviloPredBrezMinus(delMnozenjeDeljenje, "*")
                st2 = poisciSteviloZa(delMnozenjeDeljenje, "*")
                rezultat = mnozenje(float(st1), float(st2))
                x = x.replace(st1+"*"+st2, str(rezultat))
    return x

def resiOdstevanja(x):
    while ("-" in x) and (x.count("-")>1 or x[0] != "-"):
        if "+-" in x:
            x = x.replace("+-", "-")
        splitMinus = x.split("+")
        for deliSestevanja in splitMinus:
            if "-" in deliSestevanja:
                st1 = poisciSteviloPredBrezMinus(deliSestevanja, "-")
                st2 = poisciSteviloZa(deliSestevanja, "-")
                rezultat = odstej(float(st1), float(st2))
                x = x.replace(st1+"-"+st2, str(rezultat))
    return x

def resiSestevanja(x):
    while ("+" in x):
        st1 = poisciSteviloPredZminus(x, "+")
        st2 = poisciSteviloZa(x, "+")
        rezultat = sestej(float(st1), float(st2))
        rezultat = round(rezultat, 5)
        x = x.replace(st1+"+"+st2, str(rezultat))
    return x


def resi(x):
    if("root(" in x):
        x = resiKorene(x)
    if("**" in x):
        x = resiPotence(x)
    if("%" in x):
        x = resiModule(x)
    while "(" in x:
        x = resiOklepaje(x)
    x = x.replace(")", "")
    x = resiMnozenjaDeljenja(x)
    x = resiOdstevanja(x)
    x = resiSestevanja(x)
    return x