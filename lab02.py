# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""


# Método de Euler
# dydt = y
# y(0) = 1
# dt = 0.01
# tmax = 4
# y(t) = ?

import numpy as np
import matplotlib.pyplot as plt

tmax = 4
dt = 0.01

tempo = np.arange(0, tmax, dt)
y = np.zeros(len(tempo))
y[0] = 1

for p in range(len(tempo)-1):
    dydt = y[p]
    y[p+1] = y[p] + dydt * dt
    
plt.plot(tempo, y)
plt.show()


# Simule o comportamento desse circuito com o método de Euler

# dV/dt = -V/(RC) + I/C

# Plote a voltagem em função do tempo (0 < t <= 100)
# Use os seguintes parâmetros:
# R = {2, 5, 10, 20, 50}
# C = 1; V0 = 0; dt = 1;
# I = 1 para 10 < t <= 60
# I = 0 para t < = 10 e t > 60

tmax = 100
dt = 1

tempo = np.arange(0, tmax, dt)

C = 1
I = np.array([1 if x > 10 and x <= 60 else 0 for x in tempo])
V = np.zeros(len(tempo))
R = [2, 5, 10, 20, 50]

plt.figure(figsize=[8, 6])
for r in R:
    for p in range(len(tempo)-1):
        dvdt = -V[p]/r + I[p]
        V[p+1] = V[p] + dvdt
        
    plt.plot(tempo, V, label=f"R = {r}")
    plt.title(f"Voltagem em função do tempo")
    plt.legend()