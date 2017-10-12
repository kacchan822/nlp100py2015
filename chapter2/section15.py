"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．

確認
$ python3 section15.py 5
埼玉県  鳩山    39.9    1997-07-05
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02

$ tail -n5 hightemp.txt
埼玉県  鳩山    39.9    1997-07-05
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, 'hightemp.txt')
LINE_N = int(sys.argv[1])

result = []

with open(FILE, 'r') as f:
    for row in f:
        result.append(row)
        if len(result) > LINE_N:
            result.pop(0)
    print(''.join(result), end='')
