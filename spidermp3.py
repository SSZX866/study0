import requests
import os

url = "https://vt1.doubanio.com/201712280038/ea27c7274fb39650e1fb89dba2287d42/view/movie/M/302250504.mp4"
kv = {'user-agent':'Mozilla/5.0'}
root = "D://1//"
path = root + url.split('/')[-1]
def main():
    try:
        if not os.path.exists(root):
            print("路径不存在，正在创建")
            os.mkdir(root)
            print("创建成功！")
        if not os.path.exists(path):
            print("正在保存文件...")
            r = requests.get(url,params=kv)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("保存成功！")
        else:
            print("文件已存在")
    except:
        print("保存失败！")

main()


