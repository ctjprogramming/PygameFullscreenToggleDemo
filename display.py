import globals

# int x, int y, bool fullscreen
def update_display_mode():
	if(globals.fullscreen):
		globals.window = globals.pygame.display.set_mode((globals.width, globals.height), globals.pygame.FULLSCREEN)
	else:
		globals.window = globals.pygame.display.set_mode((globals.width, globals.height))

def toggle_fullscreen():
	globals.fullscreen = not globals.fullscreen
	update_display_mode()