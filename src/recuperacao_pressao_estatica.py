import math
from tkinter import *
from scipy.optimize import fsolve

rho = 0.0
Re = 0.0
f = 0.0
count = 0
Q_23 = 0.0
L_23 = 0.0
epsilon = 0.0
u_12 = 0.0
R = 0.0
mu = 0.0
theta = 0.0
D_23_i = 0.0
u_23_i = 0.0

def residuals(initial):
    D_23 = initial[0]
    u_23 = initial[1]
    residual = [0.0, 0.0]
    global Re
    global f
    Re = rho * u_23 * D_23 / mu
    f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_23), 1.11) + 6.9 / Re), -2.0)
    f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_23) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
    residual[0] = (f * L_23 / D_23 + 0.1 * theta / 90.0 + R) * u_23 ** 2.0 - R * u_12 ** 2.0
    residual[1] = D_23 - math.sqrt((4.0 * Q_23) / (math.pi * u_23))

    return residual

def submit_data():
    global rho
    global mu
    global L_23
    global Q_23
    global epsilon
    global u_12
    global R
    global theta
    global D_23_i
    global u_23_i
    global count

    rho = float(rhoet.get())
    mu = float(muet.get())
    L_23 = float(L_23et.get())
    Q_23 = float(Q_23et.get())
    epsilon = float(epsilonet.get())
    u_12 = float(u_12et.get())
    R = float(Ret.get())
    theta = float(thetaet.get())
    D_23_i = float(D_23_iet.get())
    u_23_i = float(u_23_iet.get())

    if count == 0:
        D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])
        A = (math.pi * D_23 ** 2.0) / 4.0
        dP = (rho * f * L_23 * u_23 ** 2.0 / D_23)
        count += 1

    else:
        D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])
        A = (math.pi * D_23 ** 2.0) / 4.0

    D_23ans["text"] = str(D_23)
    Aans["text"] = str(A)
    dPans["text"] = str(dP)
    residualsans["text"] = str(residuals([D_23, u_23]))

window = Tk()

rholb = Label(window, text="Massa Específica (kg/m³)")
rholb.place(x=30, y=60)
rholb["bg"] = "lightblue"

rhoet = Entry(window)
rhoet.place(x=40, y=78)
#----------------------------------------------------------
mulb = Label(window, text="Viscosidade (Pa*s)")
mulb.place(x=30, y=110)
mulb["bg"] = "lightblue"

muet = Entry(window)
muet.place(x=40, y=128)
#----------------------------------------------------------
L_23lb = Label(window, text="Comprimento do Trecho (m)")
L_23lb.place(x=30, y=160)
L_23lb["bg"] = "lightblue"

L_23et = Entry(window)
L_23et.place(x=40, y=178)
#----------------------------------------------------------
Q_23lb = Label(window, text="Vazão no Trecho (m³/s)")
Q_23lb.place(x=30, y=210)
Q_23lb["bg"] = "lightblue"

Q_23et = Entry(window)
Q_23et.place(x=40, y=228)
#----------------------------------------------------------
u_12lb = Label(window, text="Velocidade no Trecho Anterior (m/s)")
u_12lb.place(x=30, y=260)
u_12lb["bg"] = "lightblue"

u_12et = Entry(window)
u_12et.place(x=40, y=278)
#----------------------------------------------------------
thetalb = Label(window, text="Ângulo Total de Curvas (deg)")
thetalb.place(x=30, y=310)
thetalb["bg"] = "lightblue"

thetaet = Entry(window)
thetaet.place(x=40, y=328)
#------------------------------------------------------------
Rlb = Label(window, text="Fator de Recuperação")
Rlb.place(x=30, y=360)
Rlb["bg"] = "lightblue"

Ret = Entry(window)
Ret.place(x=40, y=378)
#--------------------------------------------------------------
epsilonlb = Label(window, text="Rugosidade Absoluta (m)")
epsilonlb.place(x=30, y=410)
epsilonlb["bg"] = "lightblue"

epsilonet = Entry(window)
epsilonet.place(x=40, y=428)
#--------------------------------------------------------------
D_23_ilb = Label(window, text="'Chute Inicial' do Diametro do Trecho (m)")
D_23_ilb.place(x=30, y=460)
D_23_ilb["bg"] = "lightblue"

D_23_iet = Entry(window)
D_23_iet.place(x=40, y=478)
#-------------------------------------------------------------
u_23_ilb = Label(window, text="'Chute Inicial' da Velocidade no Trecho (m/s)")
u_23_ilb.place(x=30, y=510)
u_23_ilb["bg"] = "lightblue"

u_23_iet = Entry(window)
u_23_iet.place(x=40, y=528)
#=======================================================================================================================
D_23lb = Label(window, text="Diametro do Trecho (m)")
D_23lb.place(x=380, y=60)
D_23lb["bg"] = "lightblue"

D_23ans = Label(window, text="Aguardando execução...")
D_23ans.place(x=390, y=78)
D_23ans["bg"] = "lightblue"
#---------------------------------------------------------
u_23lb = Label(window, text="Velocidade no Trecho (m/s)")
u_23lb.place(x=380, y=110)
u_23lb["bg"] = "lightblue"

u_23ans = Label(window, text="Aguardando execução...")
u_23ans.place(x=390, y=128)
u_23ans["bg"] = "lightblue"
#---------------------------------------------------------
Alb = Label(window, text="Área do Trecho (m²)")
Alb.place(x=380, y=160)
Alb["bg"] = "lightblue"

Aans = Label(window, text="Aguardando execução...")
Aans.place(x=390, y=178)
Aans["bg"] = "lightblue"
#----------------------------------------------------------
dPlb = Label(window, text="Perda de Carga (Pa)")
dPlb.place(x=380, y=210)
dPlb["bg"] = "lightblue"

dPans = Label(window, text="Aguardando execução...")
dPans.place(x=390, y=228)
dPans["bg"] = "lightblue"
#-------------------------------------------------------------
residualsans = Label(window, text="")
residualsans.place(x=390, y=260)
residualsans["bg"] = "lightblue"

bt = Button(window, width=10, text="Submit", command=submit_data)
bt.place(x=345, y=628)

window.title("Método da Recuperação da Pressão Estática")
window.geometry("700x700+200+200")
window["bg"] = "lightblue"
window.mainloop()