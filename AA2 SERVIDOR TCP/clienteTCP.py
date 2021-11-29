from socket import *

host = gethostname()
port = 3220

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host,port))


msg = input('Digite a msg: ')
cli.send(msg.encode())
data = cli.recv(1024)
print('Mensagem retornada do servidor: ',data.decode())
    
    
