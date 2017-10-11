"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

strings = 'I am an NLPer'

def ngram(n, strings):
    i = 0
    result_list = []
    while i <= len(strings) - n:
        result_list.append(strings[i:i+n])
        i += 1
    return result_list

print(ngram(2, strings.split()))
print(ngram(2, strings))