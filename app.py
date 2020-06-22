from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/insert', methods=['POST'])
# def k_list():
    
    # list1_receive = request.form.getlist['list1_give[]']
    # list2_receive = request.form.getlist['list2_give[]']
    # list3_receive = request.form.getlist['list3_give[]']
    # list4_receive = request.form.getlist['list4_give[]']

    # keywords = {
    #    'list1': list1_receive,
    #    'list2': list2_receive,
    #    'list3': list3_receive,
    #    'list4': list4_receive
    # }

    # # db.getkeyword.insert_one(keywords)
    # return jsonify({'result':'success', 'msg': '키워드 보기!'})

@app.route('/success', methods=['POST'])
def k_success():
    list1_receive = request.form.getlist('list1_give[]')
    list2_receive = request.form.getlist('list2_give[]')
    list3_receive = request.form.getlist('list3_give[]')
    list4_receive = request.form.getlist('list4_give[]')

    doc = {
        'list1': list1_receive,
        'list2': list2_receive,
        'list3': list3_receive,
        'list4': list4_receive
    }

    db.getkeywords.insert_one(doc)
    return jsonify({'result':'success', 'msg': '키워드가 잘 저장되었습니다!'})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)