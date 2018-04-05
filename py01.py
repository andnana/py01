import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mywebsite', charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO job(id,
         job_name)
         VALUES (null, 'python工程师qqq')"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
