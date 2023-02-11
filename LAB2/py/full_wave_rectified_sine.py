# full wave rectified sine
import matplotlib.pyplot as plt
import math
import numpy as np

PI=math.pi

STARTI=-10
ENDI=10
DT=0.01
H=100
T=2
A = 10

coefprint=True

def f(t, h=H):
    a0= 2*PI
    somme = a0
    global coefprint
    for n in range(1,h+1):
        if (n % 2) == 0:
            an= ((-40)/PI)*(1/((n**2)-1))
        else: 
            an = 0
        bn=0

        if coefprint:
            print(f"> a0: {round(a0,3)}    --    a{n} : {round(an,3)}    --    b{n} : {round(bn,3)}")
        somme = somme + an*math.cos(n*PI*t)

    if coefprint:
        coefprint = False
    return somme

print('> == FullWaveRectifiedSine == ')
print(f'> a0        --        an        --        bn')

t=np.arange(STARTI, ENDI, DT)
ft=[f(i) for i in t]
fig=plt.figure()
fig.set_figwidth(10)
fig.suptitle('FullWaveRectifiedSine')
plt.plot(t, ft)
plt.axhline(0, color='r')
plt.axvline(0, color='r')
plt.legend()
plt.ylabel('f(t)')
plt.xlabel('t')
plt.grid(visible=True, which='major', color='#848484', linestyle='-')
plt.minorticks_on()
plt.grid(visible=True, which='minor', color='#999999', linestyle='--', alpha=0.34)
plt.show()