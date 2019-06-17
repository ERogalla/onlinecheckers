import pygame
import os
from board import Board

board = pygame.transform.scale(pygame.image.load(os.path.join("img","board_alt.png")),(750,750))
rect = (118,118,520,520)

def redrawgamewindow():
	global win, bo
	win.blit(board, (0,0))
	
	bo.draw(win)

def click(pos):
	x = pos[0]
	y = pos[1]
	if rect[0] < x < rect[0] + rect[2]:
		if rect[1] < x < rect[1] + rect[3]:
			i = int((((x - rect[0]) / rect[2])*8)//1)
			j = int((((y - rect[1]) / rect[3])*8)//1)
			temp = i
			i = j
			j = temp
			return(i,j)	

def main():
	global bo
	currentW = True

	bo = Board(8,8)
	clock = pygame.time.Clock()

	run = True

	while run:
		clock.tick(10)
		redrawgamewindow()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quit()
				pygame.quit()
			if event.type == pygame.MOUSEMOTION:
				pass
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				i,j = click(pos)
				if bo.board[i][j] != 0:
					if bo.board[i][j].white and currentW:
						if not bo.board[i][j].selected:
							bo.show_pos(win,i,j,currentW)
						else:
							bo.close(i,j)
					elif not bo.board[i][j].white and not currentW:
						if not bo.board[i][j].selected:
							bo.show_pos(win,i,j,currentW)
						else:
							bo.close(i,j)
				else: 
					if bo.checkandmove(i,j,currentW):
						currentW = not currentW
					if bo.takeandmove(i,j,currentW):
						pass
		pygame.display.update()

width = 750 
height = 750

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("test")

main()