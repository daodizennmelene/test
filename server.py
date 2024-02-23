import json
from flask import jsonify
from flask import request
from flask import Flask
from gensim.models import Word2Vec


app = Flask(__name__)


def get_word(word):

    # for w in model.wv.index_to_key:
    #     print(w)
    #     input()
    return word
    # return int(word)*int(word)

@app.route('/nlp/made',methods=['GET','POST'])
def nlp_service():
    data = request.get_data()
    result_data = json.loads(data)
    word = result_data.get('res','')
    # value = get_word(word)
    return jsonify({'code':200,'result':word})


if __name__ == "__main__":
    app.run(host='0.0.0.0')