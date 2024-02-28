import pygame
import random

pygame.init()

# Game settings
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pawsome Adventure")

dist = 10
frame_per_second = 30
clock = pygame.time.Clock()
score = 0

time = 60
pygame.time.set_timer(pygame.USEREVENT+1, 1000)

# Colors
white = (255, 255, 255)
orange = (255, 149, 0)

# Font
font = pygame.font.SysFont("comicsansms", 24, bold=True)
font_header = pygame.font.SysFont("comicsansms", 40, bold=True)

# Text
text = font_header.render("Pawsome Adventure", True, orange)
text_rec = text.get_rect()
text_rec.center = (width//2, height//2)

text_part2 = font.render("To start a new game, hit ENTER!", True, orange)
text_part2_rec = text_part2.get_rect()
text_part2_rec.center = (width//2, height//2 + 40)

text_final = font.render("Game is over!", True, orange)
text_final_rec = text_final.get_rect()
text_final_rec.center = (width//2, height//2)

text_final_part2 = font.render("To play a new game, hit ENTER!", True, orange)
text_final_rec_part2 = text_final_part2.get_rect()
text_final_rec_part2.center = (width//2, height//2 + 40)

# Images
cat_image = pygame.image.load("img/cat.png")
cat_rect = cat_image.get_rect()
cat_rect.center = (width//2, height//2)

mouse_image = pygame.image.load("img/mouse.png")
mouse_rect = mouse_image.get_rect()
mouse_rect.center = (width//2, height - 50)

bg = pygame.image.load("img/background.jpg")
bg = pygame.transform.scale(bg, (width, height))

start_menu = True
if start_menu:
    screen.blit(bg, (0, 0))
    screen.blit(text, text_rec)
    screen.blit(text_part2, text_part2_rec)
    pygame.display.update()

    while start_menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                start_menu = False
            elif event.type == pygame.QUIT:
                start_menu = False
                lets_continue = False


lets_continue = True
start_time = pygame.time.get_ticks()

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cat_rect.center = event.pos
        if event.type == pygame.USEREVENT+1:
            time -= 1

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and cat_rect.top > 50:
        cat_rect.y -= dist
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and cat_rect.bottom < height:
        cat_rect.y += dist
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and cat_rect.left > 25:
        cat_rect.x -= dist
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and cat_rect.right < width:
        cat_rect.x += dist

    if cat_rect.colliderect(mouse_rect):
        cat_rect.center = (random.randint(25, width - 25), random.randint(50, height - 25))
        mouse_rect.center = (random.randint(25, width - 25), random.randint(50, height - 25))
        score += 1

    text_score = font.render(f"Score: {score}", True, orange)
    text_score_rec = text_score.get_rect()
    text_score_rec.center = (75, 25)

    time_text = font.render(f"Time: {time} s", True, orange)
    time_text_rec = time_text.get_rect()
    time_text_rec.center = (width - 90, 25)

    screen.blit(bg, (0, 0))

    screen.blit(cat_image, cat_rect)
    screen.blit(mouse_image, mouse_rect)

    screen.blit(text_score, text_score_rec)
    screen.blit(time_text, time_text_rec)

    if time == 0:
        pygame.time.set_timer(pygame.USEREVENT + 1, 0)
        screen.blit(text_final, text_final_rec)
        screen.blit(text_final_part2, text_final_rec_part2)
        pygame.display.update()

        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    time = 5
                    cat_rect.y = height//2
                    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
                    pause = False

                elif event.type == pygame.QUIT:
                    pause = False
                    lets_continue = False

    pygame.display.update()

    clock.tick(frame_per_second)

pygame.quit()