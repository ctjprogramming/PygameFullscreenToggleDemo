import pygame

class Inputs():

	def __init__(self, pygame):
		# each hey is assigned a boolean for reference by game modules
		self.pygame = pygame
		self.up = False
		self.down = False
		self.left = False
		self.right = False
		self.K_w = False
		self.K_a = False
		self.K_s = False
		self.K_d = False
		self.K_i = False
		self.K_j = False
		self.K_k = False
		self.K_l = False
		self.K_up = False
		self.K_down = False
		self.K_left = False
		self.K_right = False
		self.K_KP8 = False
		self.K_KP4 = False
		self.K_KP5 = False
		self.K_KP6 = False
		self.K_KP0 = False
		self.K_KP_ENTER = False
		self.K_SPACE = False
		self.K_ESCAPE = False
		self.K_RETURN = False
		self.E_QUIT = False
		self.update()

	def update(self):
		pygame = self.pygame
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.E_QUIT = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					self.K_w = True
				if event.key == pygame.K_a:
					self.K_a = True
				if event.key == pygame.K_s:
					self.K_s = True
				if event.key == pygame.K_d:
					self.K_d = True
				if event.key == pygame.K_i:
					self.K_i = True
				if event.key == pygame.K_j:
					self.K_j = True
				if event.key == pygame.K_k:
					self.K_k = True
				if event.key == pygame.K_l:
					self.K_l = True
				if event.key == pygame.K_SPACE:
					self.K_SPACE = True
				if event.key == pygame.K_ESCAPE:
					self.K_ESCAPE = True
				if event.key == pygame.K_RETURN:
					self.K_RETURN = True
				if event.key == pygame.K_UP:
					self.K_up = True
				if event.key == pygame.K_DOWN:
					self.K_down = True
				if event.key == pygame.K_RIGHT:
					self.K_right = True
				if event.key == pygame.K_LEFT:
					self.K_left = True
				if event.key == pygame.K_KP8:
					self.K_KP8 = True
				if event.key == pygame.K_KP4:
					self.K_KP4 = True
				if event.key == pygame.K_KP5:
					self.K_KP5 = True
				if event.key == pygame.K_KP6:
					self.K_KP6 = True
				if event.key == pygame.K_KP0:
					self.K_KP0 = True
				if event.key == pygame.K_KP_ENTER:
					self.K_KP_ENTER = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.K_w = False
				if event.key == pygame.K_a:
					self.K_a = False
				if event.key == pygame.K_s:
					self.K_s = False
				if event.key == pygame.K_d:
					self.K_d = False
				if event.key == pygame.K_i:
					self.K_i = False
				if event.key == pygame.K_j:
					self.K_j = False
				if event.key == pygame.K_k:
					self.K_k = False
				if event.key == pygame.K_l:
					self.K_l = False
				if event.key == pygame.K_SPACE:
					self.K_SPACE = False
				if event.key == pygame.K_ESCAPE:
					self.K_ESCAPE = False
				if event.key == pygame.K_RETURN:
					self.K_RETURN = False
				if event.key == pygame.K_UP:
					self.K_up = False
				if event.key == pygame.K_DOWN:
					self.K_down = False
				if event.key == pygame.K_RIGHT:
					self.K_right = False
				if event.key == pygame.K_LEFT:
					self.K_left = False
				if event.key == pygame.K_KP8:
					self.K_KP8 = False
				if event.key == pygame.K_KP4:
					self.K_KP4 = False
				if event.key == pygame.K_KP5:
					self.K_KP5 = False
				if event.key == pygame.K_KP6:
					self.K_KP6 = False
				if event.key == pygame.K_KP0:
					self.K_KP0 = False
				if event.key == pygame.K_KP_ENTER:
					self.K_KP_ENTER = False

	def isKeyDown(self, key):
		key = key.lower()
		if key == "up": return self.K_up
		if key == "down": return self.K_down
		if key == "left": return self.K_left
		if key == "right": return self.K_right
		if key == "w": return self.K_w
		if key == "a": return self.K_a
		if key == "s": return self.K_s
		if key == "d": return self.K_d
		if key == " ": return self.K_SPACE
		if key == "space": return self.K_SPACE
		if key == "return": return self.K_RETURN
		if key == "enter": return self.K_RETURN
		if key == "escape": return self.K_ESCAPE
		if key == "i": return self.K_i
		if key == "j": return self.K_j
		if key == "k": return self.K_k
		if key == "l": return self.K_l
		if key == "kp8": return self.K_KP8
		if key == "kp4": return self.K_KP4
		if key == "kp5": return self.K_KP5
		if key == "kp6": return self.K_KP6
		if key == "kp0": return self.K_KP0
		if key == "kp_enter": return self.K_KP_ENTER

	def isQuitPressed(self):
		return self.E_QUIT
