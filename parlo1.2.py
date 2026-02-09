import socket 




s = socket.socket()

# indirizzo 10.0.4.254
indirizzo = '127.0.0.1' 
porta = 7654
s.connect((indirizzo,porta))
prompt=s.recv(1024)#prende prompt dal server
print(prompt.decode())
username=input(prompt.decode())#codifica a stringa
s.sendall(username.encode())#da stringa a byte
prompt=s.recv(1024)#secondo prompt
password=input(prompt.decode())
s.sendall(password.encode())


if username=='admin':
   prompt=s.recv(1024)#riceve lista utenti se è admin
   print(prompt.decode())
   


s.close()