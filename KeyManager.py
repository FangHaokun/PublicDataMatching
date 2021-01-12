import socket               
from phe import paillier
import pickle

def createKeyPairs():
    public_key, private_key = paillier.generate_paillier_keypair()
    return public_key, private_key

def createKeyPairsFiles(publicKey, privateKey):
    privateFile = open('pkls/privateKey.pkl','wb')
    pickle.dump(privateKey,privateFile)
    privateFile.close()
    publicFile = open('pkls/publicKey.pkl','wb')
    pickle.dump(publicKey,publicFile)
    publicFile.close()

#公共数据比对之后返回[i.j]
def decryptCompareData[i.j]():
    dataFile = open('pkls/compareRes.pkl', 'rb')
    data = pickle.load(dataFile)
    dataFile.close()
    print(data)

if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    port = 12001
    publicKey, privateKey = createKeyPairs()
    createKeyPairsFiles(publicKey, privateKey)
    s.bind((host, port))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print('连接地址：', addr)
        print(c.recv(1024).decode())
        if c.recv(1024).decode() == 'GetMsg':
            print('[+] GetMsg')
            c.send('CreateFinish'.encode())
        elif c.recv(1024).decode() == 'Decrypt':
            print('[+] Decrypt')
            decryptCompareData()
            c.send('DecryptFinish'.encode())
        else:
            print('[?]')
        c.close()