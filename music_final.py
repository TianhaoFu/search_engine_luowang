import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('/Users/10739/Desktop/periodical.txt', "a", encoding='utf-8') as f:
    for i in range(2):
        i = i + 1
        url = "https://www.luoow.com/{}/".format(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser", from_encoding="iso-8859-1")
        titles = soup.select("body  script")  # CSS 选择器
        j = 1
        for title in titles:
            if j == 2:
                # print(title.get_text())# 标签体、标签属性
                sss = title.get_text()
                break
            if j == 1:
                j = 2
        sss = sss[sss.find("source"):].replace('{', '').replace('}', '').replace('[', '').replace(']', '')
        sss = sss.replace('"', '').replace('http://', '')
        pattern = re.compile(r'name:(.*?),')
        result = pattern.findall(sss)

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        data = requests.get(url, headers=headers).text
        s = etree.HTML(data)
        music_title = s.xpath('/html/body/div[@class="container"]/div[@class="title"]/text()')
        music_img = s.xpath('/html/body/div[@class="container"]/div[@class="cover_img"]/img/@src')
        music_tag = s.xpath('/html/body/div[@class="container"]/div[@class="tag"]/a/text()')
        music_decs = s.xpath('/html/body/div[@class="container"]/div[@class="desc"]/div[@class="vol-desc"]/text()')

        for j1 in music_title:
            f.write("标题：{}\n".format(j1))

        for j2 in music_img:
            f.write("图片：{}\n".format(j2))

        for j3 in music_tag:
            f.write("标签：{}\n".format(j3).replace("&nbsp", " "))

        for j4 in music_decs:
            f.write("{}".format(j4))

        for j5 in result:
            f.write("音乐：{}".format(j5))
            f.write("\n")

