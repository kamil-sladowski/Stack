import sys
import pygame
from Stack import Stack

X_MAX = 800
Y_MAX = 300
RADIUS_STEP = 10


class Display:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((X_MAX, Y_MAX))
        self.stack = Stack()

    def check_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def play(self):

        while True:
            event = pygame.event.wait()
            self.check_quit(event)
            if event.type == pygame.KEYDOWN:
                print(event)
                self.screen.fill((255, 255, 255))
                if 48 <= event.key <= 57 or 65 <= event.key <= 90 or 97 <= event.key <= 122: # ascii codes
                    print("Added to stack: " + str(event.unicode))
                    self.stack.append(event.unicode)
                    self.show_message("Added to stack: ", event.unicode)
                elif event.key == 8: #backspace
                    element = self.stack.pop()
                    self.show_message("Taken from stack: ", element)
                else:
                    self.show_message("Key not allowed: ", event.unicode)
            self.draw_stack(self.stack.stack)
            pygame.display.update()
            pygame.event.clear()

    def draw_stack(self, stack_list):
        counter = 0
        y = 100
        margin = 110
        for element in stack_list:
            self.draw_in((2 * RADIUS_STEP * counter + margin, y), element)
            counter += 1

    def draw_in(self, pos, num):
        color = self.stack.get_color(num)
        pygame.draw.circle(self.screen, color, pos, RADIUS_STEP, 0)

    def show_message(self, comment, event_key):
        print(comment)
        event_key = str(event_key)
        black = (0, 0, 0)
        myFont = pygame.font.SysFont("Times New Roman", 18)
        randNumLabel = myFont.render(comment, False, black)
        diceDisplay = myFont.render(event_key, False, black)
        self.screen.blit(randNumLabel, (100, 20))
        self.screen.blit(diceDisplay, (100, 50))














