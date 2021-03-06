import socket
import time
import sys

port = 9898
host = ""

x = int(raw_input("Enter number of files: "))

filenames = []

for i in range(x):
    filename = raw_input("Enter file to get: ")
    filenames.append(filename)

start = time.time()
for filename in filenames:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect((host, port))
    s.send(filename)

    filen = filename.split('/')
    p = len(filen) - 1

    with open(filen[p], 'wb') as f:
        print 'File opened'
        while True:
            print('receiving data...')
            data = s.recv(1024)
            if not data:
                print 'Error : No such file %s exists' %filen[p]
                s.close()
                sys.exit()
            f.write(data)
            if len(data) < 1024:
                break

    f.close()

    print('Successfully got the file')
    s.close()

    print('Connection closed')

print('Time take: ' + str(time.time() - start))
