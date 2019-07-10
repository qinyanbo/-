# 导入模块

import serial #串口模块
import threading  # 线程模块
import socket #网络编程模块

IP_ADDR = '172.20.10.9'  # 此处ip地址填网关连接的中控服务器的ip地址
PORT_NUMBER = 20001


from config import SERIAL_CONFIG, DOWN_PROTOCOL


m = serial.Serial(**SERIAL_CONFIG)
print('串口初始化成功！')

# 场景id
scene_id = 2
for cmd_item in DOWN_PROTOCOL.values():
    cmd_item[7] = scene_id
    # print(cmd_item)
# print(DOWN_PROTOCOL)


# 字符串转16进制，用于处理串口接收的数据
def convert_hex(string):
    res = []
    result = []
    for item in string:
        res.append(item)
    for i in res:
        result.append(hex(i))
    return result


def recv_serial_data():
    while True:
        resp = bytearray(b'')
        current = m.read()
        if current == b'':
            continue
        elif current == b'\xef':
            resp += current
            current = m.read()
            if current == b'\xef':
                resp += current
                resp += m.read()  # 保留位
                resp += m.read(2)  # 短地址
                # resp += m.read()  # 短地址
                size = m.read()  # 帧长度
                resp += size
                size = size[0]
                # print(size)

                resp += m.read(size - 6)

                resp1 = convert_hex(resp)

                # print(resp1)


def send_cmd():
    client = socket.socket()  # 创建一个socket对象
    ip_port = (IP_ADDR, PORT_NUMBER)  # 创建一个电话卡, 是元组类型
    client.connect(ip_port)
    print('网关程序连接中控服务器成功')
    while True:
        from_client_msg = client.recv(1024)  # 服务端必须通过两者之间的连接通道来收消息,接收到的数据消息是bytes类型
        from_client_msg = from_client_msg.decode('utf-8')  # 将接收到的数据消息进行解码
        print("来自从django客户端通过中转服务器发来的指令:", from_client_msg)
        minput = from_client_msg
        # minput = input('请输入下发给串口的指令>>>>：')
        if minput == 'f':
            # 获取风扇状态 f
            m.write(DOWN_PROTOCOL['GETFAN'])
        elif minput == 'f1':
            # 打开风扇 f1
            m.write(DOWN_PROTOCOL['OPENFAN'])
        elif minput == 'f0':
            # 关闭风扇 f0
            m.write(DOWN_PROTOCOL['CLOSEFAN'])

        elif minput == 'light':
            # 灯
            m.write(DOWN_PROTOCOL['GETLIGHT'])
        elif minput == 'light1':
            # 打开灯
            m.write(DOWN_PROTOCOL['OPENLIGHT'])
        elif minput == 'light0':
            # 关闭灯
            m.write(DOWN_PROTOCOL['CLOSELIGHT'])

        elif minput == 'C':
            # 获取CO2的值 C
            m.write(DOWN_PROTOCOL['GETCO2'])
        elif minput == 'B':
            # 获取光照强度的值 B
            m.write(DOWN_PROTOCOL['GETBEAM'])
        elif minput == 'T':
            # 获取温度的值 T
            m.write(DOWN_PROTOCOL['GETTEMPERATURE'])
        elif minput == 'H':
            # 获取湿度的值 H
            m.write(DOWN_PROTOCOL['GETHUMIDITY'])
        elif minput == 'F':
            # 获取火光 的值  F
            m.write(DOWN_PROTOCOL['GETFLAME'])
        elif minput == 'M':
            # 获取甲烷的值  M
            m.write(DOWN_PROTOCOL['GETMETHANE'])
        elif minput == 'S':
            # 获取烟雾的值 S
            m.write(DOWN_PROTOCOL['GETSMOKE'])
        elif minput == 'PM2.5':
            # 获取PM2.5的值 PM2.5
            m.write(DOWN_PROTOCOL['GETPM25'])

        elif minput == 'a':
            # 获取报警器的值 a
            m.write(DOWN_PROTOCOL['GETALERTOR'])
        elif minput == 'a1':
            # 打开报警器 a1
            m.write(DOWN_PROTOCOL['OPENALERTOR'])
        elif minput == 'a0':
            # 关闭 报警器 a0
            m.write(DOWN_PROTOCOL['CLOSEALERTOR'])
        elif minput == 'al':
            # 获取报警灯的值 al
            m.write(DOWN_PROTOCOL['GETALARMLAMP'])
        elif minput == 'al1':
            # 打开报警灯  al1
            m.write(DOWN_PROTOCOL['OPENALARMLAMP'])
        elif minput == 'al0':
            # 关闭报警灯 al0
            m.write(DOWN_PROTOCOL['CLOSEALARMLAMP'])

        elif minput == 'I':
            # 获取入侵检测状态 I
            m.write(DOWN_PROTOCOL['GETINVADE'])
        elif minput == 'P':
            # 获取光电传感器的值 P
            m.write(DOWN_PROTOCOL['GETPHOTOSENSOR'])

        elif minput == 'r11':
            # 打开继电器1 r11
            m.write(DOWN_PROTOCOL['OPENRELAY1'])
        elif minput == 'r10':
            # 关闭继电器1 r10
            m.write(DOWN_PROTOCOL['CLOSERELAY1'])
        elif minput == 'r21':
            # 打开继电器2 r21
            m.write(DOWN_PROTOCOL['OPENRELAY2'])
        elif minput == 'r20':
            # 关闭继电器2 r20
            m.write(DOWN_PROTOCOL['CLOSERELAY2'])

        elif minput == 'p':
            # 获取水泵状态 p
            m.write(DOWN_PROTOCOL['GETPUMP'])
        elif minput == 'p1':
            # 打开水泵 p1
            m.write(DOWN_PROTOCOL['OPENPUMP'])
        elif minput == 'p0':
            # 关闭水泵 p0
            m.write(DOWN_PROTOCOL['CLOSEPUMP'])

        elif minput == 'l':
            # 获取锁状态 l
            m.write(DOWN_PROTOCOL['GETLOCK'])
        elif minput == 'l1':
            # 打开锁 l1
            m.write(DOWN_PROTOCOL['OPENLOCK'])
        elif minput == 'l0':
            # 关闭锁 l0
            m.write(DOWN_PROTOCOL['CLOSELOCK'])

        else:
            # 在led上写字 lw
            data = minput.encode('gbk')
            data_len = len(data) + 11
            DOWN_PROTOCOL['WRITELED'][5] = data_len
            DOWN_PROTOCOL['WRITELED'][10:11] = data
            m.write(DOWN_PROTOCOL['WRITELED'])
    client.close()  # 挂电话

recv_serial_th = threading.Thread(target=recv_serial_data)
send_cmd_th = threading.Thread(target=send_cmd)
# send_cmd

recv_serial_th.start()
send_cmd_th.start()

recv_serial_th.join()
send_cmd_th.join()