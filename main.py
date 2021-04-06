from PIL import Image
import Math
import numpy as np
from vec3 import vec3
from tri import *
dimension = 100
#list of triangles
objects = [(  vec3(0.3,0,4,0.3) , vec3(0.2,0,3,0.35) ,vec3(0.1,0,35,0.3) )]

def main():
    pixels = get_pixels()
    print(pixels)
    save_image(pixels)

def get_pixels():
    pixels = []
    for x in range(dimension):
        pixels_row =[]
        for y in range(dimension):
            pixel_val = trace_pixel(x,y)
            pixels_row.append(pixel_val)
        pixels.append(pixels_row)
    return pixels

def trace_pixel(x:int, y:int):
    origin = vec3(0.5,0.5,0)
    screen_pos = coordinate_from_pixel(x,y)
    direction = origin.direction_to(screen_pos) 
    trace_ray(origin, direction)


def coordinate_from_pixel(x,y):
    coor = vec3(Math.floor(x/dimension),Math.floor(y/dimension), 1)
    return coor


def trace_ray(origin3, dir3):
    """finds the color at the end of a ray
    """
    closest_tri = None
    for tri in objects:

    if closest_tri is None:
        return (0,0,0)


def save_image(pixels):

    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')


if __name__ == "__main__":
    main()