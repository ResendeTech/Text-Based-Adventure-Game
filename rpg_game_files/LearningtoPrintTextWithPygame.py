import sys, time
import random
import sys, pygame
from TextDB import Texts

pygame.init()
x = 720
y = 480
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((x, y), flags)
clock = pygame.time.Clock()
running = True
delay = 25
counter = 0
speed = 6
current_message = 0
Text = Texts[current_message]
displayed_messages = []
text_font = pygame.font.SysFont(None, 30)
snip = text_font.render("", True, "Black")


# My attempt :(
def draw_text(text, font, text_col, x, y):
    i = len(text)
    n = 1
    extra_x = 10
    first_run = True
    while i >= 0:
        if i == 0:
            break
        if first_run == True:
            char1 = font.render(text[0], True, text_col)
            screen.blit(char1, (x, y))
            first_run = False
            last_char_time = pygame.time.get_ticks()
            print("last_time:", last_char_time)
        else:
            current_time = pygame.time.get_ticks()
            print("current_time:", current_time)
            if current_time - last_char_time > delay:
                chars = font.render(text[n], True, text_col)
                screen.blit(chars, (x + extra_x, y))
                n += 1

        extra_x += 10
        i -= 1

def draw_texto(text):
    y_offset = y-(y*0.99)
    line_height = 30
    if displayed_messages:
        old_msg = displayed_messages
        for old_msg in displayed_messages:
            complete_text = text_font.render(old_msg, True, "Black")
            y_offset -= line_height
            screen.blit(complete_text, (x-(x*0.99), y_offset))
            

    snip = text_font.render(text[0:counter//speed], True, "Black")
    screen.blit(snip, (x-(x*0.99), y_offset)) 

    
while running:
    screen.fill((255, 255, 255))
    clock.tick(60)

    if counter < speed * len(Texts[current_message]):
        counter += 1
    elif counter >= speed * len(Texts[current_message]):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and current_message < len(Text):
                displayed_messages.append(Texts[current_message])
                current_message += 1
                done = False
                Text = Texts[current_message]
                counter = 0


    draw_texto(Texts[current_message])
    #draw_texto(text1)

    # draw_text("skibidi dop dop", text_font, (0, 0, 0), x-(x*0.99), y-(y*0.99))
    pygame.display.flip()

pygame.quit()