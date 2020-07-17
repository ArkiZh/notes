from sklearn import preprocessing as pre
import numpy as np

X = [[ 1., -1.,  2.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]
X_normalzied = pre.normalize(X,norm='l2')
print(X_normalzied)
X_scaled = pre.scale(X)
print(X_scaled)
