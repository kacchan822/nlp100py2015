"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとして
ファイルに保存せよ．確認にはcutコマンドを用いよ．

確認
$ cut -f1 hightemp.txt | diff - col1.txt
$ cut -f2 hightemp.txt | diff - col2.txt
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, 'hightemp.txt')
OUT1 = os.path.join(BASE_DIR, 'col1.txt')
OUT2 = os.path.join(BASE_DIR, 'col2.txt')

with open(FILE, 'r') as f, open(OUT1, 'w') as out1, open(OUT2, 'w') as out2:
    for row in f:
        cols = row.split('\t')
        out1.write(cols[0] + '\n')
        out2.write(cols[1] + '\n')
