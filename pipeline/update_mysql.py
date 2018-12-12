#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import MySQLdb

#打印脚本路径
print(sys.argv[0])

#打印第一个参数
print(sys.argv[1])

imageName = sys.argv[1]
imageNameSplit = imageName.split('/')
imageNameUserDefine = imageNameSplit[2]
#10.12.4.26:5000/user-images/test_dir:170
a = 2
# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "root", "sangjing", "dataset", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#cursor.execute("""INSERT INTO images(name,place,description,provider,createtime) VALUES (%s,"10.11.3.8:5000/user-images/sangjing","这是我的镜像描述","sangjing",NOW())"""%(a))
# SQL 插入语句
sql = """INSERT INTO images(name,place,description,provider,createtime) VALUES (%s,"10.11.3.8:5000/user-images/sangjing","这是我的镜像描述","sangjing",NOW())"""%(imageNameUserDefine)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 出现任何错误进行回滚
   db.rollback()

# 关闭数据库连接
db.close()