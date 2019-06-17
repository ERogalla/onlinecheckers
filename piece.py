import pygame
import os

b_check = pygame.image.load(os.path.join("img","bcheck.png"))
w_check = pygame.image.load(os.path.join("img","wcheck.png"))
b_queen = pygame.image.load(os.path.join("img","bqueen.png"))
w_queen = pygame.image.load(os.path.join("img","wqueen.png"))

b = [b_check,b_queen]
w = [w_check,w_queen]

B = []
W = []

for img in b:
	B.append(pygame.transform.scale(img,(55,55)))
for img in w:
	W.append(pygame.transform.scale(img,(55,55)))



class Piece:
	img = -1
	rect = (118,118,520,520)
	startX = rect[0]
	startY = rect[1]

	def __init__(self, row, col, white):
		self.row = row
		self.col = col
		self.white = white
		self.selected = False


	def move(self,i,j):
		self.row = i
		self.col = j
		

	def switch(self):
		self.selected = not self.selected

	def draw(self,win):
		if self.white:
			drawthis = W[self.img]	
		else:
			drawthis = B[self.img]


		x = round(self.startX + (self.col * self.rect[2]/8))
		y = round(self.startY + (self.row * self.rect[2]/8))

		win.blit(drawthis, (x,y)) 

		if self.selected:
			pygame.draw.rect(win,(255,0,0), (x,y,55,55),2)



class Check(Piece):
	img = 0

class Queen(Piece):
	img = 1