import socket
import threading
from queue import Queue


IP_ADDR = '172.20.10.9' #此处ip测试时配置为中控服务器的本机ip，部署在云服务器上需要配置为0.0.0.0
PORT_NUMBER1 = 20000  # 用于接收Django后台发来的指令
PORT_NUMBER2 = 20001  # 用于接收网关客户端发来的数据，并将django后台发来的指令转发给网关客户端

server1 = socket.socket()
ip_port = (IP_ADDR, PORT_NUMBER1)
server1.bind(ip_port)
server1.listen(2)

server2 = socket.socket()
ip_port = (IP_ADDR, PORT_NUMBER2)
server2.bind(ip_port)
server2.listen(2)


def recv_cmd_from_django(q):
    while True:
        print("等待新django客户端连接......")
        conn, addr = server1.accept()
        print('新django客户端连接成功，IP为：', addr[0], '端口号为：', addr[1])
        while True:
            from_client_msg = conn.recv(1024)
            from_client_msg = from_client_msg.decode('utf-8')
            print("来自django客户端的消息:", from_client_msg)
            q.put(from_client_msg)
            if from_client_msg == 'bye':
                break
        print('与上次django客户端断开连接')
        conn.close()


def recv_data_from_gateway(q):
    while True:
        print("等待新网关客户端连接......")
        conn, addr = server2.accept()
        print('新网关客户端连接成功，IP为：', addr[0], '端口号为：', addr[1])
        while True:
            def send_cmd_to_gateway():
                while True:
                    if not q.empty():
                        data = q.get()
                        q.queue.clear()
                        conn.send(data.encode('utf-8'))
            send_cmd_to_gateway_th = threading.Thread(target=send_cmd_to_gateway)
            send_cmd_to_gateway_th.start()

            from_client_msg = conn.recv(1024)
            from_client_msg = from_client_msg.decode('utf-8')
            print("来自网关客户端的消息:", from_client_msg)
            if from_client_msg == 'bye':
                break
        print('与上次网关客户端断开连接')
        conn.close()


q = Queue(1)
recv_cmd_from_django_th = threading.Thread(target=recv_cmd_from_django, args=(q,))
recv_data_from_gateway_th = threading.Thread(target=recv_data_from_gateway, args=(q,))

recv_cmd_from_django_th.start()
recv_data_from_gateway_th.start()
recv_cmd_from_django_th.join()
recv_data_from_gateway_th.join()