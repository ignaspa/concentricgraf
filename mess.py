import pygame
import sys
import math
from typing import *


class CircleGraph:
    def __init__(self, categories: Dict[Any, List[Any]], elements: List)->None:
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
        black = (0,0,0)
        thickness = 10
        #screen measurements and measurement of square that circle will be w/in
        screen_w = (self.num_cat * thickness * 2) + 10
        screen_h = (self.num_cat * thickness * 2) + 10
        square = screen_w
        #inital circle radius for first ring
        print('len:self.el: ' + str(len(self.el)))
        ICR = (len(self.el) * 4) / (2 * math.pi)
        print('ICR: ' + str(ICR))

        #degrees per slice
        dps = (math.pi * 2) / (self.num_el + 1)


        #actual window
        pygame.init()
        screen = pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption("Circle Graph!")
        clock = pygame.time.Clock()
        screen.fill(white)


        # pygame.draw.arc(screen, pink,(0,0,200,200),
        #                 math.pi/2, math.pi, thickness)
        # pygame.draw.arc(screen, darkBlue,(0,0,200,200),
        #                 math.pi, 3*math.pi/2, thickness)

        #distance from center
        min = ICR
        #enclosing box coordinates for x and y
        eb = square/2 - min
        #each ring
        for w in self.cat:

            #each gene in the ring
            for k in range(len(self.el)):
                print(w)
                print(k)
                if self.el[k] in self.cat[w]:
                    color = darkBlue
                else:
                    color = pink
                #draw slice
                print('Box width:' + str(min*2))
                print('dps+k:' + str(dps*k))
                print('eb:' + str(eb))
                pygame.draw.arc(screen, color,
                                (eb,eb,min*2,min*2),
                                dps*k, (dps * (k + 1) - 1), thickness)
                #draw slice border
                pygame.draw.arc(screen, black,
                                (eb,eb,min*2,min*2),
                                (dps * (k + 1)) - 1, (dps * (k + 1)), thickness)
            min = min + thickness
            eb = eb - thickness

        pygame.display.update()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()








bob = CircleGraph({"bob":[3], "tom":[7, 3]},[3,8])
bob.draw_graph()