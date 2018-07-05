import scipy as sp
import pylab as plt
from scipy.integrate import odeint
from scipy import stats
import scipy.linalg as lin

C_m = 1.0 # membrane capacitance, 1uF.cm^2
g_Na = 120.0 # maximum sodium conductance
g_K = 36.0 # potassium
g_L = 0.3
E_Na = 50.0
E_K = -77.0
E_L = -54.387

#############################################################################


# Channel gating
def alpha_m(Vm):
    return 0.1 * (Vm + 40.0) / (1.0 - sp.exp(-(Vm + 40.0) / 10.0))


# Channel gating
def beta_m(Vm):
    return 4.0 * sp.exp(-(Vm + 65.0) / 18.0)


def alpha_h(Vm):
    return 0.07 * sp.exp(-(Vm + 65.0) / 20.0)


def beta_h(Vm):
    return 1.0 / (1.0 + sp.exp(-(Vm + 35.0) / 10.0))


def alpha_n(Vm):
    return 0.01 * (Vm + 55.0) / (1.0 - sp.exp(-(Vm + 55.0) / 10.0))


def beta_n(Vm):
    return 0.125 * sp.exp(-(Vm + 65.0) / 80.0)


def I_inj(t):
    return 10 * (t > 100) - 10 * (t > 200) + 20 * (t > 300) - 20 * (t > 400)




t = sp.arange(0.0, 500.0, 0.01)


def HH(HHall, t):
    Vm, m, h, n = HHall

    dVmdt = (I_inj(t) - (g_Na * m**3 * h * (Vm - E_Na)) - (g_K * n**4 * (Vm - E_K)) - (g_L * (Vm - E_L))) / C_m

    dmdt = alpha_m(Vm) * (1.0 - m) - beta_m(Vm) * m
    dhdt = alpha_h(Vm) * (1.0 - h) - beta_h(Vm) * h
    dndt = alpha_n(Vm) * (1.0 - n) - beta_n(Vm) * n

    return dVmdt, dmdt, dhdt, dndt



X = odeint(HH, [-65, 0.05, 0.6, 0.32], t)
Vm = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]


i_na = (g_Na * m**3 * h * (Vm - E_Na))
i_k = (g_K * n**4 * (Vm - E_K))
ileak = (g_L * (Vm - E_L))



plt.figure()
plt.subplot(411)
plt.title('Hodkin-Huxley model')
plt.plot(t, Vm, 'k')
plt.ylabel('Vm (mV)')

plt.subplot(412)
plt.plot(t, i_na, 'c', label='$I_{Na}$')
plt.plot(t, i_k, 'y', label='$I_{K}$')
plt.plot(t, ileak, 'm', label='$I_{L}$')
plt.legend()

plt.subplot(413)
plt.plot(t, m, 'r', label='m')
plt.plot(t, h, 'b', label='h')
plt.plot(t, n, 'g', label='n')
plt.legend()

plt.subplot(414)
plt.plot(t, I_inj(t), 'k')
plt.xlabel('t (ms)')
plt.ylabel('$I_{inj}$ ($\\mu{A}/cm^2$)')
#plt.ylim(-1, 31)

plt.show()