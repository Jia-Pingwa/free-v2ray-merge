import requests
import base64
#读入webside.txt 中的内容，并按行分割，生成一个列表
with open('webside.txt','r') as f:
    webside = f.read().splitlines()
# 用request get列表中的每一个网址，并将结果写入到文件中
for i in webside:
    r = requests.get(i)
    # 对r进行base64解码
    # print(r.text)
    temp = base64.b64decode(r.text)
    with open('r.txt','wb') as f:
        f.write(temp)
#读取r.txt中的内容
with open('r.txt','r') as f:
    txt = f.read()
# 将r.txt中的内容按行分割，生成一个列表
txt = txt.splitlines()
# 对txt列表进行去重
txt = list(set(txt))
# 将txt列表写入到文件中
with open('r.txt','w') as f:
    for i in txt:
        f.write(i+'\n')

