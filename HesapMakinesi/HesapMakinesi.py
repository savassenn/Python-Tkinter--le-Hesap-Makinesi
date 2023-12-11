import tkinter
from tkinter import*
import math

sayi, sayi1, sayi2, k = 0, 0, 0, 0
islem = ""
artimieksimi = 0
pencere = Tk()
pencere.geometry("330x510")
fnt = "Helvetica 13"

def dokuz_():
    global sayi, k
    sayi = 9
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text"))+str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def sekiz_():
    global sayi, k
    sayi = 8
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def yedi_():
    global sayi, k
    sayi = 7
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def alti_():
    global sayi, k
    sayi = 6
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def bes_():
    global sayi, k
    sayi = 5
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def dort_():
    global sayi, k
    sayi = 4
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def uc_():
    global sayi, k
    sayi = 3
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def iki_():
    global sayi, k
    sayi = 2
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def bir_():
    global sayi, k
    sayi = 1
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
            k = 0
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def sifir_():
    global sayi
    sayi = 0
    aktifet()
    if str(ekran.cget("text")).isalpha() == 0:
        if ekran.cget("text") != 0 and k == 0:
            ekran.config(text=str(ekran.cget("text"))+str(sayi))
            sayi = ekran.cget("text")

        elif ekran.cget("text") == 0 and k == 0:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))

        elif ekran.cget("text") != 0 and k == 1:
            ekran.config(text="")
            ekran.config(text=str(ekran.cget("text")) + str(sayi))
    else:
        ekran.config(text=sayi)
        kekran.config(text="")

def c_():
    kekran.config(text="")
    ekran.config(text=0)
    aktifet()

def ce_():
    kekran.config(text="")
    ekran.config(text=0)
    aktifet()

def yuzde_():
    global islem, k, sayi1
    islem = "%"
    k += 1
    kekran.config(text=str(ekran.cget("text")) + islem)
    sayi1 = int(ekran.cget("text"))

def pasifeal():
    kareal.config(state=tkinter.DISABLED)  # Butonları pasife çeker
    karekok.config(state=tkinter.DISABLED)
    bolme.config(state=tkinter.DISABLED)
    carpma.config(state=tkinter.DISABLED)
    toplama.config(state=tkinter.DISABLED)
    cikarma.config(state=tkinter.DISABLED)
    artieksi.config(state=tkinter.DISABLED)
    virgul.config(state=tkinter.DISABLED)
    yuzde.config(state=tkinter.DISABLED)

def aktifet():
    kareal.config(state=tkinter.NORMAL)  # Butonları normal konumuna alır
    karekok.config(state=tkinter.NORMAL)
    bolme.config(state=tkinter.NORMAL)
    carpma.config(state=tkinter.NORMAL)
    toplama.config(state=tkinter.NORMAL)
    cikarma.config(state=tkinter.NORMAL)
    artieksi.config(state=tkinter.NORMAL)
    virgul.config(state=tkinter.NORMAL)
    yuzde.config(state=tkinter.NORMAL)

def azalt_():
    global sayi
    aktifet()
    if ekran.cget("text") != 0:
        text = len(str(ekran.cget("text")))
        ekran.config(text=str(ekran.cget("text"))[:int(text) - 1])
        sayi = ekran.cget("text")
        text = len(ekran.cget("text"))
        if text < 1:
            ekran.config(text=0)
            kekran.config(text="")
            sayi = ekran.cget("text")
    else:
        ekran.config(text=0)
        sayi = ekran.cget("text")

def artieksi_():
    global artimieksimi, sayi1, sayi
    if ekran.cget("text") == 0:
        pass
    else:
        ekran.config(text=-1 * int(ekran.cget("text")))
        sayi = int(ekran.cget("text"))

def virgul_():
    if "," in ekran.cget("text"):
        pass
    else:
        ekran.config(text=ekran.cget("text")+",")

def birbolux_():
    # islem = "1/x"
    kekran.config(text="1/{}".format(ekran.cget("text")))
    if int(ekran.cget("text") == 0):
        ekran.config(text="Sıfıra Bölünemez")
        pasifeal()
    else:
        ekran.config(text=1 / int(ekran.cget("text")))

def kareal_():
    global islem
    islem = "sqr"
    kekran.config(text=islem + "({})".format(str(ekran.cget("text"))))
    ekran.config(text=pow(int(ekran.cget("text")), 2))

def karekok_():
    global islem
    islem = "√x"
    kekran.config(text="√{}".format(str(ekran.cget("text"))))
    ekran.config(text=math.sqrt(int(ekran.cget("text"))))

def toplama_():
    global islem, k, sayi1
    islem = "+"
    k += 1
    kekran.config(text=str(ekran.cget("text")) + islem)
    sayi1 = int(ekran.cget("text"))

def cikarma_():
    global islem, k, sayi1
    islem = "-"
    k += 1
    kekran.config(text=str(ekran.cget("text")) + islem)
    sayi1 = int(ekran.cget("text"))

def carpma_():
    global islem, k, sayi1
    islem = "x"
    k += 1
    kekran.config(text=str(ekran.cget("text")) + islem)
    sayi1 = int(ekran.cget("text"))

def bolme_():
    global islem, k, sayi1
    islem = "/"
    k += 1
    kekran.config(text=str(ekran.cget("text")) + islem)
    sayi1 = int(ekran.cget("text"))

def esittir_():
    global islem, sayi1, sayi2, k, sayi
    k = 0
    aktifet()
    if islem == "x":
        print(sayi)
        ekran.config(text=int(sayi1) * int(sayi))
        kekran.config(text=str(sayi1) + islem + str(sayi) + "=")
        sayi1 = int(ekran.cget("text"))
    if islem == "/":
        if sayi == 0:
            ekran.config(text="Sonuc Tanımsız")
        else:
            ekran.config(text=int(sayi1) / int(sayi))
            kekran.config(text=str(sayi1) + islem + str(sayi) + "=")
            sayi1 = int(ekran.cget("text"))
    if islem == "+":
        ekran.config(text=int(sayi1) + int(sayi))
        kekran.config(text=str(sayi1) + islem + str(sayi) + "=")
        sayi1 = int(ekran.cget("text"))
    if islem == "-":
        ekran.config(text=int(sayi1) - int(sayi))
        kekran.config(text=str(sayi1) + islem + str(sayi) + "=")
        sayi1 = int(ekran.cget("text"))
    if islem == "%":
        ekran.config(text=(int(sayi1) * int(sayi)) / 100)
        kekran.config(text=str(sayi1) + islem + str(sayi) + "=")
        sayi1 = int(ekran.cget("text"))


yuzde = Button(pencere)
yuzde.config(text="  %  ", font=fnt, bg="#d3d3d3", fg="black", command=yuzde_)
yuzde.place(x=10, y=175, width=70, height=50)

ce = Button(pencere)
ce.config(text=" CE ", font=fnt, bg="#d3d3d3", fg="black", command=ce_)
ce.place(x=90, y=175, width=70, height=50)

c = Button(pencere)
c.config(text="  C  ", font=fnt, bg="#d3d3d3", fg="black", command=c_)
c.place(x=170, y=175, width=70, height=50)

azalt = Button(pencere)
azalt.config(text=" <x ", font=fnt, bg="#d3d3d3", fg="black", command=azalt_)
azalt.place(x=250, y=175, width=70, height=50)

birbolux = Button(pencere)
birbolux.config(text=" 1/x ", font=fnt, bg="#d3d3d3", fg="black", command=birbolux_)
birbolux.place(x=10, y=230, width=70, height=50)

kareal = Button(pencere)
kareal.config(text="   x²  ", font=fnt, bg="#d3d3d3", fg="black", command=kareal_)
kareal.place(x=90, y=230, width=70, height=50)

karekok = Button(pencere)
karekok.config(text="  √x ", font=fnt, bg="#d3d3d3", fg="black", command=karekok_)
karekok.place(x=170, y=230, width=70, height=50)

bolme = Button(pencere)
bolme.config(text="   /  ", font=fnt, bg="#d3d3d3", fg="black", command=bolme_)
bolme.place(x=250, y=230, width=70, height=50)

yedi = Button(pencere)
yedi.config(text="   7  ", font=fnt, bg="#f5f5dc", fg="black", command=yedi_)
yedi.place(x=10, y=285, width=70, height=50)

sekiz = Button(pencere)
sekiz.config(text="   8  ", font=fnt, bg="#f5f5dc", fg="black", command=sekiz_)
sekiz.place(x=90, y=285, width=70, height=50)

dokuz = Button(pencere)
dokuz.config(text="   9  ", font=fnt, bg="#f5f5dc", fg="black", command=dokuz_)
dokuz.place(x=170, y=285, width=70, height=50)

carpma = Button(pencere)
carpma.config(text="   x  ", font=fnt, bg="#d3d3d3", fg="black", command=carpma_)
carpma.place(x=250, y=285, width=70, height=50)

dort = Button(pencere)
dort.config(text="   4  ", font=fnt, bg="#f5f5dc", fg="black", command=dort_)
dort.place(x=10, y=340, width=70, height=50)

bes = Button(pencere)
bes.config(text="   5  ", font=fnt, bg="#f5f5dc", fg="black", command=bes_)
bes.place(x=90, y=340, width=70, height=50)

alti = Button(pencere)
alti.config(text="   6  ", font=fnt, bg="#f5f5dc", fg="black", command=alti_)
alti.place(x=170, y=340, width=70, height=50)

cikarma = Button(pencere)
cikarma.config(text="   _  ", font=fnt, bg="#d3d3d3", fg="black", command=cikarma_)
cikarma.place(x=250, y=340, width=70, height=50)

uc = Button(pencere)
uc.config(text="   3  ", font=fnt, bg="#f5f5dc", fg="black", command=uc_)
uc.place(x=10, y=395, width=70, height=50)

iki = Button(pencere)
iki.config(text="   2  ", font=fnt, bg="#f5f5dc", fg="black", command=iki_)
iki.place(x=90, y=395, width=70, height=50)

bir = Button(pencere)
bir.config(text="   1  ", font=fnt, bg="#f5f5dc", fg="black", command=bir_)
bir.place(x=170, y=395, width=70, height=50)

toplama = Button(pencere)
toplama.config(text="   +  ", font=fnt, bg="#d3d3d3", fg="black", command=toplama_)
toplama.place(x=250, y=395, width=70, height=50)

artieksi = Button(pencere)
artieksi.config(text="   +/-  ", font=fnt, bg="#d3d3d3", fg="black", command=artieksi_)
artieksi.place(x=10, y=450, width=70, height=50)

sifir = Button(pencere)
sifir.config(text="   0  ", font=fnt, bg="#f5f5dc", fg="black", command=sifir_)
sifir.place(x=90, y=450, width=70, height=50)

virgul = Button(pencere)
virgul.config(text="   ,  ", font=fnt, bg="#f5f5dc", fg="black", command=virgul_)
virgul.place(x=170, y=450, width=70, height=50)

esittir = Button(pencere)
esittir.config(text="   =  ", font=fnt, bg="#778899", fg="black", command=esittir_)
esittir.place(x=250, y=450, width=70, height=50)

ekran = Label(pencere, text=0, font="Helvetiva 15", fg="black", anchor=E)
ekran.place(x=5, y=55, width=320, height=100)

kekran = Label(pencere, font="Helvetiva 15", fg="black", anchor=E)  # "anchor E" yazılan veriyi sağa hizalar
kekran.place(x=5, y=5, width=320, height=50)


mainloop()
