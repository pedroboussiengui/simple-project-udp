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
