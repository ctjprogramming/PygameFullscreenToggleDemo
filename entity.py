import globals
import pygame

class Entity(): # the base for all objects that will be drawn on the screen in the game

	def __init__(self):
		self.img = pygame.image.load("res/box.png") # default image
		self.x = 0 # default x coord
		self.y = 0 # default y coord

	def draw(self): # draw the entity's image on the screen at its coords
		globals.window.blit(self.img, (self.x, self.y))