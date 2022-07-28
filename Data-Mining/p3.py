import numpy as np
import sklearn as skl
import pandas as pd
from sklearn import preprocessing
file=pd.read_csv('wine.data')
file

data=file.values
print('wine',data[:,1].mean())
print('wine',data[:,1].std())
print('Alcohol',data[:,2].mean())
print('Alcohol',data[:,2].std())
print('malicacid',data[:,3].mean())
print('malicacid',data[:,3].std())
print('ash',data[:,4].mean())
print('ash',data[:,4].std())
print('acl',data[:,5].mean())
print('acl',data[:,5].std())
print('mg',data[:,6].mean())
print('mg',data[:,6].std())
print('phenol',data[:,7].mean())
print('phenol',data[:,7].std())
print('flavanoid',data[:,8].mean())
print('flavanoid',data[:,8].std())
print('nonfla.phenol',data[:,9].mean())
print('nonfla.phenol',data[:,9].std())
print('proanth',data[:,10].mean())
print('proanth',data[:,10].std())
print('color.int',data[:,11].mean())
print('color.int',data[:,11].std())
print('hue',data[:,12].mean())
print('hue',data[:,12].std())
print('OD',data[:,13].mean())
print('OD',data[:,13].std())
print('proline',data[:,-1].mean())
print('proline',data[:,-1].std())

a=data[:,1]
b=data[:,2]
c=data[:,3]
d=data[:,4]
e=data[:,5]
f=data[:,6]
g=data[:,7]
h=data[:,8]
i=data[:,9]
j=data[:,10]
k=data[:,11]
l=data[:,12]
m=data[:,13]
n=data[:,-1]

scaled_a=preprocessing.scale(a)
scaled_b=preprocessing.scale(b)
scaled_c=preprocessing.scale(c)
scaled_d=preprocessing.scale(d)
scaled_e=preprocessing.scale(e)
scaled_f=preprocessing.scale(f)
scaled_g=preprocessing.scale(g)
scaled_h=preprocessing.scale(h)
scaled_i=preprocessing.scale(i)
scaled_j=preprocessing.scale(j)
scaled_k=preprocessing.scale(k)
scaled_l=preprocessing.scale(l)
scaled_m=preprocessing.scale(m)

scaled_n=preprocessing.scale(n)

print('StandardizedwineMean',int(scaled_a.mean()))
print('StandardizedwineStandardDeviation',scaled_a.std())
print('StandardizedprolineMean',int(scaled_b.mean()))
print('StandardizedprolineStandardDeviation',scaled_b.std())
print('StandardizedmalicacidMean',int(scaled_c.mean()))
print('StandardizedmalicacidStandardDeviation',scaled_c.std())
print('StandardizedashMean',int(scaled_d.mean()))
print('StandardizedashStandardDeviation',scaled_d.std())
print('StandardizedaclMean',int(scaled_e.mean()))
print('StandardizedaclStandardDeviation',scaled_e.std())
print('StandardizedmgMean',int(scaled_f.mean()))
print('StandardizedmgStandardDeviation',scaled_f.std())
print('StandardizedphenolMean',int(scaled_g.mean()))
print('StandardizedphenolStandardDeviation',scaled_g.std())
print('StandardizedflavanoidMean',int(scaled_h.mean()))
print('StandardizedflavanoidStandardDeviation',scaled_h.std())
print('Standardizednonfla.phenolMean',int(scaled_i.mean()))

print('Standardizednonfla.phenolStandardDeviation',scaled_i.std())

print('StandardizedproanthMean',int(scaled_j.mean()))
print('StandardizedproanthStandardDeviation',scaled_j.std())
print('Standardizedcolor.intMean',int(scaled_k.mean()))
print('Standardizedcolor.intStandardDeviation',scaled_k.std())
print('StandardizedhueMean',int(scaled_l.mean()))
print('StandardizedhueStandardDeviation',scaled_l.std())
print('StandardizedODMean',int(scaled_m.mean()))
print('StandardizedODStandardDeviation',scaled_m.std())
print('StandardizedprolineMean',int(scaled_n.mean()))
print('StandardizedprolineStandardDeviation',scaled_n.std())