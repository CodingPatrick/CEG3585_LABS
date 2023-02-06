import matplotlib.pyplot as plt
import math
import numpy as np

PI=math.pi

STARTI=-10
ENDI=10
DT=0.01
H=100

coefprint=True

def f(t, h=H):
    a0=0
    somme = a0
    global ceofprint
    for n in range(1,h+1):
        an=0
        bn=(20/(n*PI))*(1-math.pow(-1,n))

        if coefprint:
            print(f"> a0: {a0}    --    a{n} : {round(an,3)}    --    b{n} : {round(bn,3)}")
        somme = somme + bn