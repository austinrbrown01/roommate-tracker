import pygame
from pygame import display
import pygame.gfxdraw
import sys
import dynamoHelper
 
pygame.init()
#screen = pygame.display.set_mode((480, 320), pygame.FULLSCREEN)
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption('Roommate Tracker')
ddbHelper = dynamoHelper.dynamoDbHelper()
# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((142, 176, 232))
# Display some text
titleFont = pygame.font.Font(None, 36)
subtitleFont = pygame.font.Font(None, 25)
titleText = titleFont.render("Austin's Roommate Tracking System", 1, (10, 10, 10))
titleTextPos = titleText.get_rect()
titleTextPos.centerx = background.get_rect().centerx
titleTextPos.move_ip(0,5)
subtitle1Text = subtitleFont.render("Press your name to toggle here/away, view live data at", 1, (10,10,10))
subtitle1TextPos = subtitle1Text.get_rect()
subtitle1TextPos.centerx = background.get_rect().centerx
subtitle1TextPos.move_ip(0,40)
subtitle2Text = subtitleFont.render("roommates.austinbrown.dev/tracker", 1, (10,10,10))
subtitle2TextPos = subtitle2Text.get_rect()
subtitle2TextPos.centerx = background.get_rect().centerx
subtitle2TextPos.move_ip(0,60)
subtitle3Text = subtitleFont.render("Tip: briefly hold your finger on the screen while tapping", 1, (10,10,10))
subtitle3TextPos = subtitle3Text.get_rect()
subtitle3TextPos.centerx = background.get_rect().centerx
subtitle3TextPos.move_ip(0,280)
background.blit(titleText, titleTextPos)
background.blit(subtitle1Text, subtitle1TextPos)
background.blit(subtitle2Text, subtitle2TextPos)
background.blit(subtitle3Text, subtitle3TextPos)
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()
screen.blit(background, (0, 0))
pygame.display.flip()
class Button(pygame.sprite.Sprite):
    def __init__(self, position, name, size,
        fgcolor,
        bgcolor,
        #hover_colors="red on green",
        style=1,
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.name = name
        self.command = command
        self.fg = fgcolor
        self.bg = bgcolor
        self.text = self.name + " - HOME"
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        self.ddbHelper = dynamoHelper.dynamoDbHelper()
        self.is_here = True
        buttons.add(self)
 
    def render(self):
        self.text_render = self.font.render(self.text, True, self.fg)
        #self.text_render = self.font.render(self.text, True, (0,0,0))
        self.image = self.text_render
 
    def update(self):
        #self.fg = (0,0,0)
        #self.bg = (0,255,0)
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        #self.hover()
        self.click()
 
    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  
 
    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.w , self.h), self.borderc)

    def update_color(self):
        if (self.is_here):
            self.bg = (0,255,0)
        else:
            self.bg = (255,255,0)
        self.render()

    
    def update_text(self):
        if (self.is_here):
            self.text = self.name + " - HOME"
        else:
            self.text = self.name + " - AWAY"
        self.render()
 
    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Execunting code for button '" + self.text + "'")
                self.command(self)
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1
 


def toggle_here(button):
    print("toggling here for " + button.name + "'s button.")
    button.is_here = not (button.is_here)
    button.update_color()
    button.update_text()
    if (button.is_here):
        ddbHelper.update_roommate_status(button.name, 'HOME')
    else:
        ddbHelper.update_roommate_status(button.name, 'AWAY')
    
def buttons_def():
    # b0 = Button((10, 10), "Click me now", 55, (0,0,0), (0,255,0),
    #     command=on_click)
    # b1 = Button((10, 100), "Run the program", 40, (0,0,0), (0,255,0), command=on_run)
 
    # b2 = Button((10, 170), "Save this file", 36, (0,0,0), (0,255,0),
    #      style=2, borderc=(255,255,0),
    #     command=on_save)
    austin_button = Button((0, 95), "Austin", 33, (0,0,0), (0,255,0),
        command=toggle_here)
    zach_button = Button((0, 95), "Zach", 33, (0,0,0), (0,255,0),
        command=toggle_here)
    alex_button = Button((0, 210), "Alex", 33, (0,0,0), (0,255,0),
        command=toggle_here)
    jack_button = Button((0, 210), "Jack", 33, (0,0,0), (0,255,0),
        command=toggle_here)

    austinpos = austin_button.rect
    austinpos.centerx = background.get_rect().centerx / 2
    austin_button.x = austinpos.x
    austin_button.y = austinpos.y

    zachpos = zach_button.rect
    zachpos.centerx = background.get_rect().centerx * 1.5
    zach_button.x = zachpos.x
    zach_button.y = zachpos.y

    jackpos = jack_button.rect
    jackpos.centerx = background.get_rect().centerx / 2
    jack_button.x = jackpos.x
    jack_button.y = jack_button.y

    alexpos = alex_button.rect
    alexpos.centerx = background.get_rect().centerx * 1.5
    alex_button.x = alexpos.x
    alex_button.y = alexpos.y
    
 
# ======================= this code is just for example, start the program from the main file
# in the main folder, I mean, you can also use this file only, but I prefer from the main file
# 29.8.2021
 
if __name__ == '__main__':
    pygame.init()
    game_on = 0
    def loop():
        # BUTTONS ISTANCES
        game_on = 1
        buttons_def()
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_on = 0
            if game_on:
                buttons.update()
                buttons.draw(screen)
            else:
                pygame.quit()
                sys.exit()
            buttons.draw(screen)
            clock.tick(60)
            pygame.display.update()
        pygame.quit()
    loop()