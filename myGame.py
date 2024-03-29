# importing working libraries
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import random
#================================
# square objects are the building blocks of our snakw
class Cube(object):
    rows = 15
    columns = 15
    width = 900
    height = 900 
    def __init__(self, start_pos, x_move=1, y_move=0, color=(255,0,0)):
        self.position = start_pos
        self.x_move = 1 #1
        self.y_move = 0 # 0
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
            radius = 9
            circleMiddle = (i*dist_x+centre-radius,j*dist_y+8)
            circleMiddle2 = (i*dist_x + dist_x -radius*2, j*dist_y+8)
            pygame.draw.circle(aSurface, (45,45,120), circleMiddle, radius)
            pygame.draw.circle(aSurface, (45,45,120), circleMiddle2, radius)


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
            if (event.type == pygame.QUIT):
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
                elif (cube_element.y_move == 1 and cube_element.position[1] >= cube_element.columns - 1):
                    cube_element.position = (cube_element.position[0], 0)                    
                elif (cube_element.y_move == -1 and cube_element.position[1] <= 0):
                    cube_element.position = (cube_element.position[0],cube_element.columns-1)
                else:
                    cube_element.move(cube_element.x_move,cube_element.y_move)

    def draw(self, aSurface):
        for index, cube_element in enumerate(self.snake_body):
            if(index==0):
                cube_element.draw(aSurface, True)
            else:
                cube_element.draw(aSurface)

    def reset(self, pos):
        self.theHead = Cube(pos)
        self.snake_body = []
        self.snake_body.append(self.theHead)
        self.turns = {}
        self.x_move = 0
        self.y_move = 1


    def add_cube(self):
        snake_tail = self.snake_body[-1]

        dx, dy = snake_tail.x_move, snake_tail.y_move
 
        if(dx == 1 and dy == 0):
            self.snake_body.append(Cube((snake_tail.position[0]-1,snake_tail.position[1])))
        elif(dx == -1 and dy == 0):
            self.snake_body.append(Cube((snake_tail.position[0]+1,snake_tail.position[1])))
        elif(dx == 0 and dy == 1):
            self.snake_body.append(Cube((snake_tail.position[0],snake_tail.position[1]-1)))
        elif(dx == 0 and dy == -1):
            self.snake_body.append(Cube((snake_tail.position[0],snake_tail.position[1]+1)))
 
        self.snake_body[-1].x_move = dx
        self.snake_body[-1].y_move = dy


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


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
    global my_rows, my_width, my_height, my_columns, snake_instance, snack
    aSurface.fill((66,190,216))
    snake_instance.draw(aSurface)
    snack.draw(aSurface)
    drawGrid(my_width, my_height, my_rows, my_columns, aSurface)
    pygame.display.update()

def random_snack(rows,columns, aSnake):
    # global my_rows, my_columns
    positions = aSnake.snake_body

    while(True):
        x_position = random.randrange(rows)
        y_position = random.randrange(columns)

        if (len(list(filter(lambda x: x.position == (x_position,y_position) , positions))) > 0):
            x_position = random.randrange(rows)
            y_position = random.randrange(columns)

        else:
            break
        
    return (x_position,y_position)




def main():
    global my_width, my_height, my_rows, my_columns, snake_instance, snack
    my_width = 900
    my_height = 900
    my_rows = 15
    my_columns = 15
    display_window = pygame.display.set_mode((my_width, my_height))
    snake_head_color = (179,30,60)
    initial_position = (10,10)
    snake_instance = Snake(snake_head_color,initial_position)
    snack = Cube(random_snack(my_rows, my_columns, snake_instance), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
    # my_snake = Snake(snake_head_color, initial_position)
    flag = True
    my_clock = pygame.time.Clock()
    while(flag):
        pygame.time.delay(12)

        if (len(snake_instance.snake_body) <= 3):
            my_clock.tick(6)
        elif (3<len(snake_instance.snake_body) <= 6):
            my_clock.tick(12)
        elif (6<len(snake_instance.snake_body) <= 9):
            my_clock.tick(18)
        if (9<len(snake_instance.snake_body) <= 12):
            my_clock.tick(24)
        if (len(snake_instance.snake_body) > 12):
            my_clock.tick(30)
        
        
        snake_instance.move()
        if (snake_instance.snake_body[0].position == snack.position):
            snake_instance.add_cube()
            snack = Cube(random_snack(my_rows, my_columns, snake_instance), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))




    #collision
        for x in range(len(snake_instance.snake_body)):
            if snake_instance.snake_body[x].position in list(map(lambda z:z.position,snake_instance.snake_body[x+1:])):
                print("\nScore:    ", len(snake_instance.snake_body))
                message_box('\nYou Lost!', '\nPlay again...')
                snake_instance.reset((10,10))
                break
        redrawWindow(display_window)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main()