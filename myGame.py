# importing working libraries
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

#================================
# square objects are the building blocks of our snakw
class Cube(object):
    rows = 40
    columns = 40
    width = 600
    height = 1200 
    def __init__(self, start_pos, x_move=1, y_move=0, color=(255,0,0)):
        self.position = start_pos
        self.x_move = x_move #1
        self.dirny = y_move # 0
        self.color = color
 
       
    def move(self, x_move, y_move):
        self.x_move = x_move
        self.y_move = y_move
        self.position = (self.position[0] + self.x_move, self.position[1] + self.y_move)
 
    def draw(self, aSurface, eyes=False):
        dist_x = self.width // self.rows
        dist_y = self.height // self.columns
        
        i = self.position[0]
        j = self.position[1]
 
        pygame.draw.rect(aSurface, self.color, (i*dist_x+1,j*dist_y+1, dist_x-2, dist_y-2))
        if eyes:
            centre = dist_x//2 # same as dist_y
            radius = 3
            circleMiddle = (i*dist_x+centre-radius,j*dist_y+8)
            circleMiddle2 = (i*dist_x + dist_x -radius*2, j*dist_y+8)
            pygame.draw.circle(surface, (255,255,255), circleMiddle, radius)
            pygame.draw.circle(surface, (255,255,255), circleMiddle2, radius)


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
			if (pygame.event.type == pygame.QUIT):
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

				elif (cube_element.y_move == 1 and cube_element.position[1] >= cube_element.rows - 1):
					cube_element.position = (cube_element.position[0], 0)

                elif (cube_element.y_move == -1 and cube_element.position[1] <= 0):
                    cube_element.position = (cube_element.position[0],cube_element.rows-1)

                else:
                    cube_element.move(cube_element.x_move,c.y_move)

    def draw(self, aSurface):
        for index, cube_element in enumerate(self.snake_body):
            if(i==0):
                cube_element.draw(aSurface, True)
            else:
                cube_element.draw(aSurface)
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
    global my_rows, my_width, my_height, my_columns, snake_instance
    aSurface.fill((48,10,36))
    snake_instance.draw(aSurface)
    drawGrid(my_width, my_height, my_rows, my_columns, aSurface)
    pygame.display.update()



def main():
    global my_width, my_height, my_rows, my_columns, snake_instance
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