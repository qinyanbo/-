# coding=utf-8
import socket

client = socket.socket()  # 创建一个socket对象
server_ip_port = ('172.20.10.7', 20000)  # 服务器端的ip+端口,元组类型
client.connect(server_ip_port)  # 客户端连接服务端

while True:
    client_input = input('请输入下发给串口的指令>>>>：')
    client.send(client_input.encode('utf-8'))  # 给服务端发送bytes类型的消息
    if client_input == 'bye':
        break
    # from_server_msg = client.recv()  # 接收最大为1024B(1K)的消息,
    # from_server_msg = from_server_msg.decode('utf-8')

    # print('来自服务端的消息：', from_server_msg)  # 打印解码后的消息
    # if from_server_msg == 'bye':
    #     break
client.close()  # 客户端挂电话

