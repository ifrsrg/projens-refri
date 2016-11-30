import math
from tkinter import *
from scipy.optimize import fsolve

rho = 0.0
mu = 0.0
L_23 = 0.0
Q_23 = 0.0
Q_1 = 0.0
D_23_i = 0.0
u_23_i = 0.0
dP_m1 = 0.0
u_1 = 0.0
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

def submit_data1():
    global rho
    global mu
    global L_23
    global Q_23
    global Q_1
    global theta
    global epsilon
    global D_23_i    
    global u_23_i
    global dP_m1
    global u_1
    
    rho = float(rhoet.get())
    mu = float(muet.get())
    L_23 = float(L_23et.get())
    Q_23 = float(Q_23et.get())
    theta = float(thetaet.get())
    epsilon = float(epsilonet.get())    
    u_1 = float(u_1et.get())
    Q_1 = float(Q_1et.get())    
    
    D_1 = math.sqrt((4.0 * Q_1) / (math.pi * u_1)) 
    Re_i = rho * u_1 * D_1 / mu
    f_0_i = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re_i), -2.0)
    f_i = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re_i * math.sqrt(f_0_i))), -2.0)
    dP_m1 = (f_i * L_23 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho
    D_23_i = D_1
    u_23_i = u_1
    
    dP_m1ans["text"] = str(dP_m1)
    D_23_ians["text"] = str(D_23_i)
    u_23_ians["text"] = str(u_23_i)

def submit_data2():
    global u_23_i
    
    D_23_i = float(D_23_iet.get())   
    dP_m1 = float(dP_m12et.get())
    D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])   
    
    D_23ans["text"] = str(D_23)
    u_23ans["text"] = str(u_23)
    D_1ans["text"] = str(D_1)
    dP_m1fans["text"] = str(dP_m1)
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
#---------------------------------------------------------
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
Q_1lb = Label(window, text="Vazão no Trecho Anterior (m3/s)")
Q_1lb.place(x=30, y=260)
Q_1lb["bg"] = "lightblue"

Q_1et = Entry(window)
Q_1et.place(x=40, y=278)
#-------------------------------------------------------------
thetalb = Label(window, text="Ângulo Total de Curvas (deg)")
thetalb.place(x=30, y=310)
thetalb["bg"] = "lightblue"

thetaet = Entry(window)
thetaet.place(x=40, y=328)
#-----------------------------------------------------------
epsilonlb = Label(window, text="Rugosidade Absoluta (m)")
epsilonlb.place(x=30, y=360)
epsilonlb["bg"] = "lightblue"

epsilonet = Entry(window)
epsilonet.place(x=40, y=378)
#----------------------------------------------------------
u_1lb = Label(window, text="Velocidade Inicial no Trecho (m/s)")
u_1lb.place(x=30, y=410)
u_1lb["bg"] = "lightblue"

u_1et = Entry(window)
u_1et.place(x=40, y=428)
#----------------------------------------------------------
D_23_ilb = Label(window, text="Diametro do Trecho (m)")
D_23_ilb.place(x=380, y=60)
D_23_ilb["bg"] = "lightblue"

D_23_ians = Label(window, text="Aguardando execução...")
D_23_ians.place(x=390, y=78)
D_23_ians["bg"] = "lightblue"
#---------------------------------------------------------
u_23_ilb = Label(window, text="Velocidade no Trecho (m/s)")
u_23_ilb.place(x=380, y=110)
u_23_ilb["bg"] = "lightblue"

u_23_ians = Label(window, text="Aguardando execução...")
u_23_ians.place(x=390, y=128)
u_23_ians["bg"] = "lightblue"
#---------------------------------------------------------
dP_m1lb = Label(window, text="Perda de Carga no Trecho (Pa/m)")
dP_m1lb.place(x=380, y=160)
dP_m1lb["bg"] = "lightblue"

dP_m1ans = Label(window, text="Aguardando execução...")
dP_m1ans.place(x=390, y=178)
dP_m1ans["bg"] = "lightblue"
#---------------------------------------------------------
bt1 = Button(window, width=10, text="SUBMIT", command=submit_data1)
bt1.place(x=315, y=460)
#-----------------------------------------------------------
space = Label(window, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------")
space.place(x=30, y=510)
space["bg"] = "lightblue"
#-----------------------------------------------------------
D_23lb = Label(window, text="Diametro do Trecho (m)")
D_23lb.place(x=30, y=560)
D_23lb["bg"] = "lightblue"

D_23et = Entry(window)
D_23et.place(x=40, y=578)
#---------------------------------------------------------
u_23lb = Label(window, text="Velocidade no Trecho (m/s)")
u_23lb.place(x=30, y=610)
u_23lb["bg"] = "lightblue"

u_23et = Entry(window)
u_23et.place(x=40, y=628)
#---------------------------------------------------------
dP_m12lb = Label(window, text="Perda de Carga no Trecho (Pa/m)")
dP_m12lb.place(x=30, y=660)
dP_m12lb["bg"] = "lightblue"

dP_m1et = Entry(window)
dP_m1et.place(x=40, y=678)
#----------------------------------------------------------
D_23flb = Label(window, text="Diametro do Trecho - Valor Final - (m)")
D_23flb.place(x=380, y=560)
D_23flb["bg"] = "lightblue"

D_23ans = Label(window, text="Aguardando execução...")
D_23ans.place(x=390, y=578)
#-------------------------------------------------------
u_23flb = Label(window, text="Velocidade do Trecho - Valor Final - (m/s)")
u_23flb.place(x=380, y=610)
u_23flb["bg"] = "lightblue"

u_23ans = Label(window, text="Aguardando execução...")
u_23ans.place(x=390, y=628)
u_23ans["bg"] = "lightblue"
#-------------------------------------------------------
D_1lb = Label(window, text="Diametro do Primeiro Trecho (m)")
D_1lb.place(x=380, y=660)
D_1lb["bg"] = "lightblue"

D_1ans = Label(window, text="Aguardando execução...")
D_1ans.place(x=390, y=678)
D_1ans["bg"] = "lightblue"
#--------------------------------------------------------
dP_m1flb = Label(window, text="Perda de Carga no Trecho - Valor Final - (Pa/m)")
dP_m1flb.place(x=380, y=710)
dP_m1flb["bg"] = "lightblue"

dP_m1fans = Label(window, text="Aguardando execução...")
dP_m1fans.place(x=390, y=728)
dP_m1fans["bg"] = "lightblue"
#-------------------------------------------------------
residualslb = Label(window, text="")
residualslb.place(x=380, y=790)
residualslb["bg"] = "lightblue"
#--------------------------------------------------------
bt2 = Button(window, width=10, text="SUBMIT", command=submit_data2)
bt2.place(x=315, y=822)

D_23ans["bg"] = "lightblue"
window.title("Método da Perda de Carga Constante Clássico")
window.geometry("700x870+200+200")
window["bg"] = "lightblue"
window.mainloop()

