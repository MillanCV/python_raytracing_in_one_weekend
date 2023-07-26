if __name__ == "__main__":
    IMAGE_WIDTH: int = 256
    IMAGE_HEIGHT: int = 256
    
    print(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255')
    
    for j in range((IMAGE_HEIGHT - 1), -1, -1):
        for i in range(IMAGE_WIDTH):
            r: float = i / (IMAGE_WIDTH -1)
            g: float = j / (IMAGE_HEIGHT -1)
            b: float = 0.25
            
            ir: int = int(255.999 * r)
            ig: int = int(255.999 * g)
            ib: int = int(255.999 * b)
            
            print(f'{ir} {ig} {ib}')