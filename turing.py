# -*- coding: utf-8 -*-
import numpy as np
from scipy.ndimage import laplace
from PIL import Image
from tqdm import tqdm


# difusion coeficients
DA = 1.
DB = 0.5


def constrain(A,B,constraint):
    B = np.maximum(B,constraint)
    return A,B


def step(A,B,f,k,d,dt):
    Ap = A+(DA*d*d*laplace(A)-A*B*B+f*(1-A))*dt
    Bp = B+(DB*d*d*laplace(B)+A*B*B-(k+f)*B)*dt
    return Ap, Bp

def run(constraint,f=0.035,k=0.06,d=0.4,tmax=10000, dt=1., interval=None):
    states = []
    A = np.ones(constraint.shape)
    B = np.zeros(constraint.shape)
    for i in tqdm(range(int(tmax/dt))):
        A,B = step(A,B,f,k,d,dt)
        A,B = constrain(A,B,constraint)
        if interval != None and i%interval == 0:
            states.append((A,B))
    if interval == None:
        return A,B
    return states
