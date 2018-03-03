import requests
from bs4 import BeautifulSoup
import bs4
import os

root = "D://python//"
path = root + 'list.txt'

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].contents[0], tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

def saveUnivList(ulist):
    if not os.path.exists(root):
        print("路径不存在，正在创建")
        os.mkdir(root)
        print("创建成功！")
    if not os.path.exists(path):
        print("正在保存文件...")
        with open(path,'w') as f:
            for i in range(len(ulist)):
                u = ulist[i]
                f.write(','.join(u))
                f.write('\n')
            f.close()
            print("保存成功！")
    else:
        print("文件已存在")
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    saveUnivList(uinfo)
    printUnivList(uinfo, 20)
main()
