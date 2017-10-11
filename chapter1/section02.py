"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

strings1 = 'パトカー'
strings2 = 'タクシー'

result_strings = ''.join([i+j for i,j in zip(strings1, strings2)])
print(result_strings)