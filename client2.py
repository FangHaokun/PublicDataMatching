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
    return recvData.decode()


def createEncryptedPickle(data):
    dataFile = open('pkls/dataFromClient2.pkl', 'wb')
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
    keyFile = open('pkls/publicKey.pkl', 'rb')
    publicKey = pickle.load(keyFile)
    return publicKey


if __name__ == "__main__":
    data = ['C', 'S', 'O', 'N', 'Si', 'P']
    dataTrans = data2ascii(data)
    print('[+] Data Load Successfully')
    socketConn(Host, KeyManagePort, 'GetMsg')
    publicKey = readPublicKey()
    print('[+] PublicKey Load successfully')
    encryptedData = encryptData(publicKey, dataTrans)
    createEncryptedPickle(encryptedData)
    print('[+] Data Encrypted Successfully and Begin Sending Encrypted Data')
    msg = socketConn(Host, CompareServerPort, 'pkls/dataFromClient2.pkl')
    if msg == 'Err':
        print('[-] Error During Comparing ...')
    else:
        fileGet = open('pkls/index4Client2.pkl', 'rb')
        indexGet = pickle.load(fileGet)
        fileGet.close()
        print('[+] CompareFinish and the same data has been shown as: ', indexGet)
