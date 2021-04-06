import numpy as np
import Math
class vec3:

    def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z


    def direction_to(self, other:vec3) -> vec3:
        """return a vec3 pointing from self to other"""
        return self-other

    def __add__(self, other):
        return vec3(other.x + self.x, other.y+self.y, other.z+self.z)

    def __sub__(self, other):
        return vec3(other.x - self.x, other.y-self.y, other.z-self.z)

    def length(self):
        return Math.sqrt(self.x**2, self.y**2, self.z**2)

    def numpyarray(self):
        return np.array([self.x,self.y,self.z])
    
def cross_product(v1:vec3, v2:vec3)->vec3:
    a = [v1.x, v1.y, v1.z]
    b = [v2.x, v2.y, v2.z]
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return vec3(c[0],c[1],c[2])


def dot_product(v1:vec3, v2:vec3):
    return np.dot(v1.numpyarray(), v2.numpyarray())