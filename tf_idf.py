import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer 

file = open("dictionary.txt",  encoding="utf8")
strs = file.read().split("\n")
strs=strs[:len(strs)-1]
keys=[]
for line in strs:
    s=line.split(" ")
    keys.append(s[0])
    
    
import os
path=os.getcwd()
path+="/clean-data/train"
paths=os.listdir(path)
strs =[]
for p in paths:
    file = open(path+"/"+p,  encoding="utf8")
    strTmp=file.read().split("\n")
    x=len(strTmp)
    strs+=strTmp[:x-1]


cv=CountVectorizer(vocabulary=keys)
word_count_vector=cv.fit_transform(strs)
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True) 
tfidf_transformer.fit(word_count_vector)

def computing_tfidf(s):
    input_s =[]
    input_s.append(s)
    count_vector=cv.transform(input_s) 
    tf_idf_vector=tfidf_transformer.transform(count_vector)
    values=tf_idf_vector.toarray().tolist()[0]
    dictionary = dict(zip(keys, values))
    return dictionary

from standardize import tien_xu_li
text = "Sáng ngày 25/2, Nathan Lee tiếp tục khiến dân tình dậy sóng khi tung nhiều tin nhắn làm bằng chứng cho rằng Cao Thái Sơn chính là nhân vật đứng sau vụ bóc phốt sai lệch khách sạn vừa qua bằng cách nhờ người khác đăng thông tin sai lệch về số tài sản của anh. Còn nhớ cách đây không lâu, Nathan Lee bị 1 người bạn của Cao Thái Sơn tố nhận vơ Toà thị chính Paris là khách sạn của nhà và rao bán với mức giá 2500 tỷ đồng trong mùa dịch Covid-19."
text = tien_xu_li(text)
dic=computing_tfidf(text)
print(dic)