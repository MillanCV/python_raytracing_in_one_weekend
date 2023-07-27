from vec3 import Color

def write_color(pixel_color: Color):
    print(f'{int(255.999 * pixel_color.x())} {int(255.999 * pixel_color.y())} {int(255.999 * pixel_color.z())}')