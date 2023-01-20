import pygame
pygame.init()
#ekraaniseaded
screen=pygame.display.set_mode([300, 300])
pygame.display.set_caption("My Screen")
screen.fill([0, 100, 0])
#joonistamine
pygame.draw.circle(screen, [255, 255, 255], [150,80], 30, 0)
pygame.draw.circle(screen, [255, 255, 255], [150,145], 40, 0)
pygame.draw.circle(screen, [255, 255, 255], [150,230], 50, 0)
pygame.draw.circle(screen, [0, 0, 0], [140,75], 5, 0)
pygame.draw.circle(screen, [0, 0, 0], [160,75], 5, 0)
pygame.draw.circle(screen, [255, 102, 0], [150,85], 5, 0)

#käed
pygame.draw.line(screen,[204, 102, 0],(25,225),(375,225),2)

pygame.display.flip()
#loop

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
