import socket
import sys
import random
import threading
import time

#this will append roles in wroles.py file upon server startup. this is to ensure that there will be similar roles across players
wildcard = ['fool', 'hunter']
bad = ['wolftrickster', 'wolf', 'alpha']
roles = ['bad', 'villager', 'doctor', 'seer', 'wildcard']

#server states
p1_state = ['alive']
p2_state = ['alive']
p3_state = ['alive']
p4_state = ['alive']
p5_state = ['alive']

HOST = '127.0.0.1'
PORT = 8888
PORT2 = 5556

challenger = 1

#TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f'[*] Listening on {HOST}:{PORT}')

#sends roles to clients
rolesend = ''
for n in range(1, 6):
    role = random.choice(roles)
    roles.remove(role)
    if role == 'bad':
        role = random.choice(bad)
        bad.remove(role)
        rolesend = rolesend + role + ' ' 
    elif role == 'wildcard':
        role = random.choice(wildcard)
        wildcard.remove(role)
        rolesend = rolesend + role + ' ' 
    else:
        rolesend = rolesend + role + ' '    # 1: villager,
print(rolesend)

#connects players
while challenger < 3:
    try:
        client_socket, address = server_socket.accept()
    except KeyboardInterrupt or ConnectionResetError or BrokenPipeError:
        print('\nClosing Server Socket...')
        server_socket.close()
        sys.exit()    
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')   
    request = client_socket.recv(1024)
    chal_str = str(challenger)
    chal_bytes = chal_str.encode()
    challenger += 1
    client_socket.send(chal_bytes)
    x = request.decode("utf-8")
    print(x)  
    client_socket.close()

server_socket.close()
print('Initializing...')
time.sleep(2)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT2))
tcp_socket.listen(5)
print('[*] Game commenced. Press Ctrl-C to Exit')
clients = set()
clients_lock = threading.Lock()

def handle_client(tcp_socket):
    import vote
    svrheartbeat = 'sync'
    with tcp_socket as sock:
        while True:
            com = sock.recv(1024)
            if not com:
                break
            else:
                with clients_lock:
                    if '#1' in com.decode('utf-8'):
                        vote.p1 = com.decode('utf-8')
                        vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                        print(vote.players)
                    if '#2' in com.decode('utf-8'):
                        vote.p2 = com.decode('utf-8')
                        vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                        print(vote.players)
                    if '#3' in com.decode('utf-8'):
                        vote.p3 = com.decode('utf-8')
                        vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                        print(vote.players)
                    if '#4' in com.decode('utf-8'):
                        vote.p4 = com.decode('utf-8')
                        vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                        print(vote.players)
                    if '#5' in com.decode('utf-8'):
                        vote.p5 = com.decode('utf-8')
                        vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                        print(vote.players)
                    if com.decode('utf-8') == 'ready':
                        vote.readycount += 1
                        print(vote.readycount)
                        if vote.readycount == 2:
                            vote.players = vote.p1 + vote.p2 + vote.p3 + vote.p4 + vote.p5
                            print(vote.players)
                            svrheartbeat = 'endmenu' + vote.players
                            for c in clients:
                                c.send(svrheartbeat.encode('utf-8')) 
                                time.sleep(0.02)
                            vote.readycount += 1
                            svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'sync':
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8')) 
                            time.sleep(0.02)
                    if com.decode('utf-8') == 'day':
                        svrheartbeat = 'day'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                    if com.decode('utf-8') == 'night':
                        svrheartbeat = 'night'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        #time.sleep(5)
                        #for c in clients:
                        #    c.send(b'night2')
                        #time.sleep(5)
                        #for c in clients:
                        #    c.send(b'night3')
                    if com.decode('utf-8') == 'p1dead':
                        svrheartbeat = 'p1dead'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p2dead':
                        svrheartbeat = 'p2dead'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p3dead':
                        svrheartbeat = 'p3dead'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p4dead':
                        svrheartbeat = 'p4dead'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p5dead':
                        svrheartbeat = 'p5dead'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p1alive':
                        svrheartbeat = 'p1alive'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p2alive':
                        svrheartbeat = 'p2alive'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p3alive':
                        svrheartbeat = 'p3alive'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p4alive':
                        svrheartbeat = 'p4alive'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p5alive':
                        svrheartbeat = 'p5alive'
                        for c in clients:
                            c.send(svrheartbeat.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p1tricked':
                        trick = 'p1tricked'
                        for c in clients:
                            c.send(trick.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p2tricked':
                        trick = 'p2tricked'
                        for c in clients:
                            c.send(trick.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p3tricked':
                        trick = 'p3tricked'
                        for c in clients:
                            c.send(trick.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p4tricked':
                        trick = 'p4tricked'
                        for c in clients:
                            c.send(trick.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p5tricked':
                        trick = 'p5tricked'
                        for c in clients:
                            c.send(trick.encode('utf-8'))
                            time.sleep(0.02)
                        svrheartbeat = 'sync'
                    if com.decode('utf-8') == 'p1voted':
                        vote.votes[0] += 1
                        print(vote.votes)
                    if com.decode('utf-8') == 'p2voted':
                        vote.votes[1] += 1
                        print(vote.votes)
                    if com.decode('utf-8') == 'p3voted':
                        vote.votes[2] += 1
                        print(vote.votes)
                    if com.decode('utf-8') == 'p4voted':
                        vote.votes[3] += 1
                        print(vote.votes)
                    if com.decode('utf-8') == 'p5voted':
                        vote.votes[4] += 1
                        print(vote.votes)
                    if com.decode('utf-8') == 'votestart':
                        svrheartbeat = 'sync'
                        if vote.votes.count(max(vote.votes)) == 1:
                            voteres = 'p'+str(vote.votes.index(max(vote.votes))+1)+'lynch'
                            for c in clients:
                                c.send(voteres.encode('utf-8'))
                                time.sleep(0.02)
                            vote.votes = [0,0,0,0,0]
                        #else:
                        #    voteres = 'votetie'
                        #    for c in clients:
                        #        c.send(voteres.encode('utf-8'))
                        #        print('sent', voteres)

while True:
    try:
        client, tcp_address = tcp_socket.accept()        
    except KeyboardInterrupt:                        
        print("\nClosing Server Socket...")
        tcp_socket.close()
        sys.exit()
    client.send(rolesend.encode('utf-8'))
    print(f'[*] Accepted connection from {tcp_address[0]}:{tcp_address[1]}')
    with clients_lock:
        clients.add(client)
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
