# %% [markdown]
# # Esempio di notebook

# %% [markdown]
# Importazione delle librerie necessarie 

# %%
import math
from math import cos
from math import acos as arccos
from math import log as ln

import numpy as np

import matplotlib.pyplot as plt

# %% [markdown]
# ## Esempi con math

# %%
m=5.3 # massa di 5.3 kg
print('massa =', m, 'kg')
math.sin(1)
cos(1)
arccos(0.5)

print('pi greco =', math.pi)

print('log(10) = ', ln(10))

# %% [markdown]
# ## Esempi con numpy
# 

# %%
a=np.array([1,2,3])
print(a)
print(np.sin(a))
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(np.sin(b))
z=np.zeros(11)
print(z)
z[3]=5
print(z)
bz=np.zeros_like(b)
print(bz)

# %%
x=np.linspace(0,10,11)
print('x =',x)
y = 3*x+2
print('y =', y)

# %% [markdown]
# ## Esempio con matplotlib
# 

# %%
x=np.linspace(0, 2*np.pi, 100) # [0;2pi]
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,x,z)
plt.plot(x,y*np.exp(-0.2*x))
plt.grid()
plt.show() # in jupyter notebook non è necessario, ma in altri potrebbe



