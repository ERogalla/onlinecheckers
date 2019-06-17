import pygame
import time
from piece import Check
from piece import Queen


class Board:

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		self.select = (-1,-1)
		self.coordpos = []
		self.pos = []
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

		if isinstance(self.board[i][j], Check) or isinstance(self.board[i][j], Queen):
			if self.board[i][j].white and currentW:
				self.checkW(i,j,x,y,currentW)
				if isinstance(self.board[i][j], Queen):
					self.checkB(i,j,x,y,currentW)		
			elif not self.board[i][j].white and not currentW:
				self.checkB(i,j,x,y,currentW)
				if isinstance(self.board[i][j], Queen):
					self.checkW(i,j,x,y,currentW)				

	def checkW(self,i,j,x,y,currentW):
		if i-1>=0 and j-1>=0 and (self.board[i-1][j-1] == 0) :
			self.moveupleft(i,j,x,y)
		if i-1>=0 and j+1<8 and (self.board[i-1][j+1] == 0):
			self.moveupright(i,j,x,y)
		if i-2>=0 and j-2>=0 and ((isinstance(self.board[i-1][j-1], Check) or isinstance(self.board[i-1][j-1], Queen)) and self.board[i-1][j-1].white is not currentW) and self.board[i-2][j-2] == 0:
			self.takeupleft(i,j,x,y)
		if i-2>=0 and j+2<8 and ((isinstance(self.board[i-1][j+1], Check) or isinstance(self.board[i-1][j+1], Queen)) and self.board[i-1][j+1].white is not currentW) and self.board[i-2][j+2] == 0:
			self.takeupright(i,j,x,y)

	def checkB(self,i,j,x,y,currentW):
		if i+1<8 and j-1>=0 and self.board[i+1][j-1] == 0:
			self.movedownleft(i,j,x,y)
		if i+1<8 and j+1<8 and self.board[i+1][j+1] == 0:
			self.movedownright(i,j,x,y)
		if i+2<8 and j-2>=0 and ((isinstance(self.board[i+1][j-1], Check) or isinstance(self.board[i+1][j-1], Queen)) and self.board[i+1][j-1].white is not currentW) and self.board[i+2][j-2] == 0:
			self.takedownleft(i,j,x,y)
		if i+2<8 and j+2<8 and ((isinstance(self.board[i+1][j+1], Check) or isinstance(self.board[i+1][j+1], Queen)) and self.board[i+1][j+1].white is not currentW) and self.board[i+2][j+2] == 0:
			self.takedownright(i,j,x,y)

	def moveupleft(self,i,j,x,y):
		self.coordpos.append((x-42,y-43))
		self.pos.append((i-1,j-1))

	def moveupright(self,i,j,x,y):
		self.coordpos.append((x+88,y-43))
		self.pos.append((i-1,j+1))

	def movedownleft(self,i,j,x,y):
		self.coordpos.append((x-42,y+87))
		self.pos.append((i+1,j-1))

	def movedownright(self,i,j,x,y):
		self.coordpos.append((x+88,y+87))
		self.pos.append((i+1,j+1))

	def takeupleft(self,i,j,x,y):
		self.coordpos.append((x-107,y-108))
		self.takepos.append((i-2,j-2))

	def takeupright(self,i,j,x,y):
		self.coordpos.append((x+153,y-108))
		self.takepos.append((i-2,j+2))

	def takedownleft(self,i,j,x,y):
		self.coordpos.append((x-107,y+152))
		self.takepos.append((i+2,j-2))

	def takedownright(self,i,j,x,y):
		self.coordpos.append((x+153,y+152))
		self.takepos.append((i+2,j+2))

	def checkandmove(self,i,j,currentW):
		for po in self.pos:
			if i == po[0] and j == po[1]:
				if (currentW and i == 0) or (not currentW and i==7):
					self.promote(i,j,currentW)
				else:
					self.move(i,j)
				currentW = not currentW
				return True

	def takeandmove(self,i,j,currentW):
		for po in self.takepos:
			if i == po[0] and j == po[1]:
				self.remove(int((self.select[0]+i)/2),int((self.select[1]+j)/2))
				if (currentW and i == 0) or (not currentW and i==7):
					self.promote(i,j,currentW)
				else:
					self.move(i,j)
				return True

	def remove(self, i,j):
		self.board[i][j] = 0

	def move(self,i,j):
		self.board[self.select[0]][self.select[1]].switch()
		self.board[self.select[0]][self.select[1]].move(i,j)
		self.board[i][j] = self.board[self.select[0]][self.select[1]]
		self.board[self.select[0]][self.select[1]] = 0
		self.coordpos = []
		self.pos = []
		self.takepos = []
		self.select = (-1,-1)

	def promote(self,i,j,currentW):
		self.board[self.select[0]][self.select[1]] = 0
		self.board[i][j] = Queen(i,j,currentW)
		self.coordpos = []
		self.pos = []
		self.takepos = []
		self.select = (-1,-1)

	def close(self, i, j):
		self.board[i][j].switch()
		self.select = (-1,-1)
		self.coordpos = []
		self.pos = []
				
	def draw(self, win):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.board[i][j] != 0:
					self.board[i][j].draw(win)
		for i in self.coordpos:
			pygame.draw.rect(win,(255,0,0), (i[0],i[1],15,15),5)	