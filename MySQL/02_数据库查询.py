# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import MySQLdb


class MysqlSearch(object):
    def __init__(self):
        '''初始化调用连接数据库'''
        self.get_conn()

    def get_conn(self):
        '''获取一条数据'''
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='q8022761',
                db='news',
                charset='utf8'
            )


        # 捕获异常
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def close_conn(self):
        '''关闭数据库的链接'''

        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    def get_one(self):
        '''获取一条数据'''

        # 准备SQL语句
        sql = 'select * from news where type = %s order by created_at asc;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('资讯',))
        # 拿到结果
        # rest = cursor.fetchone()
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # print(rest)
        # print(rest['title'])
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self):
        '''获取全部  的数据'''
        # 准备SQL
        sql = 'select * from news where type = %s order by created_at desc;'

        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('资讯',))

        # 按到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]

        # 处理数据
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return rest

    def get_more_by_page(self, page, page_size):
        '''分页获取'''

        offset = (int(page) - 1) * int(page_size)
        # 准备SQL
        sql = 'select * from news where type = %s order by created_at desc limit %s, %s'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('资讯', offset, page_size))

        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]

        # 处理数据
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        '''插入一条数据'''

        try:

            # 准备SQL
            sql = ("insert into news (title, image, content, type, is_valid) value (%s, %s, %s, %s, %s)")

            # 获取连接和cursor
            cursor = self.conn.cursor()

            # 执行SQL语句
            cursor.execute(sql, ('标题3', 'static/img/news/01.png', '新闻内容2', '推荐', 1))
            cursor.execute(sql, ('标题4', 'static/img/news/01.png', '新闻内容2', '推荐', 1))

            # 提交事务
            self.conn.commit()
            cursor.close()

        except Exception as e:
            print(e)
            # 发生错误回滚
            self.conn.rollback()
        # 关闭数据库连接
        self.close_conn()


def main():
    '''主函数'''

    # 获取一条数据
    # obj = MysqlSearch()
    # rest = obj.get_more()
    # print(rest)
    # print(rest[0]['title'])


    # 获取全部数据
    # obj = MysqlSearch()
    # rest = obj.get_more()
    # for item in rest:
    #     print(item['title'])

    # 获取分页数据
    obj = MysqlSearch()
    rest = obj.get_more_by_page(4, 3)
    for item in rest:
        print(item)
        print(item['title'])

    # obj = MysqlSearch()
    # obj.add_one()


if __name__ == '__main__':
    main()
