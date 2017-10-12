"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．

確認
$ wc -l hightemp.txt
24 hightemp.txt
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, 'hightemp.txt')

with open(FILE, 'r') as f:
    count = 0
    for row in f:
        count += 1
    print(count)
