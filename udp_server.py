# import json
# import socket
# import time

# UDP_IP = "127.0.0.1"
# UDP_PORT = 5005

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.bind((UDP_IP, UDP_PORT))

# players_entered = {}
# addr_list = []

# while True:
#     data, addr = sock.recvfrom(1024)

#     obj = json.loads(data.decode('utf-8'))

#     player_id = obj['id']

#     # Verifica se o jogador já entrou no jogo
#     if player_id not in players_entered:
#         addr_list.append(addr)

#         # Marca o jogador como já tendo entrado no jogo
#         players_entered[player_id] = True
        
#         # Imprime a mensagem de entrada do jogador
#         print(f'Player ID #{player_id} enters the game')

#     for addr in addr_list:
#         sock.sendto(data, addr)

import socket
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

clients = {}  # Dicionário para armazenar as posições dos clientes

print("Servidor UDP iniciado")

while True:
    data, addr = server_socket.recvfrom(1024)
    received_data = pickle.loads(data)
    client_id, x, y = received_data

    clients[addr] = (client_id, x, y)

    # Enviar posições atualizadas para todos os clientes
    updated_positions = {cid: (cx, cy) for addr, (cid, cx, cy) in clients.items()}
    server_socket.sendto(pickle.dumps(updated_positions), addr)

server_socket.close()