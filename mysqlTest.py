# /usr/env/bin python
# -*- coding:utf-8 -*-
import pymysql
import time


class mysqlClient():
    def __init__(self,host,  username, password, database,port):
        # 连接数据库
        conn = pymysql.connect(host=host, user=username, password=password, database=database, port=port,charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        self._conn=conn
        self._cursor = cursor


    #返回查询到的数量
    def sumSQL(self,querySql):
        return self._cursor.execute(querySql)

    ##查询
    #返回查询结果中第一条结果
    def queryOne(self,querySql):
        self._cursor.execute(querySql)
        return self._cursor.fetchone()
    #返回查询结果中前num条的结果
    def queryMany(self,querySql,num):
        self._cursor.execute(querySql)
        return self._cursor.fetchmany(num)
    #返回全部查询结果
    def queryAll(self,querySql):
        self._cursor.execute(querySql)
        return self._cursor.fetchall()

    ##插入
    #插入单条数据
    def insertOne(self,insertSql,insertData):
        print(insertSql)
        print(insertData)
        self._cursor.execute(insertSql,insertData)
        self._conn.commit()

    # 插入多条数据
    def insertMany(self,insertSql,insertDataList):
        self._cursor.executemany(insertSql,insertDataList)
        self._conn.commit()





    def mysqlClose(self):
        # 关闭指针对象
        self._cursor.close()
        # 关闭连接对象
        self._conn.close()
    # def connect_collection(self,tablename):
    #     #确定连接的聚集
    #     self._tablename = tablename
    #     self.collection = self.db[tablename]
    #     return self._tablename,self.collection




if __name__=="__main__":
    mysql1=mysqlClient("localhost", "root","!QAZ2wsx", "test_001",3306)
    querySql="SELECT * FROM test1"
    insertSql="insert into test1(id,name,age) VALUES(%s,%s,%s)"
    insertData=(8,"八意永琳",260)
    insertDataList=[(9,"蕾米莉亚·斯卡雷特",555),(8,"帕秋莉·诺蕾姬",250)]
    #print(mysql1.sumSQL(querySql))
    #print(mysql1.queryOne(querySql))
    #print(mysql1.queryMany(querySql,2))
    #print(mysql1.queryAll(querySql))
    #mysql1.insertOne(insertSql,insertData)
    mysql1.insertMany(insertSql, insertDataList)
    print(mysql1.queryAll(querySql))
    mysql1.mysqlClose()




# conn = pymysql.connect(host="localhost", user="root", password="!QAZ2wsx", database="test_001", port=3306,charset="utf8")
#         # 创建游标
# cursor = conn.cursor()
# querySql="SELECT * FROM test1"
# insertSql="insert into test1(id,'name',age) VALUES(%s,%s,%s)"
# insertData=(6,"十六夜咲夜",27)
# #cursor.execute(insertSql,insertData)
# cursor.execute("insert into test1(id,name,age) VALUES(%s,%s,%s)",(7,"铃仙",16))
# conn.commit()
# cursor.execute(querySql)
# print(cursor.fetchall())
