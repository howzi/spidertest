#encoding=utf-8
from lxml import html 

x = html.parse('http://www.bupt.edu.cn/')
titles = x.xpath("///a[@class='clear']/span[@class='main_ul_span lf']/text()")
print "We got %s titles:" % len(titles)
for title in titles:
    print title