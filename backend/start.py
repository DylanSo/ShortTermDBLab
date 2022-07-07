from flask import Flask, jsonify
from flask_cors import CORS
import pymysql


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})  # 配置跨域
db = pymysql.connect(host="localhost", user="root", password="123456", database="suycmis13")


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return jsonify('Hello World!')


if __name__ == '__main__':
    # sql语句
    sql = 'select * from suyc_teacher13'
    # 定义游标
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 拿到所有返回的条目
    results = cursor.fetchall()
    print(results)
    # 关闭数据库
    # db.close()
    app.run()
