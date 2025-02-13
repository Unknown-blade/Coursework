import pytmx
from pytmx import load_pygame
import math
from queue import PriorityQueue
from Importfunctions import *


pygame.display.set_mode((1280,720))
tmx_map = load_pygame('Maps\WIP.tmx')
mainarray = tmx_map.get_layer_by_name("Main")
maindata = mainarray.data


class Node():
    def __init__(self,row,col,width):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.neighbours = []
        self.width = width

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def modifytilearray(data):
    for n, i in enumerate(data):
        list2 = i
        for n2, x in enumerate(list2):
            if x!= 0:
                 list2[n2] = 1
        data[n] = list2
    return data
               
def get_location(player_x,player_y,enemy_x,enemy_y,data):
    playercol = int(player_x/64)
    playerrow = int(player_y/64) #player will be noted in array as 3
    enemycol = int(enemy_x/64)
    enemyrow = int(enemy_y/64) #enemy will be noted in array as 4    
    data[playerrow][playercol] = 3
    data[enemyrow][enemycol] = 4
    return data,playerrow,playercol,enemyrow,enemycol


class Pathfinding():
    def __init__(self,data,startnodex,startnodey,endnodex,endnodey):
        self.data = data

px = 180
py = 1444
ex = 940.000000
ey = 1280.00000
data = modifytilearray(maindata)
data,endnodex,endnodey,startnodex,startnodey = get_location(px,py,ex,ey,data)
print(data)
#Pathfinding(data,startnodex,startnodey,endnodex,endnodey)