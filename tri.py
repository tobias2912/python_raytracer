from vec3 import *
class tri:
    kEpsilon = 0.001
    def __init__(self, p0: vec3,p1:vec3,p2:vec3, color):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.color = color
    
    def __repr__(self):
        return 'tri '+str(self.p0)+'-'+str(self.p1)+'-'+str(self.p2)

    def ray_tri_intersect(self, orig, dir):
        """
        from https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/ray-triangle-intersection-geometric-solution
        check if ray (origin, dir) intersects this rectangle
        return true if hit
        """
        v0 = self.p0
        v1 = self.p1
        v2 = self.p2
        
        #compute normal
        v0v1 = self.p1 - self.p0
        v0v2 = self.p2 - self.p0
        N = v0v1.cross_product(v0v2)
        area2 = N.length()
        #Step 1: finding P
    
        # check if ray and plane are parallel ?
        NdotRayDirection = dot_product(N,dir); 
        if abs(NdotRayDirection) < self.kEpsilon: # almost 0 
            return False; # they are parallel so they don't intersect ! 
    
        # compute d parameter using equation 2
        d = dot_product(N,v0); 
    
        # compute t (equation 3)
        t = (dot_product(N,orig) + d) / NdotRayDirection; 
        # check if the triangle is in behind the ray
        if (t < 0):
            return False; # the triangle is behind 
    
        # compute the intersection point using equation 1
        P = orig + t * dir; 
    
        # Step 2: inside-outside test
        C = None # vector perpendicular to triangle's plane 
    
        # edge 0
        edge0 = v1 - v0; 
        vp0 = P - v0; 
        C = edge0.cross_product(vp0); 
        if (dot_product(N,C) < 0):
            return False; # P is on the right side 
    
        # edge 1
        edge1 = v2 - v1; 
        vp1 = P - v1; 
        C = edge1.cross_product(vp1); 
        if (dot_product(N,C) < 0):
            return False; # P is on the right side 
    
        # edge 2
        edge2 = v0 - v2; 
        vp2 = P - v2; 
        C = edge2.cross_product(vp2); 
        if (dot_product(N, C) < 0) :
            return False; # P is on the right side; 
    
        return True; # this ray hits the triangle 
