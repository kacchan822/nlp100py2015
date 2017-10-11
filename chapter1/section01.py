"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

strings = 'パタトクカシーー'
result_strings = ''.join([strings[s] for s in (1,3,5,7)])
print(result_strings)