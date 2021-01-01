import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import random
import os
import csv

# 最終ページ番号を取得するメソッド


def get_last_page_number(url):
    # ToDo  たまにデータ取れないときあるっぽい？
    #       取れてるかどうか確認して、取れてなかったら再度取得するようにしたほうがいいかも
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find_all('a')

    page_link = soup.find_all('a', class_='page-link')
    # ページングの最大数を格納する
    return page_link[len(page_link) - 2].text

# スクレイピングの共通メソッド


def scraping(url):
    # ToDo  たまにデータ取れないときあるっぽい？
    #       取れてるかどうか確認して、取れてなかったら再度取得するようにしたほうがいいかも
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find_all('a')

    # returnする取得するカード情報の配列
    cards_data = []

    # 複数ある項目の最大数、定数で定義
    symbol_max_count = 2
    type_max_count = 4
    n_skill_max_count = 4
    s_skill_max_count = 2

    # 取得するために使用するパターン(正規表現)
    regex = re.compile(r'^https://fecipher.jp/cards/\d+')

    for img in imgs:
        if re.match(regex, img.get('href')):
            # 乱数で処理をストップする
            time.sleep(random.random())
            # カード一覧画面から取得したカード番号
            card_no = img.get('href')[26:-12]

            # カードごとのurl
            url = 'https://fecipher.jp/cards/' + card_no
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')

            # 各カードの情報を格納する配列
            # cards_dataにappendする
            card_data = []

            # 一部切り取るものは事前に取得
            card_no = soup.find("td", class_="card_no").text
            card_name = soup.find("div", class_="card_name").h1.text

            # card_id
            card_data.append(card_no)

            # rare
            card_data.append(soup.find("td", class_="card_rarity").text)

            # recording
            card_data.append(card_no[0:3])

            # title
            card_data.append(card_name.rsplit(" ", 1)[0])

            # name
            card_data.append(card_name.rsplit(" ", 1)[1])

            # sortie_cost
            card_data.append(
                soup.find("img", alt="出撃コスト").parent.parent.dd.text)

            # cc_cost
            card_data.append(
                soup.find("img", alt="クラスチェンジコスト").parent.parent.dd.text)

            # シンボル部分の要素を一括で取得
            symbol_element = soup.find(
                "img", alt="シンボル").parent.parent.dd.find_all("img")

            # symbol1 symbol2
            for i in range(len(symbol_element)):
                card_data.append(symbol_element[i].get('alt'))
            for i in range(symbol_max_count - len(symbol_element)):
                card_data.append("")

            # gender
            card_data.append(
                soup.find("img", alt="性別").parent.parent.dd.text.strip())

            # weapon
            card_data.append(
                soup.find("img", alt="武器").parent.parent.dd.text.strip())

            # タイプ部分の要素を一括で取得
            type_element = soup.find(
                "img", alt="タイプ").parent.parent.dd.find_all("img")

            # type1 type2 type3 type4
            for i in range(len(type_element)):
                card_data.append(type_element[i].get('alt'))
            for i in range(type_max_count - len(type_element)):
                card_data.append("")

            # 基本スキル部分の要素を一括で取得
            n_skill_element = soup.find("img", alt="スキル")

            n_skill_name_element = []
            n_skill_text_element = []

            if n_skill_element is not None:
                n_skill_name_element = n_skill_element.parent.parent.find_all(
                    "dt")
                n_skill_text_element = n_skill_element.parent.parent.find_all(
                    "dd")

            # n_skill_name1 n_skill_name2 n_skill_name3 n_skill_name4
            for i in range(len(n_skill_name_element)):
                card_data.append(n_skill_name_element[i].text)
            for i in range(n_skill_max_count - len(n_skill_name_element)):
                card_data.append("")

            # ToDo:画像で表現されている部分をどうするか検討
            # n_skill_text1 n_skill_text2 n_skill_text3 n_skill_text4
            for i in range(len(n_skill_text_element)):
                card_data.append(n_skill_text_element[i].text.strip().replace(
                    '\r', '').replace('\n', '').replace(' ', ''))
            for i in range(n_skill_max_count - len(n_skill_text_element)):
                card_data.append("")

            # 支援スキル部分の要素を一括で取得
            s_skill_element = soup.find("img", alt="支援スキル")

            s_skill_name_element = []
            s_skill_text_element = []

            if s_skill_element is not None:
                s_skill_name_element = s_skill_element.parent.parent.find_all(
                    "dt")
                s_skill_text_element = s_skill_element.parent.parent.find_all(
                    "dd")

            # s_skill_name1 s_skill_name2
            for i in range(len(s_skill_name_element)):
                card_data.append(s_skill_name_element[i].text)
            for i in range(s_skill_max_count - len(s_skill_name_element)):
                card_data.append("")

            # s_skill_text1 s_skill_text2
            for i in range(len(s_skill_text_element)):
                card_data.append(s_skill_text_element[i].text.strip().replace(
                    '\r', '').replace('\n', '').replace(' ', ''))
            for i in range(s_skill_max_count - len(s_skill_text_element)):
                card_data.append("")

            # c_power
            card_data.append(
                soup.find("img", alt="戦闘力").parent.parent.dd.text.strip()
            )

            # s_power
            card_data.append(
                soup.find("img", alt="支援力").parent.parent.dd.text.strip()
            )

            # range
            card_data.append(
                soup.find("img", alt="射程").parent.parent.dd.text
            )
            # class
            card_data.append(
                soup.find("img", alt="クラス").parent.parent.dd.text
            )

            # job
            card_data.append(
                soup.find("img", alt="職業").parent.parent.dd.text
            )

            # flavor
            card_data.append(
                soup.find("p", class_="card_phrase").text.strip().replace(
                    '\r', '').replace('\n', '').replace(' ', '')
            )

            # illustrator
            illustrator = soup.find("p", class_="illustrator").text[7:]

            if illustrator.find("Autograph") > -1:
                illustrator = illustrator[:illustrator.find("Autograph")]

            card_data.append(illustrator)

            # "（なし）"は空にする
            card_data = [data.replace("（なし）", "") for data in card_data]

            cards_data.append(card_data)

    # データを追加した状態でリターン
    return cards_data

# メイン処理ここから


# csvに書き込むデータヘッダーを準備
header = ['card_id',
          'rare',
          'recording',
          'title',
          'name',
          'sortie_cost',
          'cc_cost',
          'symbol1',
          'symbol2',
          'gender',
          'weapon',
          'type1',
          'type2',
          'type3',
          'type4',
          'n_skill_name1',
          'n_skill_name2',
          'n_skill_name3',
          'n_skill_name4',
          'n_skill_text1',
          'n_skill_text2',
          'n_skill_text3',
          'n_skill_text4',
          's_skill_name1',
          's_skill_name2',
          's_skill_text1',
          's_skill_text2',
          'c_power',
          's_power',
          'range',
          'class',
          'job',
          'flavor',
          'illustrator'
          ]


url = 'https://fecipher.jp/cards/'

last_page_number = int(get_last_page_number(url))


# スクレイピングしたデータを一括で書き込む
with open('data/' + str(datetime.date.today()) + '02_cipher_data.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # ヘッダーを書き込む
    writer.writerow(header)

    '''
    1ページ目とそれ以降の構成が異なるため、別でスクレイピングをする
    '''

    # 1ページ目
    writer.writerows(scraping(url))

    print('fin scraping')

    # 2〜最終ページまでのスクレイピング
    for page_id in range(2, last_page_number + 1):
        url = 'https://fecipher.jp/cards/page/' + str(page_id)
        writer.writerows(scraping(url))

        print('fin page ' + str(page_id) + ' scraping')
