from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
import time
import re
import random

def main():
    print('\n-- Tieba_spider v0.1 --\n')

    tieba_name = input('贴吧名：')
    page_number = int(input('页数：'))
    print('')

    print('1，保存帖子列表图片')
    go = input('\n选择需要的功能：')
    print('')

    if go == '1': save_pic(tieba_name, page_number)
    else: pass

# 业务 ------------------------------------------

def save_pic(tieba_name, page_number):
    url = r'https://tieba.baidu.com/f?kw='+ quote(tieba_name, safe='') + '&ie=utf-8'
    # path = 'D:/temp/tt/'
    path = input('\n储存路径：')
    
    j = 1
    for i in range(page_number):
        url = url + '&pn=' + str(i*50)
        html = get_html(url)
        pics = re.findall(r'<img src=.*?bpic="(.*?)".*?/>', html)
        
        for pic in pics:
            urllib.request.urlretrieve(pic,path + str(j)+'.jpg')
            time.sleep(random.uniform(0.1,0.6))

            print('已生成第 %d 张图片' % j)
            j += 1

# 模块 ------------------------------------------

def get_html(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/74.0"
    }
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    
    return response.read().decode("utf-8")

if __name__ == '__main__':
    main()