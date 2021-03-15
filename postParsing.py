from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dateParsing import *

DRIVER_PATH = "driver\\chromedriver.exe"  # chrome driver path
BASE_URL = "https://www.olx.ro/oferte/?search%5Bfilter_float_price%3Afrom%5D=free"  # base url to use while crawling
QUERY = ''  # search terms
BLACK_LIST = []  # unimplemented blacklist

options = Options()  # init chrome options
options.headless = True  # run headless (visually hides crawl)
options.add_argument("--window-size=1920,1080")  # default window size for testing, running headless anyways
options.add_argument(
    "load-extension=C:\\Users\\denni\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\cfhdojbkjhnklbpkdaibdccddilifddb\\3.10_0")
# todo change path to, or include extension
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)  # init webdriver on chrome settings


def parseResults(posts):
    """
    Parses the posts resulted from crawling. Optionally prints results (testing purposes)

    :param list posts: list of posts

    :rtype: list
    :return: unparsed list of results
    """
    parsedList = []
    for i, post in enumerate(posts):  # iterating posts for parsing
        postTitle = post.find('strong').getText()
        postTime = post.find('i',
                             {"data-icon": "clock"}).parent.getText()  # finds i tag and returns text of span parent
        postLocation = post.find('i', {"data-icon": "location-filled"}).parent.getText()  # looks for data icon parent
        postURL = post.find('a').get('href')  # gets href value of found post a's
        if QUERY in postTitle:  # checks query in postTitle
            print(f'{postTitle}: {dateConvert(postTime)}: {postLocation}:     {postURL}')  # test printing
            parsedList.append(f'{postTitle}:{dateConvert(postTime)}:{postLocation}:{postURL}')  # add posts to list
    return parsedList


def stepThroughPages():  # function to crawl through all pages
    """
    Crawl through the 25 pages of the OLX free section and return found posts by parsing each page's html code.

    :rtype: list
    :return: unparsed list of results
    """
    posts = []
    driver.get(BASE_URL)  # init driver on BASE_URL
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for s in soup.find_all(class_='clr tcenter'):
        s.extract()
    # lastPage = soup.find_all('a', class_='block br3 brc8 large tdnone lheight24')[-1].getText()  #error fix only
    for pageNumber in range(1, 25):  # int(lastPage)
        driver.get(BASE_URL + "&page=" + str(pageNumber))
        posts.extend(soup.find_all('div', class_='offer-wrapper'))
    return posts  # un-parsed list


def test():  # functionality testing
    totalPosts = stepThroughPages()  # get list of unparsed
    totalPosts = list(dict.fromkeys(totalPosts))  # parse posts
    parseResults(totalPosts)
    print(len(totalPosts))
    driver.quit()  # exit driver


test()
