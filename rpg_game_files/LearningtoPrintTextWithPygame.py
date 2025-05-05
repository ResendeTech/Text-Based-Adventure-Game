import sys, time
import random
import sys, pygame


pygame.init()
x = 720
y = 480
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((x, y), flags)
clock = pygame.time.Clock()
running = True

text_font = pygame.font.SysFont(None, 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    # for i in text[0]:
    #     print("skbiidi")
    #for (i = 0)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_text("Skibidi dop dop", text_font, (0, 0, 0), x-(x*0.99), y-(y*0.99))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()