from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

from pymongo import MongoClient     #몽고디비를 사용하기 위한 import

client = MongoClient('localhost', 27017)       # ip주소 :localhost, port번호: 27017 를 이용해 몽고디비에 접속한다.
db = client.myproject                           # myproject라는 디비에 접속한다.(없으면 새로 만든다.)


## HTML 화면 보기
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api/food', methods=['GET'])
def show_foods():
    myfoods_from_db = list(db.food.find({}, {"_id": False}))
    return jsonify({'result': 'success', 'myfoods': myfoods_from_db})


@app.route('/api/search', methods=['POST'])
def find_from_db():
    value_received = request.form['value_get']      #index에서 보내진 value_get변수를 value_received라는 변수로 받는다.
    search_result = list(db.food.find({'name': {'$regex': value_received}}, {'_id': False})) # 그리고 나서 받은 값(검색값)을 포함한 모든 값들을 디비에서 찾아서 search_result 변수에 넣는다.
    return jsonify({'result': 'success', 'search_result': search_result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)