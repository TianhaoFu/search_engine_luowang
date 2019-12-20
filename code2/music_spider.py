'''
运行本程序需要修改点1
'''
import bs4
import bs4
import requests
from lxml import etree
import re

i = 1
with open('/Users/10739/Desktop/data_content.txt', "a", encoding='utf-8') as f:  # 1将periodical.txt所在地址拷过来
    for i in range(1000):
        url = "https://www.luoow.com/{}/".format(i)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        data = requests.get(url, headers=headers).text
        s = etree.HTML(data)
        music_title = s.xpath('/html/body/div[@class="container"]/div[@class="title"]/text()')


        songname = []
        songauthor = []
        URL = "https://www.luoow.com/{}/".format(i)
        r = requests.get(url=URL)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        titles = soup.select("body  script")
        j = 1
        for title in titles:
            if j == 2:
                # print(title.get_text())# 标签体、标签属性
                sss = title.get_text()
                sss = sss[sss.find("source"):].replace('{', '').replace('}', '').replace('[', '').replace(']', '')
                aaa = sss.replace('"', '').replace('http://', '')
                pattern1 = re.compile(r'name:(.*?),')
                pattern2 = re.compile(r'author:(.*?),')
                songname = pattern1.findall(aaa)
                songauthor = pattern2.findall(aaa)
                break
            if j == 1:
                j = 2

        for j1 in music_title:
            f.write("期刊名：{}\n".format(j1))

        for j4 in songname:
            f.write("歌曲名：{}\n".format(j4))

        for j5 in songauthor:
            f.write("歌手：{}\n".format(j5))



