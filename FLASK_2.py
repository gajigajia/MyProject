from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)


# 아니 이렇게 한다면 지금 HTML을 두페이지 만들겠다는 것이잖아요?^^
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('table.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('ajax_test.html')


# 1월로 들어가면 GET요청을 가져와서 1월꺼를 보여줘....... 우선은 그냥 여기 들어가면 다 보여주는걸로 하자
@app.route('/database', methods=['GET'])
def database():

    # DB import를 여기다 해야한다
    client = MongoClient('localhost', 27017)
    data = client.dbsparta.indice.find()[0]

    SP500 = data['S&P']
    DOWJONES = data['DOW']
    NASDAQ = data['NDQ']

    NYindex = {"SP500":SP500, "DOWJONES": DOWJONES, "NASDAQ":NASDAQ}
    # FLASK는 list형은 불러오지 않으므로 jsonify를 사용하여 dict형으로 해야함. type(data)하면 data가 무슨 데이터타입인지 보여줌
    print(jsonify(NYindex))
    return jsonify(NYindex)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
