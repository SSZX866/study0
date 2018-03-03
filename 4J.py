# encoding=utf8
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://www.chsi.com.cn/cet/query'


def start(zkzh):
    print(zkzh)

    xm = '曹兴旺'
    driver = webdriver.Chrome(executable_path='D:\phantomjs-2.1.1-windows\\bin\chromedriver.exe')
    driver.get(url)
    driver.find_element_by_id('zkzh').send_keys(zkzh)
    driver.find_element_by_id('xm').send_keys(xm)
    driver.find_elements_by_tag_name('form')[1].submit()
    driver.set_page_load_timeout(10)
    ''''leibie = driver.find_element_by_xpath("//tr[3]/td[1]").text
        leibie2 = str(leibie.encode("utf-8"))
        ss = ""
        if leibie2.decode("utf-8") == '英语四级'.decode("utf-8"):
            ss = 4
        else:
            ss = 6
        # zongfen = driver.find_element_by_xpath("//tr[6]/th[1]").text
        # print zongfen
        # print "===="
        chuli = driver.find_element_by_xpath("//tr[6]/td[1]").text
        chuli2 = str(chuli.encode("utf-8"))
        m = re.findall(r'(\w*[0-9]+)\w*', chuli2)
        sqltxt = "update cet.cet set leibie=(%s),zongfen=(%s),tingli=(%s),yuedu=(%s),xiezuo=(%s) WHERE zkzh=(%s)" % (
            ss, m[0], m[1], m[2], m[3], i)
        cur.execute(sqltxt)
        conn.commit()
        print str(i) + " finish"'''
    print(zkzh,zkzh)
    #except:
       # return ''

def main():
    '''for i in range(0,9):
        zkzh = str('130170172100' + str(i) + '14')
        start(zkzh)
    for i in range(10,99):
        zkzh = str('13017017210' + str(i) + '14')
        start(zkzh)
    for i in range(100, 200):
        zkzh = str('1301701721' + str(i) + '14')'''
    start(130170172112823)

main()