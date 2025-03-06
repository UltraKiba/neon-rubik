from vpython import *
import math
import time

scene = canvas(width=800, height=600, background=color.black)
scene.lights = [distant_light(direction=vector(0,0,-1), color=color.gray(0.5))]

# Neon color palette
neon_colors = {
    'front': vector(1, 0, 1),       # Neon Purple
    'back': vector(0.224, 1, 0.082),# Neon Green
    'left': vector(0.122, 0.318, 1),# Neon Blue
    'right': vector(1, 0.42, 0.207),# Neon Orange
    'top': vector(1, 0, 0.498),     # Neon Pink
    'bottom': vector(0.875, 1, 0)   # Neon Yellow
}

cubies = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            cubie = box(size=vector(0.9,0.9,0.9), pos=vector(x*1.1, y*1.1, z*1.1))
            
            # Determine dominant face for coloring
            max_coord = max(abs(x), abs(y), abs(z))
            if max_coord == 1:
                if abs(x) == 1: cubie.color = neon_colors['right'] if x > 0 else neon_colors['left']
                if abs(y) == 1: cubie.color = neon_colors['top'] if y > 0 else neon_colors['bottom']
                if abs(z) == 1: cubie.color = neon_colors['front'] if z > 0 else neon_colors['back']
            else:
                cubie.color = vector(0.2, 0.2, 0.2)  # Dark gray for internal pieces

cube = compound(cubies, origin=vector(0,0,0))

t = 0
while True:
    rate(60)
    t += 0.01
    
    # Dynamic rotation pattern
    x_angle = math.sin(t*2) * 0.05
    y_angle = math.cos(t*3) * 0.03
    z_angle = math.sin(t*1.5) * 0.02
    
    cube.rotate(angle=x_angle, axis=vector(1,0,0))
    cube.rotate(angle=y_angle, axis=vector(0,1,0))
    cube.rotate(angle=z_angle, axis=vector(0,0,1))
    
    # Add some positional variation
    cube.pos = vector(
        math.sin(t*1.2)*0.1,
        math.cos(t*0.8)*0.1,
        math.sin(t*0.5)*0.1
    )