#encoding=utf-8
import requests
from lxml import html
from IPython.display import Image
url = ['//bj.meituan.com/meishi/']
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.107 Safari/537.36"}
with open("meituan.txt","wb") as f:
    while(url):
        page = requests.get('http:'+url[0],headers=header)
        y = html.fromstring(page.content)
        url = y.xpath('//*[@class="pagination-item next-btn active"]/a/@href')
        groups = y.xpath("//div[@class='common-list-main']/div[@class='common-list-item clearfix']")
        for group in groups:
            title = group.xpath(".//div[@class='list-item-desc-top']/a[@class='item-title']/text()")[0]
            stars = group.xpath(".//div[@class='item-eval-info clearfix']/span[1]/text()")[0]
            commit_num = group.xpath(".//div[@class='item-eval-info clearfix']/span[@class='highlight']/text()")[0]
            print title,stars,commit_num
            f.writelines(title)
            f.writelines(stars)
            f.writelines(commit_num)
            f.writelines("/n")



