from pymysql import *
conn = connect(host="localhost", database="jing_dong", user="root", password="SXBCMZT.", charset="utf8")
cursor = conn.cursor()
cursor.execute("select * from goods")
print(cursor.fetchall())
