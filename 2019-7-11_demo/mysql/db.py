import pymysql

HOST = '127.0.0.1'   # 连接数据库的服务器的ip地址
USERNAME = 'test'    # 连接数据库的用户名
PASSWORD = '123456'  # 连接数据库的密码
DATABASE = 'ecs'     # 连接的数据库名
PORT = 3306          # 数据库端口号


class MysqlConnect(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self, host, user, password, port, database):
        '''
        :param host: IP
        :param user: 用户名
        :param password: 密码
        :param port: 端口号
        :param database: 数据库名
        :param charset: 编码格式
        '''
        self.db = pymysql.connect(host=host, user=user, password=password, port=port, database=database, charset='utf8')
        self.cursor = self.db.cursor()

    # 将要插入的数据写成元组传入
    def exec_data(self, sql, data=None):
        # 执行SQL语句
        self.db.ping(reconnect=True)
        self.cursor.execute(sql, data)
        # 提交到数据库执行
        self.db.commit()

    # sql拼接时使用repr()，将字符串原样输出
    def exec(self, sql):
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        # 提交到数据库执行
        self.db.commit()

    # 插入多条数据
    def exec_multi_data(self, sql, data=None):
        # 执行SQL语句
        self.db.ping(reconnect=True)
        self.cursor.executemany(sql, data)
        # 提交到数据库执行
        self.db.commit()

    def select(self, sql):
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        print('该表格中共有', len(results), '条数据')
        return len(results)  # 返回总条数
        # print(results)       # 输出表中所有的数据
        # for row in results:
        #     print(row, type(row))  # 一条数据为一个元组
        #     return row         # 返回第一条数据

    def selectone(self, sql):
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchone()
        return results  # 返回1条数
        # for row in results:
        #     return row

    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    mc = MysqlConnect(HOST, USERNAME, PASSWORD, PORT, DATABASE)
    # 查询测试
    # mc.select('select * from tablename') # 查询数据表测试
    # 插入数据测试 注意：在插入数据时tablename(即表名)后的括号中传的列名不需要传表格的自增列的列名(如id)
    #   插入一条数据
    #     整数和字符串
    # mc.exec('insert into tablename(columnname1, columnname2) values(%s, %s)' % (12, repr('aaaaa')))
    #     字符串
    # mc.exec('insert into tablename(columnname1, columnname2) values(%s, %s)' % (repr('aa'), repr('aaa')))
    # mc.exec_data('insert into tablename(columnname1, columnname2) values(%s, %s)' % (repr('b'), repr('bb')))
    # mc.exec_data('insert into tablename(columnname1, columnname2) values(%s, %s)', ('b', 'bb'))
    #   插入多条数据
    # mc.exec_multi_data('insert into tablename(columnname1, columnname2) values(%s, %s)', [('a', 'aa'), ('b', 'bb')])

