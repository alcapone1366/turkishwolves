# importing working libraries
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

#================================
# square objects are the building blocks of our snakw
class Cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
 
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


#======================================================
class Snake(object):
	snake_body = []
    snake_turns = {}
    def __init__(self, inColor, inPosition):
    	self.color = inColor
        self.theHead = Cube(inPosition)
        self.snake_body.append(self.theHead)

        # snake is either moving left, right or, or up,down at a time
        self.x_move = 0
        self.y_move = 1 
                
	def move(self):

		for event in pygame.event.get():
			pygame.event.type = pygame.QUIT:
				pygame.quit()
		
		keys = pygame.key.get_pressed()

		for key in keys:
			if(keys[pygame.K_LEFT]):
				self.x_move = -1
				self.y_move = 0
				self.snake_turns[self.theHead.position[:]] = [self.x_move, self.y_move]

			elif(keys[pygame.K_RIGHT]):
				self.x_move = 1
				self.y_move = 0
				self.snake_turns[self.theHead.position[:]] = [self.x_move, self.y_move]

			elif(keys[pygame.K_UP]):
				self.x_move = 0
				self.y_move = -1
				self.snake_turns[self.theHead.position[:]] = [self.x_move, self.y_move]


			elif(keys[pygame.K_DOWN]):
				self.x_move = 0
				self.y_move = 1
				self.snake_turns[self.theHead.position[:]] = [self.x_move, self.y_move]
		
		for index, cube_element in enumerate(self.snake_body):

			temp_position = cube_element.position[:]

			if temp_position in self.snake_turns:
				temp_turn = self.snake_turns[temp_position]
				cube_element.move(temp_turn[0], temp_turn[1])

				if (index == len(self.snake_body) - 1):
					self.snake_turns.pop(temp_position)
			

			else:
				if (cube_element.x_move == -1 and cube_element.position[0] <= 0):
					cube_element.position = (cube_element.rows -1, cube_element.position[1])
				
				elif (cube_element.x_move == 1 and cube_element.position[0] >= cube_element.rows - 1):
					cube_element.position = (0, cube_element.position[1])

				elif (cube_element.y_move == 1 and cube_element.position[1] >= cube_element.rows - 1):
					cube_element.position = (cube_element.position[0], cube_element.rows -1)


				elif (cube_element.y_move) == 1 and cube_element.position[1] >= cube_element.rows - 1):
					cube_element.position = (cube_element.position[0], 0)

                elif (cube_element.y_move == -1 and cube_element.position[1] <= 0):
					 cube_element.position = (cube_element.position[0],cube_element.rows-1)

                else: cube_element.move(cube_element.x_move,c.y_move)

#===============================
def drawGrid(aWidth, aHeight, rows, columns, aSurface):
    
    horizontal_block_size = my_width // my_columns
    vertical_block_size=  my_height // my_rows

    x = 0
    y = 0

    for i in range(my_rows):
        x  = x + horizontal_block_size
        pygame.draw.line(aSurface, (255,255,255), (x,0), (x, my_width), 2)

    for i in range(my_columns):
        y  = y + vertical_block_size
        pygame.draw.line(aSurface, (255,255,255), (0,y), (my_height, y),2)


def redrawWindow(aSurface):
    global my_rows, my_width, my_height, my_columns
    aSurface.fill((48,10,36))
    drawGrid(my_width, my_height, my_rows, my_columns, aSurface)
    pygame.display.update()



def main():
    global my_width, my_height, my_rows, my_columns
    my_width = 600
    my_height = 1200
    display_window = pygame.display.set_mode((my_width, my_height))
    my_rows = 30
    my_columns = 15

    snake_head_color = (255,0,0)
    initial_position = (25,25)
    
    # my_snake = Snake(snake_head_color, initial_position)
    flag = True
    my_clock = pygame.time.Clock()
    while(flag):
        pygame.time.delay(69)
        my_clock.tick(10)
        redrawWindow(display_window)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main()