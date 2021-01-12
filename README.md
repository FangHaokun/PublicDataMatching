# PublicDataMatching

## 简介

该项目是基于同态加密的共有数据匹配，可以用于样本对齐。

该系统共有**密钥管理中心**，**比较服务器**与**客户端三方**。密钥管理中心生成密钥对，包括公钥与私钥。客户端初始化之后，从密钥管理中心获取公钥，并使用公钥为数据加密。客户端将加密数据传给服务器，比较服务器进行同态运算后，将运算结果发给密钥管理中心解密。密钥管理中心解密后将共有数据交由比较服务器并转发至各客户端

## 运行方法 

  >安装phe库:  **pip install phe**

  >终端 1:  **python KeyManager.py**
  
  >终端 2:  **python ComparingServer.py**
  
  >终端 3:  **python client1.py**
  
  >终端 4:  **python client2.py**

## Introduction

This project is based on homomorphic encryption of public data matching, which can be used for sample alignment.

The system has **a key management center**, **a comparison server** and **some clients**. The key management center generates a key pair, including a public key and a private key. After the client is initialized, it obtains the public key from the key management center and uses the public key to encrypt data. The client transmits the encrypted data to the server。 And after the comparison server performs the homomorphic calculation, the calculation result is sent to the key management center for decryption. After decryption by the key management center, the shared data is handed over to the comparison server and forwarded to each client.

## How to run 

  >Install phe package for python:  **pip install phe**

  >Termianl 1:  **python KeyManager.py**
  
  >Termianl 2:  **python ComparingServer.py**
  
  >Terminal 3:  **python client1.py**
  
  >Terminal 4:  **python client2.py**
 
