import pygame
import time
from piece import Check
from piece import Queen


class Board:

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		self.select = (-1,-1)
		self.pos = []
		self.posibilities = []
		self.takepos = []
		self.board = [[0 for x in range(8)] for _ in range(rows)]

		self.board[0][0] = Check(0,0,False)
		self.board[0][2] = Check(0,2,False)
		self.board[0][4] = Check(0,4,False)
		self.board[0][6] = Check(0,6,False)
		self.board[1][1] = Check(1,1,False)
		self.board[1][3] = Check(1,3,False)
		self.board[1][5] = Check(1,5,False)
		self.board[1][7] = Check(1,7,False)
		self.board[2][0] = Check(2,0,False)
		self.board[2][2] = Check(2,2,False)
		self.board[2][4] = Check(2,4,False)
		self.board[2][6] = Check(2,6,False)

		self.board[7][1] = Check(7,1,True)
		self.board[7][3] = Check(7,3,True)
		self.board[7][5] = Check(7,5,True)
		self.board[7][7] = Check(7,7,True)
		self.board[6][0] = Check(6,0,True)
		self.board[6][2] = Check(6,2,True)
		self.board[6][4] = Check(6,4,True)
		self.board[6][6] = Check(6,6,True)
		self.board[5][1] = Check(5,1,True)
		self.board[5][3] = Check(5,3,True)
		self.board[5][5] = Check(5,5,True)
		self.board[5][7] = Check(5,7,True)

	def show_pos(self, win, i, j, currentW):
		if self.select[0]>=0 and self.select[1]>=0:
			self.close(self.select[0],self.select[1])
		self.select = (i,j)
		self.board[i][j].switch()

		x = j / 8 * 520 + 118
		y = i / 8 * 520 + 118

		if isinstance(self.board[i][j], Check):
			if self.board[i][j].white and currentW:
				if i-1>=0 and j-1>=0 and (self.board[i-1][j-1] == 0) :
					self.pos.append((x-42,y-43))
					self.posibilities.append((i-1,j-1))
				if i-1>=0 and j+1<8 and (self.board[i-1][j+1] == 0):
					self.pos.append((x+88,y-43))
					self.posibilities.append((i-1,j+1))
				if i-2>=0 and j-2>=0 and (isinstance(self.board[i-1][j-1], Check) and not self.board[i-1][j-1].white) and self.board[i-2][j-2] == 0:
					self.pos.append((x-107,y-108))
					self.takepos.append((i-2,j-2))
				if i-2>=0 and j+2<8 and (isinstance(self.board[i-1][j+1], Check) and not self.board[i-1][j+1].white) and self.board[i-2][j+2] == 0:
					self.pos.append((x+153,y-108))
					self.takepos.append((i-2,j+2))

			elif not self.board[i][j].white and not currentW:
				if i+1>=0 and j-1>=0 and self.board[i+1][j-1] == 0:
					self.pos.append((x-42,y+87))
					self.posibilities.append((i+1,j-1))
				if i+1>=0 and j+1<8 and self.board[i+1][j+1] == 0:
					self.pos.append((x+88,y+87))
					self.posibilities.append((i+1,j+1))
				if i+2>=0 and j-2>=0 and (isinstance(self.board[i+1][j-1], Check) and self.board[i+1][j-1].white) and self.board[i+2][j-2] == 0:
					self.pos.append((x-107,y+152))
					self.takepos.append((i+2,j-2))
				if i+2>=0 and j+2<8 and (isinstance(self.board[i+1][j+1], Check) and self.board[i+1][j+1].white) and self.board[i+2][j+2] == 0:
					self.pos.append((x+153,y+152))
					self.takepos.append((i+2,j+2))

	def checkandmove(self,i,j):
		for po in self.posibilities:
			if i == po[0] and j == po[1]:
				self.move(i,j)
				return True

	def takeandmove(self,i,j):
		for po in self.takepos:
			if i == po[0] and j == po[1]:
				self.remove(int((self.select[0]+i)/2),int((self.select[1]+j)/2))
				self.move(i,j)

				return True

	def remove(self, i,j):
		self.board[i][j] = 0

	def move(self,i,j):
		self.board[self.select[0]][self.select[1]].switch()
		self.board[self.select[0]][self.select[1]].move(i,j)
		self.board[i][j] = self.board[self.select[0]][self.select[1]]
		self.board[self.select[0]][self.select[1]] = 0
		self.pos = []
		self.posibilities = []
		self.takepos = []
		self.select = (-1,-1)

	def close(self, i, j):
		self.board[i][j].switch()
		self.select = (-1,-1)
		self.pos = []
		self.posibilities = []
				
	def draw(self, win):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.board[i][j] != 0:
					self.board[i][j].draw(win)
		for i in self.pos:
			pygame.draw.rect(win,(255,0,0), (i[0],i[1],15,15),5)	