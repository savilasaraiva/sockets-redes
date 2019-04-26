from socket import *
from datetime import datetime
from time import time
from encodings import utf_8

print("Uhuu! Deu certo!")

servidor = 'localhost'
porta = 12000
cliente_socket = socket(AF_INET, SOCK_DGRAM)
ultimo_ping = 10
count = 1
cliente_socket.settimeout(1)

while count <= ultimo_ping:
    mensagem = 'olá'
    inicio = datetime.now()
    cliente_socket.sendto(mensagem.encode(), (servidor, porta))
    final = datetime.now()

    try:
        RTT = final - inicio
        print("Ping ", count, " hora: ",
              inicio.strftime('%H:%M:%S'), "rtt: ", RTT)
        enderecoC = cliente_socket.recvfrom(1024)
    except timeout:
        print("Não foi dessa vez... que pena :(")
    count = count + 1
