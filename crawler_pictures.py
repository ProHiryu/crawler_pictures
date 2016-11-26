# -*- coding:utf-8 -*-

# from bs4 import BeautifulSoup
# import urllib.request
#
# def retrieve(url):
#     html = urllib.request.urlopen(url)
#     soup = BeautifulSoup(html,'html.parser')
#     imgs = soup.findAll('img')
#     for img in imgs:
#         src = img.get('src')
#         print(src)
#
# if __name__ == "__main__":
#     retrieve('http://www.officeplus.cn/List.shtml?cat=IMAGE&tag=19&order=1')

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import os

srcs = []
names = []

def browser(url):
    driver = webdriver.Firefox()
    driver.get(url)
    lis = driver.find_elements_by_class_name('dlink')
    for li in lis:
        if li.get_attribute('data-href') == None:
            continue
        elif li.get_attribute('data-href') == 'http://www.officeplus.cn/images/officeplus/loading_1.jpg':
            srcs.append(li.get_attribute('lazy-src'))
        else:
            srcs.append(li.get_attribute('data-href'))
        # names.append(li.get_attribute('alt'))

def store():
    path = os.getcwd()
    new_path = os.path.join(path, u'pictures')
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    for i in range(len(srcs)):
        PATH = new_path + '\\' + str(i) + '.jpg'
        urllib.request.urlretrieve(srcs[i],PATH)
        print (i , 'sucess!' , 'NEXT PAGE!')

if __name__ == "__main__":
    browser('http://www.officeplus.cn/List.shtml?cat=IMAGE&tag=19&order=1')
    store()
    print ((srcs))
    print(len(srcs))
