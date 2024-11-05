import pygame
import socket
import pickle
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cliente Pygame")

x = WIDTH // 2
y = HEIGHT // 2
velocidade = 5

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_id = sys.argv[1] if len(sys.argv) > 1 else '1'  # ID do cliente (pode ser passado como argumento)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade
    if keys[pygame.K_RIGHT]:
        x += velocidade
    if keys[pygame.K_UP]:
        y -= velocidade
    if keys[pygame.K_DOWN]:
        y += velocidade

    data = pickle.dumps((client_id, x, y))
    client_socket.sendto(data, (UDP_IP, UDP_PORT))

    received_data, addr = client_socket.recvfrom(1024)
    positions = pickle.loads(received_data)
    
    screen.fill(WHITE)
    for id, (px, py) in positions.items():
        if client_id != id:
            pygame.draw.circle(screen, (255, 0, 0), (px, py), 20)
        else:
            pygame.draw.circle(screen, (0, 255, 0), (px, py), 20)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()