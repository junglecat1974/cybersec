#quindi...
import socket
server_socket = socket.socket()

host="127.0.0.1"
port = 7654
utenti={'admin':' è segreta'}

server_socket.bind((host,port))
server_socket.listen(1)

for i in range (2):#accetta piu connessioni


            conn,addr_p = server_socket.accept()#aspetta connessione
            print(f"Connected by {addr_p}\n")#tupla
            conn.sendall('nome'.encode())#conn.sendall(b'nome') al posto di encode

            #devo decodificare username ricevuto
            username=conn.recv(1024).decode()

            #print(f"il tuo usename {username}\n")
            
            conn.sendall(b'dammi password :')
            password=conn.recv(1024).decode()
            #print(f"la tua password {password}\n")
            if username=='admin':
                    if utenti[username]==password:
                        conn.sendall(str(utenti).encode())#manda dizionario utenti al client
                        print("Accesso riuscito")
                        
                    else:
                        conn.close()
                        print("Accesso negato")
                        continue
            else :

                utenti[username]=password#assegno password a utenti
                conn.close()

server_socket.close()


for u,p in utenti.items():
        print(f"Utente: {u}, Password: {p}")
#print(utenti)
