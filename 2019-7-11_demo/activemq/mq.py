import stomp
import json

# 此处配置中的HOSTADDRESS和TOPIC需要和前端
# 代码中的配置统一，建议设置好后告知前端开发人员
# 其中TOPIC的配置'/topic'这一级目录结构必须存在
# 建议在'/topic'目录下再建一层自定义的目录，例如：
# '/topic/scene_id'
# 注：将数据往消息队列中发送时必须保证Activemq成功运行！

HOSTADDRESS = '127.0.0.1'
PORTNUMBER  = 61613
TOPIC = "/topic/111/real_time_data"


# 推送消息到主题topic中
def send_msg_to_topic(topic_name, msg):
    conn = stomp.Connection10([(HOSTADDRESS, PORTNUMBER)])
    conn.start()
    conn.connect(username='admin', password='admin')
    conn.send(topic_name, msg)
    conn.disconnect()


# 定义往Activemq消息队列中发送的数据样例
data = {
    "light": {
        "light_status": 1,
        "light_insert_time": "2019-03-13 10:27:29"
    },
    "co2": {
        "co2_value": " 5.18",
        "co2_insert_time": "2019-03-13 10:27:29",
        "co2_status": 1
    }
}


send_msg_to_topic(TOPIC, json.dumps(data))
