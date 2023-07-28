import sys

from color import write_color
from ray import Ray
from vec3 import Vec3, Point3, Color, unit_vector

def ray_color(ray: Ray) -> Color:
    unit_direction: Vec3 = unit_vector(ray.direct())
    t = 0.5 * (unit_direction.y() + 1.0)
    return Color(1.0, 1.0, 1.0)*(1.0-t) + Color(0.5, 0.7, 1.0)*t

if __name__ == "__main__":
    
    # image
    ASPECT_RATIO = 16.0 / 9.0
    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = (int)(IMAGE_WIDTH / ASPECT_RATIO)
    
    # camera
    VIEWPORT_HEIGHT = 2.0
    VIEWPORT_WIDTH = ASPECT_RATIO * VIEWPORT_HEIGHT
    FOCAL_LENGHT = 1.0
    
    origin = Point3(0, 0, 0)
    horizontal = Vec3(VIEWPORT_WIDTH, 0, 0)
    vertical = Vec3(0, VIEWPORT_HEIGHT, 0)
    lower_left_corner = origin - horizontal*2 - vertical/2 - Vec3(0, 0 , FOCAL_LENGHT)
    
    print(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255')
    
    for j in range((IMAGE_HEIGHT - 1), -1, -1):
        print(f'\rScanlines remaining {j}', file=sys.stderr)
        for i in range(IMAGE_WIDTH):
            u = float(i) / (IMAGE_WIDTH - 1)
            v = float(j) / (IMAGE_HEIGHT - 1)
            ray = Ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)
            color_pixel = ray_color(ray)
            write_color(pixel_color=color_pixel)
    
    print('Done', file=sys.stderr)