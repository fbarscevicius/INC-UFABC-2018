# -*- coding: utf-8 -*-
'''
Modelagem Compartimental

1) Utilize o método de Euler para simular um modelo compartimental composto
por dois circuitos equivalentes passivos conectados por resistências axiais (Ra).

Dimensões espaciais dos compartimentos:
L1 = 10 µm (comprimento)
D1 = 1 µm (diâmetro)
L2 = 10 µm (comprimento)
D2 = 2 µm (diâmetro)
A  = Área superfície do cilindro = pi.D.L
S  = Área secção transversal do cilindro = pi.(D/2)2

Conversão µm para cm: 1 µm = 10^-4cm

Parâmetros Elétricos:
RA    = 0.115 KΩ.cm
RM    = 2 KΩ.cm2
CM    = 1 µF/cm2
Vm(1) = -70 mV
Em    = -70 mV
dt    = 0.001 ms
I     = 1 nA para 10 < t <= 60 ms
I     = 0 para t <= 10 e t > 60 ms
Tmax  = 100 ms
Cm    = A * CM (Capacitância Absoluta)
Rm    = RM / A (Resistência Absoluta)
Ra    = RA * L / S (Resistência Axial Absoluta)

Injete a corrente no compartimento da esquerda e plote a voltagem dos 2 compartimentos simulados
em subplots diferentes. Utilize Ra = 0.115 KΩ.cm (resistência axial).

Aumente em 10 x o valor de Ra e plote a voltagem dos 2 compartimentos.
'''

import numpy as np
import matplotlib.pyplot as plt

tmax = 100
dt   = 0.001
f    = int(1/dt)

#Parametros Espaciais
L1 = 10*1e-4 #cm
L2 = 10*1e-4 #cm
D1 = 1*1e-4 #cm
D2 = 2*1e-4 #cm

A1 = np.pi*D1*L1
A2 = np.pi*D2*L2

S1 = np.pi*(D1/2)**2
S2 = np.pi*(D2/2)**2

#Parametros Eletricos Relativos
RA = 0.115 #Kohm.cm
RM = 2 #Kohm*cm**2
CM = 1 #uF/cm^**2

#Parametros Eletricos Absolutos
Ra1 = RA*(L1/S1) #Kohm
Ra2 = RA*(L2/S2) #Kohm
Ra  = 1*(Ra1+Ra2)

Rm1 = RM/A1 #Kohm
Rm2 = RM/A2 #Kohm

Cm1 = CM*A1 #uF
Cm2 = CM*A2 #uF

Em1 = -70 #mV
Em2 = -70 #mV

tempo = np.arange(0,tmax,dt)
vm1   = np.zeros((len(tempo)))
vm2   = np.zeros((len(tempo)))

vrest  = -70
vm1[0] = vrest
vm2[0] = vrest

amplitude = 1*1e-3  # uA
I = np.zeros(len(tempo))
I[10*f:60*f] = amplitude


for p in range(len(tempo)-1):
    Ia12 = (vm1[p] - vm2[p]) / (Ra)
    Ia21 = (vm2[p] - vm1[p]) / (Ra)
    Im1 = (vm1[p] - Em1)/ Rm1 
    Im2 = (vm2[p] - Em2)/ Rm2
    dvm1dt = 1/Cm1 * (-Im1- Ia12 + I[p]) 
    vm1[p+1] = vm1[p] + dvm1dt * dt
    dvm2dt = 1/Cm2 * (-Im2 - Ia21) 
    vm2[p+1] = vm2[p] + dvm2dt * dt
    
plt.plot(tempo,vm1)
plt.plot(tempo,vm2)
plt.show()

'''
Utilize o método de Euler para simular um modelo compartimental composto por cinco circuitos
equivalentes passivos conectados por resistências axiais (Ra). 

Considere a dimensão espacial de todos os compartimentos igual:
L = 10 µm (comprimento)
D = 1 µm (diâmetro)

Cada compartimento pode ser descrito pelos parâmetros abaixo:
dVm/dt=-(Vm-Em)/(RmCm)+I/Cm+Iaxial/Cm;
RA = 0.115 KΩ.cm
RM = 2 KΩ.cm2
CM = 1 µF/cm2
Vm(1) = -70 mV
Em=-70 mV
dt=0.001 ms
a) Injete a corrente abaixo apenas no compartimento V1 e plote a voltagem em todos os
compartimentos.
I=1 nA para 10<t<=60 ms
I=0 para t<=10 e t>60 ms
b) Injete a corrente abaixo apenas no compartimento V4 e plote a voltagem em todos os
compartimentos.
I=10 nA para 10<t<=60 ms
I=0 para t<=10 e t>60 ms
'''

tmax = 100
dt   = 0.001
f    = int(1/dt)

#Parametros Espaciais
L = 10*1e-4 #cm
D = 1*1e-4 #cm
A = np.pi*D*L
S = np.pi*(D/2)**2

#Parametros Eletricos Relativos
RA = 0.115 #Kohm.cm
RM = 2 #Kohm*cm**2
CM = 1 #uF/cm^**2

#Parametros Eletricos Absolutos
Ra1 = RA*(L/S) #Kohm
Ra = 10*(Ra1+Ra1)

Rm = RM/A #Kohm
Cm = CM*A #uF
Em = -70 #mV

tempo = np.arange(0,tmax,dt)

vm1 = np.zeros((len(tempo)))
vm2 = np.zeros((len(tempo)))
vm3 = np.zeros((len(tempo)))
vm4 = np.zeros((len(tempo)))
vm5 = np.zeros((len(tempo)))

vrest = -70

vm1[0] = vrest
vm2[0] = vrest
vm3[0] = vrest
vm4[0] = vrest
vm5[0] = vrest

amplitude = 1*1e-3  # uA
I = np.zeros(len(tempo))
I[10*f:60*f] = amplitude


for p in range(len(tempo)-1):
    Ia12 = (vm1[p] - vm2[p])/(Ra)
    Ia21 = (vm2[p] - vm1[p])/(Ra)
    Ia13 = (vm1[p] - vm3[p])/(Ra)
    Ia31 = (vm3[p] - vm1[p])/(Ra)
    Ia34 = (vm3[p] - vm4[p])/(Ra)
    Ia43 = (vm4[p] - vm3[p])/(Ra)
    Ia35 = (vm3[p] - vm5[p])/(Ra)
    Ia53 = (vm5[p] - vm3[p])/(Ra)
    Ia45 = (vm4[p] - vm5[p])/(Ra)
    Ia54 = (vm5[p] - vm4[p])/(Ra)
    Ia23 = (vm2[p] - vm3[p])/(Ra)
    Ia32 = (vm3[p] - vm2[p])/(Ra)
    
    Im1 = (vm1[p] - Em)/Rm 
    Im2 = (vm2[p] - Em)/Rm
    Im3 = (vm3[p] - Em)/Rm 
    Im4 = (vm4[p] - Em)/Rm
    Im5 = (vm5[p] - Em)/Rm

    dvm1dt = 1/Cm*(-Im1 - Ia12 - Ia13 + I[p]) 
    vm1[p+1] = vm1[p] + dvm1dt * dt

    dvm2dt = 1/Cm*(-Im2 - Ia21 -Ia23) 
    vm2[p+1] = vm2[p] + dvm2dt * dt

    dvm3dt = 1/Cm*(-Im3 - Ia32 - Ia31 - Ia34 - Ia35) 
    vm3[p+1] = vm3[p] + dvm3dt * dt

    dvm4dt = 1/Cm*(-Im4 - Ia43 -Ia45 ) 
    vm4[p+1] = vm4[p] + dvm4dt * dt

    dvm5dt = 1/Cm*(-Im5 - Ia53 - Ia54) 
    vm5[p+1] = vm5[p] + dvm5dt * dt
    
plt.plot(tempo,vm1)
plt.plot(tempo,vm2)
plt.plot(tempo,vm3)
plt.plot(tempo,vm4)
plt.plot(tempo,vm5)
plt.show()