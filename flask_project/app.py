from turtle import pd
from flask import Flask, render_template, request
import sqlite3

from flask import Flask, request



import json


# def get_db(db_name):
#     return sqlite3.connect(db_name)

# def exe_sql(conn, command: str):
    
#     try:
#         conn.execute(command)
#         conn.commit()

#         if command.split()[0].lower() == 'select':
#             df = pd.read_sql(command, conn, index_col=None)
#             df_html = df.to_html()
#             return df_html, 1
#     except:
#         return None, 0

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello world"

# @app.route('/sql')
# def index():
#     return render_template('index.html')

# @app.route('/command', methods=['POST'])
# def command():    
#     return "TEST" + request.form.get('first_test') # render_template('index.html')

# @app.route('/data')
# def data_page():
#     return render_template('data.html')

# @app.route('/dbsql', methods=["POST"])
# def sql_test():
#     if request.method=='POST':
#         db_name = request.form.get('db_name')
#         sql_command = request.form.get('sql')

#         conn = get_db(db_name)

#         output, status = exe_sql(conn, sql_command)
#         if status==1:
#             # 잘 처리됨
#             return render_template('data.html', label = "정상 작동")

#         else:
#             return render_template('data.html', label = "오류 발생")

app = Flask(__name__);


@app.route("/")
def helloWorld():
    return "Hello World!"




if __name__=="__main__":
    app.run(debug=True)