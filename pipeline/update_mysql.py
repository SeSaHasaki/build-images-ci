#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import MySQLdb

#打印脚本路径
print(sys.argv[0])

imageName = sys.argv[1]
imageNameSplit = imageName.split('/')

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "root", "sangjing", "dataset", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO images(name,place,description,provider,createtime) VALUES ("%s","10.11.3.8:5000/user-images/sangjing","这是我的镜像描述","sangjing",NOW())"""%(imageNameSplit[2])
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