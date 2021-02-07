import pygame
#import clock

'''
events:
=======
JOYAXISMOTION 7
JOYBALLMOTION 8
JOYBUTTONDOWN 10
JOYBUTTONUP 11
JOYHATMOTION 9
'''


# init
joysticks = []
clock = pygame.time.Clock()

# maximální krok v jednom kole
lx = 10
ly = 10
lz = -10

x, y, z = (127.0, 127.0, 32.0)
dx, dy, dz = (0.0, 0.0, 0.0)
#loc = (x, y, z)

# Indicates pygame is running
run = True

try:
    pygame.init()
except:
    exit()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("X-BOX")


for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))

j = joysticks[-1]
j.init()

print(joysticks[-1])

#print(f'JOYAXISMOTION {pygame.JOYAXISMOTION}\nJOYBALLMOTION {pygame.JOYBALLMOTION}\nJOYBUTTONDOWN {pygame.JOYBUTTONDOWN}\nJOYBUTTONUP {pygame.JOYBUTTONUP}\nJOYHATMOTION {pygame.JOYHATMOTION}')

while run:
    clock.tick(20) # 20 frames pes second
    clock.tick(20) # 20 frames pes second
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # it will make exit the while loop
            run = False

        dx = round(lx * j.get_axis(0), 2)
        dy = round(ly * j.get_axis(1), 2)
        dz = round(lz * j.get_axis(3), 2)

    x = x + dx
    y = y + dy
    z = z + dz



    print(x, y, z)

        # completely fill the surface object
    # with black colour
    win.fill((255, 255, 255))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (int(x), int(y), int(z), int(z)))

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()