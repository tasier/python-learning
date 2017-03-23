# -*- coding: UTF-8 -*-

import requests


if __name__ == '__main__':
    login_data = {'email': '964378878@qq.com',
                  'password': 'sbjjbs10517'}

    login_url = 'https://www.douban.com/accounts/login'
    someone_url = 'https://www.douban.com/people/er-mao/contacts'

    loginRequest = requests.post(login_url, login_data)
    print loginRequest.status_code

    jar = requests.cookies.RequestsCookieJar()
    r = requests.get(someone_url, cookies=jar)
    print r.text