# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
from string import Template
import random
from time import sleep

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Referer': 'https://www.douban.com/'}

    someone_collect_url = 'https://book.douban.com/people/moshou/collect'
    someone_collect_page_url = Template(
        "https://book.douban.com/people/moshou/collect?start=${num}&amp;sort=time&amp;rating=all&amp;filter=all&amp;mode=grid")

    r = requests.get(someone_collect_url, headers=headers)
    index_soup = BeautifulSoup(r.text, 'lxml')
    # 寻找读了多少本书的标签
    subject_num_tag = index_soup.find(
        lambda tag:
        cmp(tag.name, 'span') == 0  # span标签
        and tag.has_attr('class')  # 有class属性
        and cmp(tag['class'][0], 'subject-num') == 0)  # class属性为subject-num

    if subject_num_tag is not None:
        # 1-15 / 158
        # 确定有多少本书
        num_of_books = int(subject_num_tag.string.split('/')[1].strip())

        num_of_eachpage = 15  # 每页抓取的数量
        # 分页抓取
        for num in range(0, num_of_books, num_of_eachpage):
            # 随机等待1-2秒
            random_time = random.random()
            sleep(random_time + 1.0)

            # 字符串格式化替换
            url = someone_collect_page_url.substitute(num=num)
            r = requests.get(url, headers=headers)

            # 处理抓取的每一个页面
            soup = BeautifulSoup(r.text, 'lxml')
            for item in soup.find_all('li', class_='subject-item'):
                # 获取评分标签
                book_rating_tag = item.find(
                    lambda tag:
                    cmp(tag.name, 'span') == 0  # span标签
                    and tag.has_attr('class')  # 有class属性
                    and tag['class'][0].startswith('rating'))  # class属性以rating开头

                # 判断rating是否有，对书有评价的话在操作
                # bookid,bookname,rating,bookpubinfo
                if book_rating_tag is not None:
                    # bookid
                    print item.a['href'].split('/')[4], ',',
                    # bookname
                    print item.find('div', class_='info').a['title'], ',',
                    # rating
                    print book_rating_tag['class'][0][6], ',',
                    # bookpubinfo
                    print item.find('div', class_='pub').string.strip()
