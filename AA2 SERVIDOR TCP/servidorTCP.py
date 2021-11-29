from socket import *

host = gethostname()
port = 3220

serv = socket(AF_INET, SOCK_STREAM)#Defino que vai ser com IPV4 e o protocolo que é o TCP
serv.bind((host,port))
serv.listen(5) #define quantas pessoas podem acessar
print("Aguardando Conexao...")
while True:
    con, endereco = serv.accept()#Recebo a conexao
    print(f'Conexao recebida de {endereco}')
    msg = con.recv(1024)#recebo a mensagem da conexao
    print(f'Mensagem Recebida: {msg.decode()}')
    con.send(msg)#reenvio a msg
    con.close()

