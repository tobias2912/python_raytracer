from PIL import Image
import math
import numpy as np
from vec3 import vec3
from tri import *
dimension = 20
background = (30,30,30)

def test():
    objects = []
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
        objects = get_objects() 
        pixels = get_pixels(objects)
        save_image(pixels)

def get_objects():
    """reads all triangles from a csv file
    returns list of triangles
    """
    color_presets = {'white':(255,255,255), 'blue':(0,0,255)}
    f = open('objects.csv')
    objects = []
    for line in f:
        if '/' in line:
            continue
        params = line.split('-')
        v0 = vec_from_line(params[0])
        v1 = vec_from_line(params[1])
        v2 = vec_from_line(params[2])
        color_str = params[3].strip()
        print(color_str)
        if color_str.strip() in color_presets:
            #preset color
            color = color_presets[(color_str)]
        else:
            colors = [int(s) for s in color_str.split(',')]
            color = (colors[0], colors[1], colors[2])
        
        t = tri(v0, v1,v2, color)
        objects.append(t)
    print(objects)
    return objects


def vec_from_line(str):
    nums = str.split(',')
    v = vec3(float(nums[0]), float(nums[1]), float(nums[2]))
    return v


def get_pixels(objects):
    """does a raytrace for every pixel
    returns list of pixels
    """
    flip_v = -1
    flip_h = 1
    pixels = []
    for y in range(dimension)[::flip_v]:
        pixels_row =[]
        for x in range(dimension)[::flip_h]:
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
    closest_t = None
    for tri in objects:
        t = tri.ray_tri_intersect(origin3, dir3)
        if t is not False:
            if closest_t is None or t < closest_t:
                closest_tri = tri
                closest_t = t
                print(t)

    if closest_tri is None:
        return background
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