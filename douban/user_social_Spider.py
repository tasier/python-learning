# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from time import sleep
import random

if __name__ == '__main__':
    login_data = {'form_email': '',
                  'form_password': ''}

    #登陆页面
    login_url = 'https://accounts.douban.com/login'
    #关注人页面
    someone_contacts_url = 'https://www.douban.com/people/moshou/contacts'
    #被关注人页面
    someone_rev_contacts_url = 'https://www.douban.com/people/moshou/contacts'

    with open('douban_account.log') as f:
        login_data['form_email'] = f.readline().strip().split('|')[1]
        login_data['form_password'] = f.readline().strip().split('|')[1]

    with requests.Session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Referer': 'https://www.douban.com/'}

        #先获取登陆页面，分析是否包含验证码
        r = session.get(login_url)
        login_soup = BeautifulSoup(r.text, 'lxml')
        # login_soup = BeautifulSoup(open('tmp.html'), 'lxml')
        captcha_tag = login_soup.find('img', id='captcha_image')

        #如果登陆页面有验证码识别
        if captcha_tag is not None:
            #获取验证码图片的url
            image_url = captcha_tag['src']
            print image_url

            #保存验证码图片
            r = requests.get(image_url, stream=True)
            i = Image.open(StringIO(r.content))
            i.save('image.jpg')

            #获取验证码id
            captcha_input = login_soup.find(attrs={'name': 'captcha-id'})
            captcha_value = captcha_input['value']
            print captcha_input, captcha_input['value']

            #人工读取验证码
            captcha_key = raw_input('输入验证码: ')
            print captcha_key

            #post信息当中填充验证码
            login_data['captcha-solution'] = captcha_key
            login_data['captcha-id'] = captcha_value


        #login
        r = session.post(login_url, login_data, headers=headers)
        # print r.text

        #随机等待1-2秒
        random_time = random.random()
        sleep(random_time + 1.0)

        #获取所有关注人的页面
        r = session.get(someone_contacts_url, headers=headers)
        # print r.status_code
        soup = BeautifulSoup(r.text, 'lxml')
        i = 1
        #获取所有关注的人
        for tag in soup.find_all('dl', class_='obu'):
            #提取用户主页
            print '关注 ', i, tag.a['href']
            i += 1

        print '------------------------------------------------------'

        # 随机等待1-2秒
        random_time = random.random()
        sleep(random_time + 1.0)

        #获取被关注人的页面
        r = session.get(someone_rev_contacts_url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        i = 1
        for tag in soup.find_all('dl', class_='obu'):
            # 提取用户主页
            print '被关注 ', i, tag.a['href']
            i += 1
