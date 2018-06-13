import os
import re
import http.cookiejar
from lxml import etree
import requests

studentnumber = input('学 号 :')
password = input('密 码 :')

s = requests.session()
url = "http://219.149.172.4:81/"
response = s.get(url)
selector = etree.HTML(response.content)
__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
imgUrl = "http://219.149.172.4:81/CheckCode.aspx"
imgresponse = s.get(imgUrl, stream=True)
image = imgresponse.content
DstDir = os.getcwd() + "\\"
print("保存验证码到：" + DstDir + "code.jpg" + "\n")
try:
    with open(DstDir + "code.jpg", "wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
code = input("验证码是：")
data = {
    "__VIEWSTATE": __VIEWSTATE,
    "txtUserName": studentnumber,
    "TextBox2": password,
    "txtSecretCode": code,
    "Button1": "",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}
# #登陆教务系统
response = s.post(url, data=data, headers=headers)
print("成功进入教务系统！")


def getInfor(response, xpath):
    content = response.content.decode('gb2312')  # 网页源码是gb2312要先解码
    selector = etree.HTML(content)
    infor = selector.xpath(xpath)
    return infor


# 获取学生基本信息
username = getInfor(response, '//*[@id="xhxm"]/text()')
username = ''.join(username)
username = username.replace('同学', '')
print(username)
kburl = 'http://219.149.172.4:81/xscj_gc.aspx?xh={}&xm={}&gnmkdm=N121605'.format(studentnumber, username)
headers = {
    "Referer": 'http://219.149.172.4:81/xs_main.aspx?xh=%s' % (studentnumber),
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

viewstate = 'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwxNDA2MDI0MTMxOz4+O2w8aTwxPjs+O2w8dDw7bDxpPDE+O2k8Mz47aTw1PjtpPDc+O2k8OT47aTwxMT47aTwxMz47aTwxNj47aTwyNj47aTwyNz47aTwyOD47aTwzNT47aTwzNz47aTwzOT47aTw0MT47aTw0NT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85a2m5Y+377yaMTQwNjAyNDEzMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85aeT5ZCN77ya5aea5rW36b6ZOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlrabpmaLvvJrorqHnrpfmnLrns7s7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS4k+S4mu+8mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8572R57uc5bel56iLOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJoxNDA2MDI0MTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxNDA2MDI7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8WE47WE47Pj47Pjt0PGk8MTM+O0A8XGU7MjAxNy0yMDE4OzIwMTYtMjAxNzsyMDE1LTIwMTY7MjAxNC0yMDE1OzIwMTMtMjAxNDsyMDEyLTIwMTM7MjAxMS0yMDEyOzIwMTAtMjAxMTsyMDA5LTIwMTA7MjAwOC0yMDA5OzIwMDctMjAwODsyMDA2LTIwMDc7PjtAPFxlOzIwMTctMjAxODsyMDE2LTIwMTc7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7MjAxMi0yMDEzOzIwMTEtMjAxMjsyMDEwLTIwMTE7MjAwOS0yMDEwOzIwMDgtMjAwOTsyMDA3LTIwMDg7MjAwNi0yMDA3Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPFpKVTs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47PlH5ogVq2pEaTga1O7OqLf9jfie+'
data1 = {
    "__VIEWSTATE": viewstate,
    'ddlXN': '',
    'ddlXQ': '',
    'Button2': '(unable to decode value)'
}

response = s.post(kburl, headers=headers, data=data1)

myhtml = response.text
ret = re.findall(
    '<td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.?)</td>',
    myhtml)
for x in ret:
    print('学年:', x[0])
    print('课程名称:', x[3])
    print('课程性质:', x[4])
    print('学分:', x[6])
    print('绩点', x[7])
    print('成绩:', x[8])
    print('*' * 60)
