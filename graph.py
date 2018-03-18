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

    def draw_graph(self, width, height) -> None:
        """
        """
        #different colors we will use:
        white = (255,255,255)
        pink = (255,200,200)
        darkBlue = (0,0,128)

        #screen measurements and measurement of square that circle will be w/in
        screen_w = width
        screen_h = height
        square = screen_h

        #degrees per slice
        dps = (math.pi * 2) / self.num_el

        clock = pygame.time.Clock()

        pygame.init()
        screen = pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption("hello world")
        screen.fill(white)
        pygame.display.update()
        screen.fill(white)
        pygame.display.flip()
        
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        # for w in range(len(self.cat)):
        #     for k in range(len(self.num_el)):
        #         if self.num_el[k] in self.cat[w]:
        #             color = darkBlue
        #         else:
        #             color = pink
        #
        #         pygame.draw.arc(screen, color, (0,0,square,square), dps*k,
        #                 (dps*k) +1, thickness)
bob = CircleGraph({"bob":3},[0])
bob.draw_graph(300,300)
