import socket               
from phe import paillier
import pickle

host = socket.gethostname() 
port = 12002           

def compareHelper(files):
    dataFromClient = []
    for file in files:
        dataFromClient.append(dataLoad(file))
    print('[+] Loading Finish')
    res = []
    for i in range(len(dataFromClient[0])):
        for j in range(len(dataFromClient[1])):
            print(dataFromClient[0][i],dataFromClient[1][j])
            res.append([i,j,dataFromClient[0][i]-dataFromClient[1][j]])
    resFile = open('pkls/compareRes.pkl','wb')
    pickle.dump(res,resFile)
    resFile.close()
    print('[+] Begin Sending')
    msg = socketConn('Decrypt')
    return msg

def socketConn(msg):
    ss = socket.socket()             
    ss.connect((host, 12001))
    ss.send(msg.encode())
    recvData = ss.recv(1024)
    ss.close()
    return recvData

def dataLoad(file):
    f = open(file,'rb')
    data = pickle.load(f)
    return data

if __name__ == "__main__":
    s = socket.socket()         
    s.bind((host, port))        
    s.listen(5)
    files = []
    clients = []
    while True:
        c,addr = s.accept()
        clients.append(c)     
        print('连接地址：', addr)
        files.append(c.recv(1024).decode())
        if len(files) == 2:
            msg = compareHelper(files)
            files = []
            for i in clients:
                i.send(msg.encode())
                i.close()
            clients = []      