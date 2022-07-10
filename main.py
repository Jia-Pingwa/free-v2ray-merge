import requests
import base64
#读入webside.txt 中的内容，并按行分割，生成一个列表
with open('webside.txt','r') as f:
    webside = f.read().splitlines()
# 用request get列表中的每一个网址，并将结果进行base64解码后加入列表txt
txt = []
for i in webside:
    r = requests.get(i)
    txt.append(base64.b64decode(r.text).decode('utf-8'))
# 对txt列表进行去重
txt = list(set(txt))
# 将txt列表写入到文件中
with open('output.txt','w') as f:
    for i in txt:
        f.write(i+'\n')