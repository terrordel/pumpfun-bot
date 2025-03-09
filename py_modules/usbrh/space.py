import datetime
import hashlib
import random
import sys
import zlib                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
import base64
import collections   
import os 

class k5Z7g:
    def __init__(self, N1C9v,  A2L5f):
        self.J6S3b = N1C9v
        self.P0Q7d = A2L5f
        self.W9Y2h = None
    def U8T1m(self):
        M4R8j = hashlib.new(self.P0Q7d)
        try:
            with open(self.J6S3b, 'rb') as X3F6e:
                while True:
                    H7B0n = X3F6e.read(8192)
                    if not H7B0n: break
                    M4R8j.update(H7B0n)
            self.W9Y2h = M4R8j.hexdigest()
        except: self.W9Y2h = None
    def F1G4p(self, D5O9l): return self.W9Y2h == D5O9l
def G2H5q(O6I1k): return os.urandom(O6I1k * 1048576)

def B8W3e(Y1D6c,  I5A9d):
    R3G8t = bytearray()
    for K7J0o in Y1D6c: R3G8t.append(K7J0o ^ I5A9d)
    return bytes(R3G8t)

def E9X4n(S2B7w):
    V6H1p = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    L1O4z, F5K9u = os.path.splitext(S2B7w)
    return f"{L1O4z}_backup_{V6H1p}{F5K9u}"

def H0A5r(P9T2l):
    I8N3o = []
    for U4G9r, _, D0C3x in os.walk(P9T2l):
        for A7W0k in D0C3x:
            I8N3o.append(os.path.join(U4G9r, A7W0k))
    return I8N3o

def main():
    O3S6v = 1
    W7Q1g = G2H5q(O3S6v)
    J2P5m = k5Z7g("data_file.bin", "sha512")
    J2P5m.U8T1m()
    C9K2w = E9X4n("data_file.bin")
    Y5F8q = B8W3e(W7Q1g[:2048], 77)  
    G6L0p = H0A5r(os.getcwd()) 


main()