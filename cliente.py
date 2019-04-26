# o modulo socket é a base para toda a comunicação Python em rede
from socket import *

# o nome ou IP do servidor. Se nome, uma consulta DNS será realizada. Porta do servidor.
serverName = 'localhost'
serverPort = 12000

# cria um socket cliente. o primeiro parametro indica que o endereço é o IPv4. o segundo indica que é UDP
# se a porta não é especificasda, o SO escolhe uma aleatória
clientSocket = socket(AF_INET, SOCK_DGRAM)

# input() espera uma entrada do teclado para formar a msg
message = input('Digite uma mensagem: ')

# envia a msg. .encode() transforma a string em bytes. as informações de ip de origem e porta também
# estão contidas na mensagem
clientSocket.sendto(message.encode(), (serverName, serverPort))

# recebe a msg. modifiedMessage guarda a msg e serverAddress guarda o ip e porta do servidor (não é necessário)
# buffer de 2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

messageDec = modifiedMessage.decode()
# imprime a msg recebida do servidor
print(messageDec)

# fecha o socket
clientSocket.close()
