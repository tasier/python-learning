# -*- coding: UTF-8 -*-

import requests


if __name__ == '__main__':
    login_data = {'form_email': '',
                  'form_password': ''}

    login_url = 'https://accounts.douban.com/login'
    someone_url = 'https://www.douban.com/people/er-mao/contacts'

    with requests.Session() as session:
        session.post(login_url, login_data)
        r = session.get(someone_url)
        print r.text