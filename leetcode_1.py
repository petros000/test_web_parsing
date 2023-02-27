import time

import requests
from bs4 import BeautifulSoup

url = "https://leetcode.com/problemset/all/?page=2"

headers = {
    "Accept": "*/*",
    "USer-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36 "
}
# 'https://leetcode.com/problemset/all/?page=1'


def get_html(url):
    request = requests.get(url, headers=headers)
    print(request.status_code)
    time.sleep(10)
    src = request.text

    return src


def save_src_to_html(src, file_name):
    all_name = file_name + '.html'
    with open(all_name, "w", encoding="utf-8") as file:
        file.write(src)


def open_src(file_name):
    all_name = file_name + '.html'
    with open(all_name) as file:
        src = file.read()

    return src


src = get_html(url)
save_src_to_html(src, 'problems_all_2')
src = open_src('problems_all_2')
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

