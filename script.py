import re

f = open('list.txt', encoding="utf8")
for x in f:
    #url =  re.findall(r'(https?://\S+)', x)
    #num = x.split('')[1].split(')')[0]
    title = x.split(')')[1]
    tag = "<li>" + title + "</li>"
    print(tag)
  