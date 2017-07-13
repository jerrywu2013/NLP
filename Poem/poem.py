import re
from collections import Counter

dic = []
data = open('1112.txt','r') 

for i in data.readlines():
    dic.append(i.strip().replace('：','').replace('，','').replace('。','').replace('？','').replace('！','').replace('［','').replace('］',''))  #去除一些不用的符号
word = ''.join(dic)
word_str = re.sub(r"(?<=\w)","",word)  
word_list = list(word_str)
a = [v for v in word_list if not str(v).isdigit()]

c = Counter(a)
s = c.most_common(300)  
tangshi = []
for i in s:
    tangshi.append(i[0])

import random
i = random.sample(tangshi,20) 
print(i[0]+i[1]+i[2]+i[3]+i[4]+'，'+i[5]+i[6]+i[7]+i[8]+i[9]+'。'+'\n'+i[10]+i[11]+i[12]+i[13]+i[14]+'，'+i[15]+i[16]+i[17]+i[18]+i[19]+'。')