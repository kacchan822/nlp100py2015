"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．

確認
$ python3 section14.py 2
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16

$ head -n2 hightemp.txt
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, 'hightemp.txt')
LINE_N = int(sys.argv[1])

with open(FILE, 'r') as f:
    for num, row in enumerate(f):
        if num + 1 > LINE_N:
            break
        else:
            print(row, end='')
