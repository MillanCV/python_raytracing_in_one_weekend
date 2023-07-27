import sys

from color import write_color
from vec3 import Color

if __name__ == "__main__":
    IMAGE_WIDTH: int = 256
    IMAGE_HEIGHT: int = 256
    
    print(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255')
    
    for j in range((IMAGE_HEIGHT - 1), -1, -1):
        print(f'\rScanlines remaining {j}', file=sys.stderr)
        for i in range(IMAGE_WIDTH):
            pixel_color = Color(
                e0= i / (IMAGE_WIDTH -1),
                e1= j / (IMAGE_HEIGHT -1),
                e2=0.25
            )
            write_color(pixel_color=pixel_color)
    
    print('Done', file=sys.stderr)