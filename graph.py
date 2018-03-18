import pygame
import sys
import math
from typing import *


class CircleGraph:
    def __init__(self, categories: Dict[Any, List[Any]], elements: List) -> None:
        """
        """
        self.cat = categories
        self.el = elements
        self.num_el = len(elements)
        self.num_cat = len(categories)

    def draw_graph(self) -> None:
        """
        """
        #different colors we will use:
        white = (255,255,255)
        pink = (255,200,200)
        darkBlue = (0,0,128)
        thickness = 10
        #screen measurements and measurement of square that circle will be w/in
        screen_w = (self.num_cat * thickness * 2) + 10
        screen_h = (self.num_cat * thickness * 2) + 10
        square = screen_w / 2
        #inital circle radius for first ring
        ICR = (len(self.el) * 4) / (2 * math.pi)

        #degrees per slice
        dps = (math.pi * 2) / self.num_el


        #actual window
        pygame.init()
        screen = pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption("hello world")
        clock = pygame.time.Clock()
        screen.fill(white)
        pygame.display.update()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

        enclosingBox = square/2 - ICR
        #each ring
        for w in range(len(self.cat)):
            degree = 0

            #each gene in the ring
            for k in range(len(self.num_el)):
                if self.num_el[k] in self.cat[w]:
                    color = darkBlue
                else:
                    color = pink

                pygame.draw.arc(screen, color, (enclosingBox,enclosingBox,square,square), dps*k,
                        dps * (k + 1), thickness)
                enclosingBox = enclosingBox - 10






bob = CircleGraph({"bob":3},[0])
bob.draw_graph(300,300)
