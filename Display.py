import sys
import pygame
from Stack import Stack

X_MAX = 500
Y_MAX = 300
RADIUS_STEP = 5


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
                if 48 <= event.key <= 57: # 48: 0, 57: 9
                    print("Added to stack: " + str(event.unicode))
                    self.stack.append(event.unicode)
                    self.show_message("Added to stack: ", event.unicode)
                elif event.key == 8: #backspace
                    element = self.stack.pop()
                    self.show_message("Taken from stack: ", element)
                pygame.display.update()
                pygame.event.clear()

    def show_message(self, comment, event_key):
        print(comment)
        event_key = str(event_key)
        black = (0, 0, 0)
        myFont = pygame.font.SysFont("Times New Roman", 18)
        randNumLabel = myFont.render(comment, False, black)
        diceDisplay = myFont.render(event_key, False, black)
        self.screen.blit(randNumLabel, (100, 20))
        self.screen.blit(diceDisplay, (100, 50))














