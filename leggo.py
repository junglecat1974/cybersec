import socket
s = socket.socket()
s.settimeout(2)
quarto = "254"
indirizzo = "10.0.3."+quarto
print(indirizzo)
s.connect((indirizzo,80))
risposta=s.recv(1024)
print(risposta.decode())

