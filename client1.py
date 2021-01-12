import socket               
import pickle
from phe import paillier

Host = socket.gethostname() 
KeyManagePort = 12001
CompareServerPort = 12002

def socketConn(host, port, msg):
    s = socket.socket()             
    s.connect((host, port))
    s.send(msg.encode())
    recvData = s.recv(1024)
    s.close()
    return recvData

def createEncryptedPickle(data):
    dataFile = open('pkls/dataFromClient1.pkl','wb')
    pickle.dump(data, dataFile)
    dataFile.close()

def data2ascii(data):
    dataReturn = []
    for dt in data:
        num = ''
        for i in dt:
            num += str(ord(i))
        dataReturn.append(int(num))
    return dataReturn

def encryptData(publicKey, data):
    encryptedData = [publicKey.encrypt(x) for x in data]
    return encryptedData

def readPublicKey():
    keyFile = open('pkls/publicKey.pkl','rb')
    publicKey = pickle.load(keyFile)
    return publicKey

if __name__ == "__main__":
    data = ['H', 'C', 'S', 'O', 'N', 'Si']
    dataTrans = data2ascii(data)
    socketConn(Host, KeyManagePort, 'GetMsg')
    publicKey = readPublicKey()
    encryptedData = encryptData(publicKey, dataTrans)
    createEncryptedPickle(encryptedData)
    print('[+] Begin Sending')
    socketConn(Host, CompareServerPort, 'pkls/dataFromClient1.pkl')