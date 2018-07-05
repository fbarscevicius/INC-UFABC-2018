# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt

#Metodo de Euler

tmax = 100
dt = 0.01

#a-> rate of recovery of u
#b-> sensitivity
#c-> afterspike reset of v
#d-> afterspike reset of u

a = 0.1
b = 0.2
c = -65
d = 8
pico = 30

tempo = np.arange(0,tmax,dt)
v = np.zeros((len(tempo)))
u = np.zeros((len(tempo)))

vrest = -70
v[0]=vrest
u[0]=b*v[0]

I = np.zeros((len(tempo))) + 15
#I[10*f:60*f] = 15


for p in range(len(tempo)-1):
    
    if(v[p] >= pico):
        v[p] = c
        u[p] = u[p] + d
    
    dvdt = 0.04 * v[p]**2 + 5 * v[p] + 140 - u[p] + I[p]
    v[p+1] = v[p] + dvdt * dt
    
    dudt = a * (b * v[p] - u[p])
    u[p+1] = u[p] + dudt * dt

    
plt.plot(tempo,v)
plt.plot(tempo,u)
plt.show()

