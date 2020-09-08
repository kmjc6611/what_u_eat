from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myproject


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
    value_received = request.form['value_get']
    search_result = list(db.food.find({'name': value_received}, {'_id': False}))
    return jsonify({'result': 'success', 'search_result': search_result})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
