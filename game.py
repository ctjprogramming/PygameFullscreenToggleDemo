import globals
import pygame
from inputs import Inputs
from entity import Entity
from render import render
from display import update_display_mode, toggle_fullscreen

globals.width = 640
globals.height = 480
globals.fullscreen = False

def main():

	pygame.init()

	globals.pygame = pygame
	globals.inputs = Inputs(pygame)
	update_display_mode()
	clock = pygame.time.Clock()

	entities = []

	entities.append(Entity())

	loop = True

	while(loop):
		clock.tick(60)
		globals.inputs.update()

		render(entities)

		if(globals.inputs.K_SPACE): toggle_fullscreen()
		if(globals.inputs.K_ESCAPE): loop = False
		if(globals.inputs.isQuitPressed()): loop = False

		pygame.display.flip()

	pygame.quit()

main()