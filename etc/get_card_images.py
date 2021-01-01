import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os

# 最終ページ番号を取得するメソッド
def get_last_page_number(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find_all('a')

    page_link = soup.find_all(class_='page-link')
    # ページングの最大数を格納する
    return page_link[len(page_link) - 2].text

# スクレイピングの共通メソッド
def scraping(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find_all('a')

    # 取得するために使用するパターン(正規表現)
    regex = re.compile(r'^https://fecipher.jp/cards/\d+')

    for img in imgs:
        if re.match(regex, img.get('href')):
            # 乱数で処理をストップする
            time.sleep(random.random())
            # カード一覧画面から取得したカード番号
            card_no = img.get('href')[26:-12]
            # 取得したpngに名前をつける際に使用するcard_id
            card_id = img.next.get('src')[53:-25]
            # 取得したpngに名前をつける際に使用するunit_name
            unit_name = img.next.get('alt')
            # カードの画像を取得するためのurl
            url = 'https://fecipher.jp/cards/' + card_no
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')

            images = []

            images.append(soup.find_all('img')[6].get('src'))

            for index, target in enumerate(images):
                r = requests.get(target)

                # 収録弾ごとにフォルダを分ける
                recording_no = card_id[0:3]

                # フォルダがなければ作る
                if os.path.exists('img/' + recording_no):
                    pass
                else:
                    os.makedirs('img/' + recording_no)

                # imgフォルダに書き出す(ユニット名なし)
                with open('img/' + recording_no + '/' + card_id + '.png', 'wb') as f:
                    f.write(r.content)

                # imgフォルダに書き出す(ユニット名付き)
                # with open('img/' + recording_no + '/' + card_id + '_' + unit_name + '.png', 'wb') as f:
                #     f.write(r.content)

'''
    1ページ目とそれ以降の構成が異なるため、別でスクレイピングをする
'''

# 1ページ目
url = 'https://fecipher.jp/cards/'

scraping(url)

print('fin scraping')

# 2ページ目以降のスクレイピングを実施する前に最終ページ数を取得
last_page = get_last_page_number(url)

# 2〜最終ページまでのスクレイピング
for page_id in range(2, int(last_page) + 1):
    url = 'https://fecipher.jp/cards/page/' + str(page_id)
    scraping(url)
    print('fin page ' + str(page_id) + ' scraping')