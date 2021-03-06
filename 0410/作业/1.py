"""
网络编程：套接字编程，Socket编程
套接字：一套用于网络通讯的API（一套类，方法）
"""

import socket
print(socket)
print(dir(socket))
# TCP通讯
socketObj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 通过调用socketObj特定方法完成进程通信

# bind方法用于 TCP 连接中将socket对象和    IP  PORT 绑定
socketObj.bind(("127.0.0.1",8888))

# listen 开始监听客户端连接
socketObj.listen()

# 阻塞方法 直到客户端有连接
# clientsoccket = socketObj.accept()

# 构造客户端socket
socketclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到tcp服务器
# socketclient.connect(("192.168.12.135",8888))

# recv,sent TCP 发送消息
# recvfrom sendto UDP收发消息

# clientsocket.close()


# UDP通讯
# socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
