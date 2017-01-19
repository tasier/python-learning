import urllib2
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    quote_page = 'http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/'

    page = urllib2.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # name_box = soup.find('div', attrs={'class': 'post-content clearfix'})
    for tag in soup.find_all(re.compile("^pre")):
        print tag.code.contents[0].strip()

