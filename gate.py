import numpy as np
from mkvcli import MKV

class MultiplyGate:
    def forward(self,W, x):
        return np.dot(W, x)

    def forward0(self, k0, k1):
        return MKV.Mul(k0, k1, 60)

    def backward(self, W, x, dz):
        dW = np.asarray(np.dot(np.transpose(np.asmatrix(dz)), np.asmatrix(x)))
        dx = np.dot(np.transpose(W), dz)
        return dW, dx
class AddGate:
    def forward(self, x1, x2):
        return x1 + x2

    def backward(self, x1, x2, dz):
        dx1 = dz * np.ones_like(x1)
        dx2 = dz * np.ones_like(x2)
        return dx1, dx2