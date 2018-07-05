# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt

#Metodo de Euler
# dvdt = -v / (r*c) + I /c
# v(0) = 0
#r = 2
#c = 1
#dt = 1
#I = 1 para 10<t<60

tmax = 100
dt = 0.01
f=int(1/dt)

r = 2
c = 1
tempo = np.arange(0,tmax,dt)
v = np.zeros((len(tempo)))

vrest = -60
v[0]=vrest

I = np.zeros((len(tempo)))
I[10*f:60*f] = 16

v_pico = 10
v_limiar = -30

contador = 0

for p in range(len(tempo)-1):
    dvdt = - (v[p] - vrest)/ (r*c) + I[p] / c
    v[p+1] = v[p] + dvdt * dt
    
    if (v[p] > v_limiar)  :
        v[p] = v_pico
        v[p+1] = vrest
        contador = contador + 1

print('disparos=',contador)

plt.plot(tempo,v)
plt.show()

