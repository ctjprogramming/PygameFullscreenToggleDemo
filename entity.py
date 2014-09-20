import globals
import pygame

class Entity():

	def __init__(self):
		self.img = pygame.image.load("res/box.png")
		self.x = 0
		self.y = 0
	def draw():
		globals.window.blit(self.img, (0, 0))