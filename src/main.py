import sys

from color import write_color
from ray import Ray
from vec3 import Vec3, Point3, Color, unit_vector

def hit_sphere(center: Point3, radius: float, r: Ray) -> bool:
    oc: Vec3 = r.get_origin() - center
    a = Vec3.dot(r.get_direction(), r.get_direction())
    b = 2.0 * Vec3.dot(oc, r.get_direction())
    c = Vec3.dot(oc, oc) - radius*radius
    discriminant = b*b - 4*a*c
    
    return (discriminant > 0)

def ray_color(ray: Ray) -> Color:
    if hit_sphere(center=Point3(0,0,-1), 
                  radius=0.5, 
                  r=ray):
        return Color(1, 0, 0)
    
    unit_direction: Vec3 = unit_vector(vector=ray.get_direction())
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
    
    origin: Point3 = Point3(0, 0, 0)
    horizontal: Vec3 = Vec3(VIEWPORT_WIDTH, 0, 0)
    vertical: Vec3 = Vec3(0, VIEWPORT_HEIGHT, 0)
    lower_left_corner: Vec3 = origin - horizontal/2 - vertical/2 - Vec3(0, 0 , FOCAL_LENGHT)
    
    print(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255')
    
    for j in range((IMAGE_HEIGHT - 1), -1, -1):
        print(f'\rScanlines remaining {j}', file=sys.stderr)
        for i in range(IMAGE_WIDTH):
            u = float(i) / (IMAGE_WIDTH - 1)
            v = float(j) / (IMAGE_HEIGHT - 1)
            ray = Ray(origin=origin, 
                      direction= lower_left_corner + horizontal*u + vertical*v - origin)
            color_pixel = ray_color(ray)
            write_color(pixel_color=color_pixel)
    
    print('Done', file=sys.stderr)