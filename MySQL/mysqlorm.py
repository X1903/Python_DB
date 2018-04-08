# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# 冲入数据使用sessionmaker
from sqlalchemy.orm import sessionmaker

# 链接数据库
engine = create_engine('mysql://root:q8022761@127.0.0.1:3306/news_test?charset=utf8')
Base = declarative_base()

Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(200), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300),)
    author = Column(String(20),)
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

class OrmTest(object):
    '''插入数据'''

    def __init__(self):
        self.session = Session()

    def add_one(self):
        '''新增记录'''
        new_obj = News(
            title='标题5',
            content='内容',
            types='百家',
        )

        new_obj1 = News(
            title='标题6',
            content='内容',
            types='百家',
        )

        self.session.add(new_obj)
        self.session.add(new_obj1)
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据'''
        return self.session.query(News).get(90)

    def get_more(self):
        '''查询多条数据'''
        return self.session.query(News).filter_by(is_valid=1)

    def update_data(self, pk):
        '''修改一条数据'''
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def update_data_more(self):
        '''修改多条数据'''
        # data_list = self.session.query(News).filter_by(is_valid=0)
        data_list = self.session.query(News).filter(News.id>5)
        if data_list:
            for item in data_list:
                item.is_valid = 1
                self.session.add(item)
            self.session.commit()
            return True
        else:
            return False

    def delate_data(self, pk):
        '''删除一条数据'''
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            self.session.delete(new_obj)
            self.session.commit()
            return True
        else:
            return False

    def detale_data_more(self):
        '''删除多条数据'''
        data_list = self.session.query(News).filter(News.id>=7)
        if data_list:
            for item in data_list:
                self.session.delete(item)
            self.session.commit()
            return True
        else:
            return False


def main():
    # 插入数据
    # obj = OrmTest()
    # rest = obj.add_one()
    # print(rest.id)

    # 获取一条数据
    # obj = OrmTest()
    # rest = obj.get_one()
    # if rest:
    #     print('ID{0}=={1}'.format(rest.id, rest.title))
    # else:
    #     print('数据不存在')

    # 获取多条数据
    # obj = OrmTest()
    # rest = obj.get_more()
    # print(rest.count())
    #
    # for new_obj in rest:
    #     print('ID:{0}=={1}'.format(new_obj.id, new_obj.title))

    # 更新数据一条
    # obj = OrmTest()
    # print(obj.update_data(3))

    # 更新数据多条
    # obj = OrmTest()
    # print(obj.update_data_more())

    # 删除一条数据
    # obj = OrmTest()
    # rest = obj.delate_data(10)
    # print(rest)

    # 删除多条数据
    obj = OrmTest()
    ret = obj.detale_data_more()
    print(ret)



    # for item in rest:
    #     print(item.id)
if __name__ == '__main__':
    main()

