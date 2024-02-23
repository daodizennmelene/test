import requests
import json
from gensim.models import Word2Vec


def get_result(word1,word2):
    url = 'http://192.168.250.244:5000/nlp/made'
    model = Word2Vec.load(r"wenbenmoxing.bin")
    int_a = model.wv.similarity(word1,word2)
    data = {'res':str(int_a)}
    data_json = json.dumps(data)
    res = requests.post(url,data=data_json)
    print(res.json())


if __name__ == '__main__':
    get_result('情侣', '夫妻')



