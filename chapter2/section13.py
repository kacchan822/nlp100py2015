"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第2章: UNIXコマンドの基礎
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納した
ファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べた
テキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

確認
$ cut -f1 hightemp.txt | diff - col1.txt
$ cut -f2 hightemp.txt | diff - col2.txt
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IN1 = os.path.join(BASE_DIR, 'col1.txt')
IN2 = os.path.join(BASE_DIR, 'col2.txt')
OUT = os.path.join(BASE_DIR, 'col1_2.txt')

with open(IN1, 'r') as in1, open(IN2, 'r') as in2, open(OUT, 'w') as out:
    for in1_row, in2_row in zip(in1, in2):
        out.write(in1_row.strip() + '\t' + in2_row.strip() + '\n')
