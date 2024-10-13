import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Play the game")
icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

target_dx = 3  # Скорость по оси X
target_dy = 3  # Скорость по оси Y

clock = pygame.time.Clock()
FPS = 60  # Количество кадров в секунду

pygame.font.init()
font_size = 30
font = pygame.font.SysFont(None, font_size)

hit_count = 0

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hit_count += 1  # Увеличение счетчика
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    target_x += target_dx
    target_y += target_dy

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_dx = -target_dx
        # Изменение цвета фона при столкновении с вертикальной границей
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_dy = -target_dy
        # Изменение цвета фона при столкновении с горизонтальной границей
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))
    # Подготовка текста счетчика
    hit_text = font.render(f"bull's-eye: {hit_count}", True, (255, 255, 255))
    # Отображение текста в верхнем левом углу
    screen.blit(hit_text, (10, 10))
    pygame.display.update()
pygame.quit()
