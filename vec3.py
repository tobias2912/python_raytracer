import numpy as np
import math
class vec3:

    def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z


    def direction_to(self, other):
        """return a vec3 pointing from self to other"""
        return self-other

    def __add__(self, other):
        return vec3(other.x + self.x, other.y+self.y, other.z+self.z)

    def __sub__(self, other):
        return vec3(other.x - self.x, other.y-self.y, other.z-self.z)
    
    def __mul__(self, other):
        return vec3(self.x*other, self.y*other, self.z*other)
    def __rmul__(self, other):
        
        return vec3(self.x*other, self.y*other, self.z*other)

    def length(self):
        return math.sqrt(self.x**2+ self.y**2+ self.z**2)
    
    def __repr__(self):
        return str(self.x)+','+str(self.y)+','+str(self.z)

    def numpyarray(self):
        return np.array([self.x,self.y,self.z])
    
    def cross_product(self,v1):
        v2 = self
        a = [v1.x, v1.y, v1.z]
        b = [v2.x, v2.y, v2.z]
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]
        return vec3(c[0],c[1],c[2])


def dot_product(v1:vec3, v2:vec3):
    return np.dot(v1.numpyarray(), v2.numpyarray())