import pygame
import sys
from typing import *
screen_w = 700
screen_h = 500
square = screen_height
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.init()

class CircleGraph:
    def __init__(self, categories: Dict[Any, List[Any]], elements: List) -> None:
        """
        """
        self.cat = categories
        self.el = elements
        self.num_el = len(elements)
        self.num_cat = len(categories)

    def draw_graph(self, width, height) -> None:
        """
        """
        white = (255,255,255)
        pink = (255,200,200)
        darkBlue = (0,0,128)


        screen_w = width
        screen_h = height
        square = screen_height

        #degrees per slice
        dps = (math.pi * 2) / self.num_el

        start radius
        pygame.init()
        screen = pygame.display.set_mode((screen_w, screen_h))
        screen.fill(white)
        pygame.display.update()
        for k in range
        pygame.draw.arc(screen, color, (x,y,width,height), start_angle,
                        stop_angle, thickness)
