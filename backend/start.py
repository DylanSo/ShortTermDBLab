from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})  # 配置跨域


def get_sql_conn():
    """
    获取数据库连接
    """
    conn = pymysql.connect(host="localhost", user="root", password="123456", database="suycmis13")
    cursor = conn.cursor()
    return conn, cursor


def get_index_dict(cursor):
    """
    获取数据库对应表中的字段名
    """
    index_dict = dict()
    index = 0
    for desc in cursor.description:
        index_dict[desc[0]] = index
        index = index + 1
    return index_dict


def get_dict_data_sql(cursor, sql):
    """
    运行sql语句，获取结果，并根据表中字段名，转化成dict格式（默认是tuple格式）
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    index_dict = get_index_dict(cursor)
    res = []
    for datai in data:
        resi = dict()
        for indexi in index_dict:
            resi[indexi] = datai[index_dict[indexi]]
        res.append(resi)
    return res


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return jsonify('Hello World!')


@app.route('/getStudentsData', methods=['GET', 'POST'])
def return_stu_data():  # put application's code here
    con, cursor = get_sql_conn()
    # sql语句
    sql = "SELECT\
	suyc_student13.syc_sno13, \
	suyc_student13.syc_sname13, \
	suyc_student13.syc_ssex13, \
	suyc_student13.syc_sage13, \
	suyc_student13.syc_source13, \
	suyc_student13.syc_scredits13, \
	suyc_student13.syc_cno13, \
	suyc_student13.syc_mno13, \
	suyc_student13.syc_ifgraduate13\
    FROM\
	suyc_student13"
    # 执行sql语句, 拿到所有返回的条目
    results = get_dict_data_sql(cursor, sql)
    print(results)
    return jsonify(results)


@app.route('/getTeachersData', methods=['GET', 'POST'])
def return_t_data():  # put application's code here
    con, cursor = get_sql_conn()
    # sql语句
    sql = "SELECT\
    suyc_teacher13.syc_tno13, \
    suyc_teacher13.syc_tname13, \
    suyc_teacher13.syc_dno13, \
    suyc_teacher13.syc_tsex13, \
    suyc_teacher13.syc_tage13, \
    suyc_teacher13.syc_title13, \
    suyc_teacher13.syc_temail13, \
    suyc_teacher13.syc_tphone13 \
    FROM \
    suyc_teacher13"
    # 执行sql语句, 拿到所有返回的条目
    results = get_dict_data_sql(cursor, sql)
    print(results)
    return jsonify(results)


if __name__ == '__main__':
    # 关闭数据库
    # db.close()
    app.run()
