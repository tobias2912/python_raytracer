from PIL import Image
import math
import numpy as np
from vec3 import vec3
from tri import *
dimension = 100
#list of triangles
def test():
    objects = [tri(vec3(0.1,0.1,1) , vec3(0.2,0.7,1) ,vec3(0.8,0.2,1), (255,255,0))]
    t = objects[0]
    origin = vec3(0.5,0.5,0)
    screen_pos = coordinate_from_pixel(5,5)
    direction = origin.direction_to(screen_pos) 
    t.ray_tri_intersect(origin, direction)
    print(t)

def main():
    if False:
        test()
    else:
        objects = [tri(vec3(0.1,0.1,1) , vec3(0.2,0.7,1) ,vec3(0.8,0.2,1), (255,255,100))]
        pixels = get_pixels(objects)
        save_image(pixels)

def get_pixels(objects):
    pixels = []
    for x in range(dimension):
        pixels_row =[]
        for y in range(dimension):
            pixel_val = trace_pixel(x,y, objects)
            pixels_row.append(pixel_val)
        pixels.append(pixels_row)
    return pixels

def trace_pixel(x:int, y:int, objects):
    origin = vec3(0.5,0.5,0)
    screen_pos = coordinate_from_pixel(x,y)
    direction = origin.direction_to(screen_pos) 
    color = trace_ray(origin, direction, objects)
    return color


def coordinate_from_pixel(x,y):
    coor = vec3((x/dimension),(y/dimension), 1)
    return coor


def trace_ray(origin3, dir3, objects):
    """finds the color at the end of a ray
    """
    closest_tri = None
    for tri in objects:
        if tri.ray_tri_intersect(origin3, dir3):
            closest_tri = tri
            print(dir3)
    if closest_tri is None:
        return (255,255,255)
    else:
        
        return closest_tri.color


def save_image(pixels):

    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')


if __name__ == "__main__":
    main()