from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbproject


## HTML 화면 보기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/food', methods=['GET'])
def show_foods():
    # name_food = request.args.get('name_food')
    foods = list(db.food.find({'name': {'$regex':'닭'}},{'_id': False}))
    for food in foods:
        print(food)

    # print(name_food)

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)