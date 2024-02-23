# import jieba
# import jieba.posseg as pseg
# datas=("李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
#        "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
#        "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。")
# words=jieba.lcut(datas)
# print("/".join(words))
#
# jieba.load_userdict("dest.txt")
# jieba.add_word("石墨烯")
# words=jieba.lcut(datas)
# print("/".join(words))

import jieba
from collections import Counter
with open('data_kg.txt','r',encoding='utf-8') as file:
    content=file.read()
ret1=jieba.lcut(content)
print(ret1)

with open("hit_stopwords.txt",'r',encoding='utf-8') as file:
    stopwords=file.read()
for i in stopwords:
    if i in ret1:
        ret1.remove(i)
print(ret1)
counter=Counter(ret1)
print(counter)



