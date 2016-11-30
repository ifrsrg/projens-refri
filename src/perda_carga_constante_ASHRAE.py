import math
from tkinter import *


def submit_data():
    mu = float(muet.get())
    L_1 = 1.0
    theta = float(thetaet.get())
    epsilon = float(epsilonet.get())
    rho = float(rhoet.get())
    Q_1 = float(Q_1et.get())
    Q_2 = float(Q_2et.get())
    Tipo = int(Tipoet.get())

    if Tipo == 1:
        Q_1L = Q_1 * 1000.0  # [l/s]
        D_1 = 32.0 * (math.pow(Q_1L, 0.38)) / 1000
        A_1 = (math.pi * D_1 ** 2.0) / 4.0
        u_1 = Q_1 / A_1

        Q_2L = Q_2 * 1000.0  # [l/s]
        D_2 = 32.0 * (math.pow(Q_2L, 0.38)) / 1000
        A_2 = (math.pi * D_1 ** 2.0) / 4.0
        u_2 = Q_2 / A_2

    else:
        Q_1L = Q_1 * 1000.0  # [l/s]
        D_1 = 25.0 * (math.pow(Q_1L, 0.38)) / 1000
        A_1 = (math.pi * D_1 ** 2.0) / 4.0
        u_1 = Q_1 / A_1

        Q_2L = Q_2 * 1000.0  # [l/s]
        D_2 = 25.0 * (math.pow(Q_2L, 0.38)) / 1000
        A_2 = (math.pi * D_1 ** 2.0) / 4.0
        u_2 = Q_2 / A_2

    Re = rho * u_1 * D_1 / mu
    f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re), -2.0)
    f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
    dP_m = (f * L_1 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho

    D_1ans["text"] = str(D_1)
    u_1ans["text"] = str(u_1)
    A_1ans["text"] = str(A_1)
    D_2ans["text"] = str(D_2)
    u_2ans["text"] = str(u_2)
    A_2ans["text"] = str(A_2)
    dP_mans["text"] = str(dP_m)

window = Tk()

#========================================DADOS LIGADOS À VISCOSIDADE====================================================
mulb = Label(window, text="Viscosidade (Pa*s)")
mulb.place(x=30, y=60)
mulb["bg"] = "lightblue"

muet = Entry(window)
muet.place(x=40, y=78)
#-----------------------------------------------------------------------------------------------------------------------

#=======================================DADOS LIGADOS AO COMPRIMENTO DO TRECHO==========================================
Q_1lb = Label(window, text="Vazão no Trecho 1 (m³/s)")
Q_1lb.place(x=30, y=110)
Q_1lb["bg"] = "lightblue"

Q_1et = Entry(window)
Q_1et.place(x=40, y=128)
#=======================================================================================================================

#=======================================DADOS LIGADOS AO TOTAL DE ANGULOS DE CURVAS=====================================
thetalb = Label(window, text="Ângulo Total de Curvas (deg)")
thetalb.place(x=30, y=310)
thetalb["bg"] = "lightblue"

thetaet = Entry(window)
thetaet.place(x=40, y=328)
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
Q_2lb = Label(window, text="Vazão no Trecho 2 (m³/s)")
Q_2lb.place(x=30, y=160)
Q_2lb["bg"] = "lightblue"

Q_2et = Entry(window)
Q_2et.place(x=40, y=178)
#=======================================================================================================================

#=======================================DADOS LIGADOS À VELOCIDADE DESEJADA=============================================
Tipolb = Label(window, text="Tipo de Sistema (1. Conforto | 2. Industrial)")
Tipolb.place(x=30, y=360)
Tipolb["bg"] = "lightblue"

Tipoet = Entry(window)
Tipoet.place(x=40, y=378)
#=======================================================================================================================

#=============================================SAIDAS DE DADOS===========================================================
D_1lb = Label(window, text="Diâmetro no Trecho 1 (m)")
D_1lb.place(x=380, y=60)
D_1lb["bg"] = "lightblue"

D_1ans = Label(window, text="Aguardando execução...")
D_1ans.place(x=390, y=78)
D_1ans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
u_1lb = Label(window, text="Velocidade no Trecho 1 (m/s)")
u_1lb.place(x=380, y=110)
u_1lb["bg"] = "lightblue"

u_1ans = Label(window, text="Aguardando execução...")
u_1ans.place(x=390, y=128)
u_1ans["bg"] = "lightblue"
#=======================================================================================================================
A_1lb = Label(window, text="Área do Trecho 1 (m²)")
A_1lb.place(x=380, y=160)
A_1lb["bg"] = "lightblue"

A_1ans = Label(window, text="Aguardando execução...")
A_1ans.place(x=390, y=178)
A_1ans["bg"] = "lightblue"
#=======================================================================================================================
D_2lb = Label(window, text="Diâmetro no Trecho 2 (m)")
D_2lb.place(x=380, y=210)
D_2lb["bg"] = "lightblue"

D_2ans = Label(window, text="Aguardando execução...")
D_2ans.place(x=390, y=228)
D_2ans["bg"] = "lightblue"
#=======================================================================================================================

#=======================================================================================================================
u_2lb = Label(window, text="Velocidade no Trecho 2 (m/s)")
u_2lb.place(x=380, y=260)
u_2lb["bg"] = "lightblue"

u_2ans = Label(window, text="Aguardando execução...")
u_2ans.place(x=390, y=278)
u_2ans["bg"] = "lightblue"
#=======================================================================================================================
A_2lb = Label(window, text="Área do Trecho 2 (m²)")
A_2lb.place(x=380, y=310)
A_2lb["bg"] = "lightblue"

A_2ans = Label(window, text="Aguardando execução...")
A_2ans.place(x=390, y=328)
A_2ans["bg"] = "lightblue"
#=======================================================================================================================
dP_mlb = Label(window, text="Perda de Carga por metro (Pa/m)")
dP_mlb.place(x=380, y=360)
dP_mlb["bg"] = "lightblue"

dP_mans = Label(window, text="Aguardando execução...")
dP_mans.place(x=390, y=378)
dP_mans["bg"] = "lightblue"
#=======================================================================================================================

bt = Button(window, width=10, text="Submit", command=submit_data)
bt.place(x=345, y=428)

window.title("Método da Perda de Carga Constante ASHRAE")
window["bg"] = "lightblue"
window.geometry("700x478+100+100")
window.mainloop()