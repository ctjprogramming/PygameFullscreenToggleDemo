import globals
def render(entities):
	for entity in entities:
		globals.window.blit(entity.img, (entity.x, entity.y))