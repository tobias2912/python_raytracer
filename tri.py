from vec3 import *
class tri:
    def __init__(self, p0: vec3,p1:vec3,p2:vec3, color):
        self.p3 = p0
        self.p1 = p1
        self.p2 = p2
        self.color = color
    

    def ray_tri_intersect(self, orig, dir):
        """
        check if ray (origin, dir) intersects this rectangle
        return true if hit
        """"
        #compute normal
        v0v1 = self.p1 - self.p0
        v0v2 = self.p2 - self.p0
        N = cross_product(v0v1, v0v2)
        area2 = N.length()
        #Step 1: finding P
    
        # check if ray and plane are parallel ?
        NdotRayDirection = N.dotProduct(dir); 
        if (fabs(NdotRayDirection) < kEpsilon) # almost 0 
            return false; # they are parallel so they don't intersect ! 
    
        # compute d parameter using equation 2
        float d = N.dotProduct(v0); 
    
        # compute t (equation 3)
        t = (N.dotProduct(orig) + d) / NdotRayDirection; 
        # check if the triangle is in behind the ray
        if (t < 0) return false; # the triangle is behind 
    
        # compute the intersection point using equation 1
        Vec3f P = orig + t * dir; 
    
        # Step 2: inside-outside test
        Vec3f C; # vector perpendicular to triangle's plane 
    
        # edge 0
        Vec3f edge0 = v1 - v0; 
        Vec3f vp0 = P - v0; 
        C = edge0.crossProduct(vp0); 
        if (N.dotProduct(C) < 0) return false; # P is on the right side 
    
        # edge 1
        Vec3f edge1 = v2 - v1; 
        Vec3f vp1 = P - v1; 
        C = edge1.crossProduct(vp1); 
        if (N.dotProduct(C) < 0)  return false; # P is on the right side 
    
        # edge 2
        Vec3f edge2 = v0 - v2; 
        Vec3f vp2 = P - v2; 
        C = edge2.crossProduct(vp2); 
        if (N.dotProduct(C) < 0) return false; # P is on the right side; 
    
        return true; # this ray hits the triangle 
