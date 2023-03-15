import pygame as pg 
from sys import exit

from settings import *
from core import *

class Game:
	def __init__(self):
		self.w, self.h = WIDTH, HEIGHT
		pg.init()
		self.screen = pg.display.set_mode((self.w, self.h), vsync=1)
		self.clock = pg.time.Clock()
		self.core = Core()

	def checkEvents(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()

	def draw(self):
		self.screen.fill("black")
		self.core.draw()

	def update(self):
		pg.display.flip()
		self.clock.tick(FPS)
		pg.display.set_caption(f"{self.clock.get_fps() : .1f}")
		self.d_time = self.clock.tick(FPS)
		self.core.setup()
		
	def run(self):
		while True:
			self.checkEvents()
			self.update()
			self.draw()

if __name__ == "__main__":
	game = Game()
	game.run()