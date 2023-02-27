import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0")
                           # "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0")
                           # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    try:
        driver = webdriver.Firefox(
            executable_path=r'C:\Users\petrs\PycharmProjects\test_web_parsing\geckodriver_32.exe',
            # executable_path="C:/Users/petrs/PycharmProjects/test_web_parsing/chromedriver.exe",
            options=options
            )
        driver.get(url=url)
        time.sleep(10)

        with open("index_selenium.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# url = "https://leetcode.com/problemset/all/?page=2"

# get_data_with_selenium(url)


def open_file(file_name):
    all_name = file_name + '.html'
    with open(all_name) as file:
        src = file.read()

    return src


src = open_file('index_selenium')
# # print(src)
soup = BeautifulSoup(src, 'lxml')
#
tasks = soup.find_all(class_="odd:bg-layer-1 even:bg-overlay-1 dark:odd:bg-dark-layer-bg dark:even:bg-dark-fill-4")
#
for task in tasks:
    task_name = task.find(class_="h-5").text
    task_link = task.find(class_="h-5").get('href')
    task_difficulty = task.find('span', class_=["text-olive", "text-yellow", "text-pink"]).text
    print(task_name, task_link, task_difficulty, sep="\n")

