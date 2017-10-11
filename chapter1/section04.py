"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine.
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
"""

strings = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
          'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

result_dict = {}

for n, s in enumerate(strings.split()):
    if n in (1, 5, 6, 7, 8, 9, 15, 16):
        result_dict[s[:1]] = n + 1
    else:
        result_dict[s[:2]] = n + 1

print(result_dict)