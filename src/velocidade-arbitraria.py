import math
from tkinter import *


def submit_data():
    mu = float(muet.get())
    L = float(Let.get())
    theta = float(thetaet.get())
    epsilon = float(epsilonet.get())
    rho = float(rhoet.get())
    Q = float(Qet.get())
    u = float(uoet.get())

    D = math.sqrt((4.0 * Q) / (math.pi * u))
    Re = rho * u * D / mu
    f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D), 1.11) + 6.9 / Re), -2.0)
    f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
    dP = (rho * f * L * u ** 2.0 / D)
    A = (math.pi * D ** 2) / 4.0

    Dans["text"] = str(D)
    uans["text"] = str(u)
    dPans["text"] = str(dP)
    fans["text"] = str(f)
    Aans["text"] = str(A)


window = Tk()

#========================================DADOS LIGADOS À VISCOSIDADE====================================================
mulb = Label(window, text="Viscosidade (Pa*s)")
mulb.place(x=30, y=60)
mulb["bg"] = "lightblue"

muet = Entry(window)
muet.place(x=40, y=78)
#-----------------------------------------------------------------------------------------------------------------------

#=======================================DADOS LIGADOS AO COMPRIMENTO DO TRECHO==========================================
Llb = Label(window, text="Comprimento do Trecho (m)")
Llb.place(x=30, y=110)
Llb["bg"] = "lightblue"

Let = Entry(window)
Let.place(x=40, y=128)
#=======================================================================================================================

#=======================================DADOS LIGADOS AO TOTAL DE ANGULOS DE CURVAS=====================================
thetalb = Label(window, text="Ângulo Total de Curvas (deg)")
thetalb.place(x=30, y=160)
thetalb["bg"] = "lightblue"

thetaet = Entry(window)
thetaet.place(x=40, y=178)
#=======================================================================================================================

#=======================================DADOS LIGADOS À RUGOSIDADE ABOSLUTA=============================================
epsilonlb = Label(window, text="Rugosidade Absoluta (m)")
epsilonlb.place(x=30, y=210)
epsilonlb["bg"] = "lightblue"

epsilonet = Entry(window)
epsilonet.place(x=40, y=228)
#=======================================================================================================================

#=======================================DADOS LIGADOS À MASSA ESPECÍFICA================================================
rholb = Label(window, text="Massa Específica (kg/m³)")
rholb.place(x=30, y=260)
rholb["bg"] = "lightblue"

rhoet = Entry(window)
rhoet.place(x=40, y=278)
#=======================================================================================================================

#=======================================DADOS LIGADOS À VAZÃO DO TRECHO=================================================
Qlb = Label(window, text="Vazão no Trecho (m³/s)")
Qlb.place(x=30, y=310)
Qlb["bg"] = "lightblue"

Qet = Entry(window)
Qet.place(x=40, y=328)
#=======================================================================================================================

#=======================================DADOS LIGADOS À VELOCIDADE DESEJADA=============================================
uolb = Label(window, text="Velocidade Desejada (m/s)")
uolb.place(x=30, y=360)
uolb["bg"] = "lightblue"

uoet = Entry(window)
uoet.place(x=40, y=378)
#=======================================================================================================================

#====================================DADOS LIGADOS AO DIÂMETRO==========================================================
Dlb = Label(window, text="Diâmetro (m)")
Dlb.place(x=380, y=60)
Dlb["bg"] = "lightblue"

Dans = Label(window, text="Aguardando execução...")
Dans.place(x=390, y=78)
Dans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
dPlb = Label(window, text="Perda de Carga (Pa)")
dPlb.place(x=380, y=110)
dPlb["bg"] = "lightblue"

dPans = Label(window, text="Aguardando execução...")
dPans.place(x=390, y=128)
dPans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
Alb = Label(window, text="Área (m²)")
Alb.place(x=380, y=160)
Alb["bg"] = "lightblue"

Aans = Label(window, text="Aguardando execução...")
Aans.place(x=390, y=178)
Aans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
ulb = Label(window, text="Velocidade (m/s)")
ulb.place(x=380, y=210)
ulb["bg"] = "lightblue"

uans = Label(window, text="Aguardando execução...")
uans.place(x=390, y=228)
uans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
flb = Label(window, text="Fator de Atrito (ƒ)")
flb.place(x=380, y=260)
flb["bg"] = "lightblue"

fans = Label(window, text="Aguardando execução...")
fans.place(x=390, y=278)
fans["bg"] = "lightblue"
#=======================================================================================================================

bt = Button(window, width=10, text="Submit", command=submit_data)
bt.place(x=345, y=338)

window.title("Método da Velocidade Arbitrária")
window["bg"] = "lightblue"
window.geometry("700x428+100+100")
window.mainloop()