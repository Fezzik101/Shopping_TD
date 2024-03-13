import pygame
from pygame import gfxdraw

#USER VARIABLES
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
FRAMERATE = 60

#Initialize PyGame
pygame.init()
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Framerate clock
engine_clock = pygame.time.Clock()

#MAIN LOOP
running = True
while running:
	display.fill((0, 0, 0))
	engine_clock.tick(FRAMERATE)
	pygame.display.set_caption(
	    f"TEMP  |  Frames Per Second: {int(engine_clock.get_fps())}, Target FPS:{FRAMERATE}"
	)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			print("Attempting to close...")

	for i in range(100):
		# gfxdraw.aacircle(display, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
		#                  WINDOW_WIDTH // 4, (255, 255, 255))
		pygame.draw.circle(display, (255, 255, 255),
		                   (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
		                   WINDOW_HEIGHT // 4, 1)
	pygame.display.update()

pygame.quit()
raise SystemExit
