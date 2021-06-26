import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
frame = 0 
started = False

# Game loop.
while True:
  screen.fill((255, 255, 255))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  if frame >= 60 and frame < 120:
      if frame % 2 == 0:
          screen.fill((0, 0, 0))

  if pygame.key.get_pressed()[pygame.K_SPACE]:
      started = True
  if started:
      frame += 1
  
  pygame.display.flip()
  fpsClock.tick(fps)