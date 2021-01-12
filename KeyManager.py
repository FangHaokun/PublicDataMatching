import socket
from phe import paillier
import pickle


def createKeyPairs():
    public_key, private_key = paillier.generate_paillier_keypair()
    return public_key, private_key


def createKeyPairsFiles(publicKey, privateKey):
    privateFile = open('pkls/privateKey.pkl', 'wb')
    pickle.dump(privateKey, privateFile)
    privateFile.close()
    publicFile = open('pkls/publicKey.pkl', 'wb')
    pickle.dump(publicKey, publicFile)
    publicFile.close()


# 公共数据比对之后返回[i.j]
def decryptCompareData(privateKey):
    dataFile = open('pkls/compareRes.pkl', 'rb')
    data = pickle.load(dataFile)
    dataFile.close()
    indexFromClient1 = []
    indexFromClient2 = []
    for item in data:
        temp = privateKey.decrypt(item[2])
        if temp == 0:
            indexFromClient1.append(item[0])
            indexFromClient2.append(item[1])
    print('[1] index From client1: ', indexFromClient1)
    print('[2] index From client2: ', indexFromClient2)
    indedxFile4Client1 = open('pkls/index4Client1.pkl', 'wb')
    pickle.dump(indexFromClient1, indedxFile4Client1)
    indedxFile4Client1.close()
    indedxFile4Client2 = open('pkls/index4Client2.pkl', 'wb')
    pickle.dump(indexFromClient2, indedxFile4Client2)
    indedxFile4Client2.close()


if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    port = 12001
    publicKey, privateKey = createKeyPairs()
    createKeyPairsFiles(publicKey, privateKey)
    print('[+] KeyPairs Have Been Created Successfully')
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        msg = c.recv(1024).decode()
        print('[+] Get Msg as: ', msg)
        if msg == 'GetMsg':
            print('[+] GetMsg')
            c.send('CreateFinish'.encode())
        elif msg == 'Decrypt':
            print('[+] Decrypt')
            decryptCompareData(privateKey)
            c.send('DecryptFinish'.encode())
        else:
            print('[?] Error Msg')
            c.send('Err'.encode())
        c.close()
