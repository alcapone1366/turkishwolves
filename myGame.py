# importing working libraries
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

#================================
# square objects are the building blocks of our snakw


# class Snake(inColor, init_pos):
#     pass



#===============================
def drawGrid(aWidth, aHeight, rows, columns, aSurface):
    
    horizontal_block_size = my_width // my_rows
    vertical_block_size =  my_height // my_rows

    x = 0
    y = 0

    for i in range(my_rows):
        x  = x + horizontal_block_size
        pygame.draw.line(aSurface, (255,255,255), (x,0), (x, my_width), 3)

    for i in range(my_columns):
        y  = y + vertical_block_size
        pygame.draw.line(aSurface, (255,255,255), (0,y), (my_height, y),3)


def redrawWindow(aSurface):
    global my_rows, my_width, my_height, my_columns
    aSurface.fill((48,10,36))
    drawGrid(my_width, my_height, my_rows, my_columns, aSurface)
    pygame.display.update()



def main():
    global my_width, my_height, my_rows, my_columns
    my_width = 900
    my_height = 900
    display_window = pygame.display.set_mode((my_width, my_height))
    my_rows = 30
    my_columns = 60

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