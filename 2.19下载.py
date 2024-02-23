import nltk
'''nltk调用停用词'''
from nltk.corpus import stopwords
# 下载停用词资源
nltk.download('stopwords')
# 获取中文停用词表
stopwords1=stopwords.words('chinese')
# 打印中文停用词表
print(len(stopwords1))
print(stopwords)

stopwords=stopwords.words('english')
# 打印英文停用词表
print(len(stopwords))
print(stopwords)
print("="*50)
# sklearn 调用停用词
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# print("停用词数量",len(ENGLISH_STOP_WORDS))
# print("停用词表",list(ENGLISH_STOP_WORDS))
# print("="*50)
# # gensim调取停用词
# from gensim.parsing.preprocessing import  STOPWORDS
#
# print("停用词数量",len(STOPWORDS))
# print("停用词表",list(STOPWORDS))
# print("="*50)