"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

確認
tabの入力は、Ctrl + v, tabでできる。
$ sed -e "s/   / /g" hightemp.txt
高知県 江川崎 41 2013-08-12
埼玉県 熊谷 40.9 2007-08-16
岐阜県 多治見 40.9 2007-08-16
山形県 山形 40.8 1933-07-25
山梨県 甲府 40.7 2013-08-10
和歌山県 かつらぎ 40.6 1994-08-08
静岡県 天竜 40.6 1994-08-04
山梨県 勝沼 40.5 2013-08-10
埼玉県 越谷 40.4 2007-08-16
群馬県 館林 40.3 2007-08-16
群馬県 上里見 40.3 1998-07-04
愛知県 愛西 40.3 1994-08-05
千葉県 牛久 40.2 2004-07-20
静岡県 佐久間 40.2 2001-07-24
愛媛県 宇和島 40.2 1927-07-22
山形県 酒田 40.1 1978-08-03
岐阜県 美濃 40 2007-08-16
群馬県 前橋 40 2001-07-24
千葉県 茂原 39.9 2013-08-11
埼玉県 鳩山 39.9 1997-07-05
大阪府 豊中 39.9 1994-08-08
山梨県 大月 39.9 1990-07-19
山形県 鶴岡 39.9 1978-08-03
愛知県 名古屋 39.9 1942-08-02
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, 'hightemp.txt')

with open(FILE, 'r') as f:
    for line in f:
        print(line.replace('\t', ' '), end='')
