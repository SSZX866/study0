import requests
url = "http://www.right.com.cn/FORUM/thread-180472-1-1.html"
kv = {'user-agent': 'Mozilla/5.0'}

def main():
    try:
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except:
        print("连接失败")

main()