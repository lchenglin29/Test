import flask
import mydef
import json
import logging
import time
import pytz

from mydef import load_json,write_js,now_time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/load_json/<name>',methods=['GET'])
def get_data(name):
  try:
    data = load_json(name)
    return jsonify(data)
  except Exception as e:
    print(e)
    return jsonify({"error":str(e)})
    

@app.route('/write_js/<name>', methods=['POST'])
def save_data(name):
  # 从请求中获取数据，例如：data = request.get_json()
  try:
    af_data = request.get_json()
    write_js(name,af_data)
    return {"confirm":True}
  except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return "Internal Server Error", 500
  # 处理保存数据的逻辑
  # 保存数据到文件或数据库
  # 返回响应，例如：return jsonify({'message': 'Data saved successfully'})

@app.route('/',methods=['GET'])
def main():
  return "Test!"

@app.route('/getid',methods=['GET'])
def getid():
  data = load_json('id')
  data.setdefault('id',0)
  write_js('id',data)
  data = load_json('id')
  sid = data['id']
  data['id']+=1
  write_js('id',data)
  return str(sid)

@app.route('/friend_apply',methods=['POST'])
def friend_apply():
  data = request.get_json()
  rqer = data["rqer"]
  user = data["user"]
  fa_data = load_json("friend_apply")
  fa_data.setdefault(user,[])
  if rqer not in fa_data[user]:
    fa_data[user].append(rqer)
    write_js("friend_apply",fa_data)
  return("ok")

@app.route('/online',methods=['POST'])
def online():
  data = request.get_json()
  user = data["user"]
  menu_data = load_json("menu")
  menu_data[user] = 0
  write_js("menu",menu_data)
  return "ok"

@app.route('/offline',methods=['POST'])
def offline():
  data = request.get_json()
  user = data["user"]
  menu_data = load_json("menu")
  menu_data[user] = 1
  write_js("menu",menu_data)
  return "ok"

@app.route('/friend_accept',methods=['POST'])
def friend_accept():
  data = request.get_json()
  user = data["user"]
  rqer = data["rqer"]
  us_data = load_json(user)
  rq_data = load_json(rqer)
  us_data[user].setdefault("friend",[])
  us_data[user]["friend"].append(rqer)
  rq_data[rqer].setdefault("friend",[])
  rq_data[rqer]["friend"].append(user)
  write_js(user,us_data)
  write_js(rqer,rq_data)
  return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)