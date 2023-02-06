# half wave rectified sine
import matplotlib.pyplot as plt
import math
import numpy as np

PI=math.pi

STARTI=-10
ENDI=10
DT=0.01
H=100
T=2

coefprint=True

def f(t=T, h=H):
    a0=0
    somme = a0
    global coefprint