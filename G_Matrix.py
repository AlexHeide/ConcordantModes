import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

"""
    This class will be used to compute the G-matrix of the GF-Matrix Method.
    It should be constructed to give the flexibility of transformation via 
    the L-matrix.
"""

class G_Matrix(object):
    def __init__(self, zmat, s_vectors, options):
        self.zmat      = zmat
        self.s_vectors = s_vectors
        self.options   = options

    def run(self):
        B = self.s_vectors.B
        
        """
            Compute and temper G
        """
        tol = 1e-12
        u = np.array(self.zmat.masses)
        for i in range(len(u)):
            if self.zmat.atomList[i] == "X":
                u[i] = 0
            else:
                u[i] = 1./u[i]
        u = np.repeat(u,3)
        u = np.diag(u)
        # u = inv(u)
        self.G = B.dot(u.dot(B.T))
        self.G[np.abs(self.G) < tol] = 0
