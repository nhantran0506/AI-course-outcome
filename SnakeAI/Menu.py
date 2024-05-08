import pygame
from Settings import *
import sys

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_size = self.game.SIZE/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -150
        self.title_size = 50
        self.option_size = 28

        # Define button dimensions and padding
        self.button_width = 200
        self.button_height = 50
        self.button_padding = 20

        self.button_spacing = 20

    def draw_cursor(self):
        self.game.draw_text(
            '', size=20,
            x=self.cursor_rect.x, y=self.cursor_rect.y,
            color=MENU_COLOR
        )

    def draw_button(self, text, x, y, color):
        # Draw button rectangle
        pygame.draw.rect(self.game.display, color, (x, y, self.button_width, self.button_height))

        # Render text
        font = pygame.font.Font(None, self.option_size)
        text_surface = font.render(text, True, (0, 0, 0))  # Black text

        # Calculate text position (center of the button)
        text_x = x + (self.button_width - text_surface.get_width()) / 2
        text_y = y + (self.button_height - text_surface.get_height()) / 2

        # Draw text on the button
        self.game.display.blit(text_surface, (text_x, text_y))

    def blit_menu(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BFS'

        self.cursorBFS = MENU_COLOR
        self.cursorDFS = WHITE
        self.cursorASTAR = WHITE        
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorGBF = WHITE

        # Define button positions
        self.BFSx, self.BFSy = self.mid_size - self.button_width / 2, self.mid_size - 50
        self.DFSx, self.DFSy = self.mid_size - self.button_width / 2, self.BFSy + self.button_height + self.button_spacing
        self.ASTARx, self.ASTARy = self.mid_size - self.button_width / 2, self.DFSy + self.button_height + self.button_spacing
        self.GREEDYx, self.GREEDYy = self.mid_size - self.button_width / 2, self.ASTARy + self.button_height + self.button_spacing                
        self.UCSx, self.UCSy = self.mid_size - self.button_width / 2, self.GREEDYy + self.button_height + self.button_spacing
        self.GBFx, self.GBFy = self.mid_size - self.button_width / 2, self.UCSy + self.button_height + self.button_spacing
        self.cursor_rect.midtop = (self.BFSx + self.offset, self.BFSy)

    def change_cursor_color(self):
        self.clear_cursor_color()
        if self.state == 'BFS':
            self.cursorBFS = MENU_COLOR
        elif self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'ASTAR':
            self.cursorASTAR = MENU_COLOR
        elif self.state == 'GREEDY':
            self.cursorGREEDY = MENU_COLOR      
        elif self.state == 'UCS':  
            self.cursorUCS = MENU_COLOR
        elif self.state == 'GBF':  
            self.cursorGBF = MENU_COLOR

    def clear_cursor_color(self):
        self.cursorBFS = WHITE
        self.cursorDFS = WHITE
        self.cursorASTAR = WHITE
        self.cursorGREEDY = WHITE        
        self.cursorUCS = WHITE
        self.cursorGBF = WHITE

    def display(self):        
        self.run_display = True

        # Load and scale the background image
        background_image = pygame.image.load('./assets/snake-img.jpg')
        background_image = pygame.transform.scale(background_image, (self.game.SIZE, self.game.SIZE))

        while self.run_display:
            self.game.event_handler()
            self.check_input()

            self.game.display.blit(background_image, (0, 0))

            self.game.draw_text(
                'Snake Game AI', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS),
                color=TITLE_COLOR
            )

            # Draw buttons
            self.draw_button('BFS', self.BFSx, self.BFSy, self.cursorBFS)
            self.draw_button('DFS', self.DFSx, self.DFSy, self.cursorDFS)
            self.draw_button('AStar', self.ASTARx, self.ASTARy, self.cursorASTAR)
            self.draw_button('Greedy', self.GREEDYx, self.GREEDYy, self.cursorGREEDY)
            self.draw_button('UCS', self.UCSx, self.UCSy, self.cursorUCS)    
            self.draw_button('GBF', self.GBFx, self.GBFy, self.cursorGBF)           

            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()

    def check_input(self):
        self.move_cursor()

        if self.game.START:
            if self.state == 'GA':  # go to genetic algorith options
                self.game.curr_menu = self.game.GA
            else:
                self.game.playing = True
                self.run_display = False

    def move_cursor(self):
        if self.game.DOWNKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'
            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'
            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.ASTARy)
                self.state = 'GREEDY'
            elif self.state == 'GREEDY':  
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'
            elif self.state == 'UCS':  
                self.cursor_rect.midtop = (
                    self.GBFx + self.offset, self.GBFy)
                self.state = 'GBF'
            

        if self.game.UPKEY:
            if self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'
            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'   
            elif self.state == 'GREEDY': 
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.ASTARy)
                self.state = 'ASTAR'         
            elif self.state == 'UCS':  
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'  
            elif self.state == 'GBF':  
                self.cursor_rect.midtop = (
                    self.GBFx + self.offset, self.UCSy)
                self.state = 'UCS'             



class button():
    def __init__(self, x, y, text, game):
        self.x = x
        self.y = y
        self.text = text
        self.game = game
        self.font = pygame.font.Font(game.font_name, 30)
        self.clicked = False    


class TextBox:
    def __init__(self, x, y, game):
        self.font = pygame.font.Font(game.font_name, 20)
        self.input_rect = pygame.Rect(x, y, TXT_WIDTH, TXT_HEIGHT)
        self.input = ''
        self.game = game
        self.active = False

    def draw_input(self):
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.input_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.active = True

        elif pygame.mouse.get_pressed()[0] == 1:
            self.active = False

        if self.active:
            color = TXT_ACTIVE
        else:
            color = TXT_PASSIVE

        pygame.draw.rect(self.game.display, color, self.input_rect, 2)
        text_surface = self.font.render(self.input, False, WHITE)
        self.game.display.blit(
            text_surface, (self.input_rect.x + 15, self.input_rect.y + 1)) 